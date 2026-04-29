#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import csv
import json
import time
import platform
import threading
from datetime import datetime
from kafka import KafkaProducer

# KAFKA_BOOTSTRAP_SERVERS = ["192.168.1.132:9092"]
KAFKA_BOOTSTRAP_SERVERS = ["44.69.16.4:9092"]
KAFKA_USERNAME = "admin"
KAFKA_PASSWORD = "Ap2uH77YyYW5n8ddFHt7"
KAFKA_TOPIC = "AIRCRAFT_STATE"
DEVICE_SN = "SN002"

CSV_PATH = r"d:/temp/mock_aircraft_flight_data.csv" if platform.system().lower() == "windows" else "/opt/ngh-smart/ngh-file/aircraft/mock_aircraft_flight_data.csv"

POLL_INTERVAL = 2       # 每次执行完毕后延迟秒数
FILE_RETRY_TIMES = 3    # 文件被占用时最大重试次数
FILE_RETRY_DELAY = 0.5  # 文件被占用时每次重试间隔秒数


def create_producer():
    return KafkaProducer(
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        security_protocol="SASL_PLAINTEXT",
        sasl_mechanism="PLAIN",
        sasl_plain_username=KAFKA_USERNAME,
        sasl_plain_password=KAFKA_PASSWORD,
        value_serializer=lambda v: json.dumps(v, ensure_ascii=False).encode("utf-8")
    )


def build_datetime(row):
    return datetime(
        int(row["DATE_year"]),
        int(row["DATE_month"]),
        int(row["DATE_day"]),
        int(row["DATE_hour"]),
        int(row["DATE_minute"]),
        int(row["DATE_second"])
    )


def try_open_file(file_path, retries=FILE_RETRY_TIMES, delay=FILE_RETRY_DELAY):
    """
    尝试打开文件，若文件被占用则重试。
    返回文件句柄，失败则抛出异常。
    """
    last_error = None
    for attempt in range(1, retries + 1):
        try:
            f = open(file_path, "r", encoding="utf-8-sig", newline="")
            return f
        except PermissionError as e:
            last_error = e
            print(f"文件被占用，第{attempt}/{retries}次重试，等待{delay}s... ({e})")
            time.sleep(delay)
        except OSError as e:
            # Windows 文件锁定通常是 OSError/WinError 32
            if hasattr(e, 'winerror') and e.winerror == 32:
                last_error = e
                print(f"文件被占用(WinError 32)，第{attempt}/{retries}次重试，等待{delay}s...")
                time.sleep(delay)
            else:
                raise
    raise IOError(f"文件 {file_path} 无法读取，已重试{retries}次: {last_error}")


def read_csv(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"文件不存在: {file_path}")

    result = []

    f = try_open_file(file_path)
    try:
        reader = csv.DictReader(f)
        for index, row in enumerate(reader, start=1):
            try:
                if not any(row.values()):
                    continue
                if all(str(v).strip() == "" for v in row.values()):
                    continue

                dt = build_datetime(row)

                data = {
                    "sn": DEVICE_SN,
                    "timestamp": int(dt.timestamp() * 1000),
                    "time": dt.strftime("%Y-%m-%d %H:%M:%S"),
                    "longitude": float(row["APEG_glo"]),
                    "latitude": float(row["APEG_gla"]),
                    "height": float(row["APEN_z"]),
                    "elevation": float(row["APEN_z"]),
                    "head": float(row["GIM1_ym"]),
                    "pitch": float(row["GIMS_pitch"]),
                    "zoom": float(row["zoom"])
                }

                result.append(data)

            except Exception as e:
                print(f"第{index}行处理失败，跳过，原因: {e}, 数据: {row}")
                continue
    finally:
        f.close()

    return result


def send_to_kafka(producer, topic, data_list):
    length = len(data_list)
    for item in data_list:
        future = producer.send(topic, item)
        meta = future.get(timeout=10)
        print(f"发送成功, total:{length} -> partition={meta.partition}, offset={meta.offset}")

    producer.flush()


# ── 停止标志 ──────────────────────────────────────────────
_stop_event = threading.Event()


def schedule_task(producer):
    """
    链式调度：本次任务执行完毕后，延迟 POLL_INTERVAL 秒再调度下一次。
    通过 _stop_event 实现优雅退出。
    """
    if _stop_event.is_set():
        return

    try:
        print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 开始读取文件: {CSV_PATH}")
        data_list = read_csv(CSV_PATH)
        print(f"共读取 {len(data_list)} 条数据")

        if data_list:
            print(data_list[0])
            send_to_kafka(producer, KAFKA_TOPIC, data_list)
            print("本轮发送完成")
        else:
            print("本轮无有效数据，跳过发送")

    except FileNotFoundError as e:
        print(f"[警告] {e}，等待下次重试")
    except IOError as e:
        print(f"[警告] 文件读取失败: {e}，等待下次重试")
    except Exception as e:
        print(f"[错误] 本轮执行异常: {e}")

    finally:
        # 无论成功或失败，延迟后调度下一轮（链式）
        if not _stop_event.is_set():
            timer = threading.Timer(POLL_INTERVAL, schedule_task, args=(producer,))
            timer.daemon = True
            timer.start()


def main():
    print("启动链式定时任务，Ctrl+C 退出")
    try:
        producer = create_producer()
    except Exception as e:
        print(f"Kafka Producer 创建失败: {e}")
        return

    # 立即启动第一轮
    schedule_task(producer)

    # 主线程等待，直到 Ctrl+C
    try:
        while not _stop_event.is_set():
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\n收到退出信号，正在停止...")
        _stop_event.set()
        time.sleep(POLL_INTERVAL + 1)  # 等待最后一个 Timer 自然结束
        producer.close()
        print("已退出")


if __name__ == "__main__":
    main()