#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import csv
import json
import time
import platform
from datetime import datetime
from kafka import KafkaProducer

KAFKA_BOOTSTRAP_SERVERS = ["192.168.1.132:9092"]
KAFKA_USERNAME = "admin"
KAFKA_PASSWORD = "Ap2uH77YyYW5n8ddFHt7"
KAFKA_TOPIC = "AIRCRAFT_STATE"
DEVICE_SN = "SN-001"

CSV_PATH = r"d:/temp/1.csv" if platform.system().lower() == "windows" else "/home/cml/1.csv"


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


def read_csv(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"文件不存在: {file_path}")

    result = []

    with open(file_path, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)

        for index, row in enumerate(reader, start=1):
            try:
                # 跳过空行
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
                    "elevation":float(row["APEN_z"]),
                    "head": float(row["GIM1_ym"]),
                    "pitch": float(row["GIMS_pitch"]),
                    "zoom": float(row["zoom"])
                }

                result.append(data)

            except Exception as e:
                print(f"第{index}行处理失败，跳过，原因: {e}, 数据: {row}")
                continue

    return result


def send_to_kafka(producer, topic, data_list):
    length = len(data_list)
    for item in data_list:
        future = producer.send(topic, item)
        meta = future.get(timeout=10)

        print(f"发送成功,total:{length} -> partition={meta.partition}, offset={meta.offset}")

        # time.sleep(1)

    producer.flush()


def main():
    try:
        print(f"读取文件: {CSV_PATH}")

        data_list = read_csv(CSV_PATH)
        print(f"共读取 {len(data_list)} 条数据")

        producer = create_producer()
        send_to_kafka(producer, KAFKA_TOPIC, data_list)

        print("发送完成")

    except Exception as e:
        print(f"执行失败: {e}")


if __name__ == "__main__":
    main()