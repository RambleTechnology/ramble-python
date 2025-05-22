import json
import time
from uuid import uuid4
from confluent_kafka import Producer, KafkaError
from datetime import datetime, timezone, timedelta
from datetime import datetime, timezone
import random

# Kafka配置
kafka_config = {
    "bootstrap.servers": "192.168.1.145:9092",  # Kafka服务器地址
    "client.id": "python-producer-" + str(uuid4()),
}

# 创建Kafka生产者实例
producer = Producer(kafka_config)

# 定义飞机状态主题
TOPIC = "AIRCRAFT_STATE"


def delivery_report(err, msg):
    """消息传递回调函数，用于处理消息发送结果"""
    if err is not None:
        print(f"消息发送失败: {err}")
    else:
        print(
            f"消息已成功发送到 {msg.topic()} [{msg.partition()}]，偏移量: {msg.offset()}"
        )


def generate_aircraft_data():
    """生成模拟的飞机状态数据（sn固定为device1-10）"""
    # 获取当前UTC时间并转换为UTC+8
    utc_now = datetime.now(timezone.utc)
    beijing_tz = timezone(timedelta(hours=8))
    beijing_now = utc_now.astimezone(beijing_tz)

    # 从北京时间获取毫秒级时间戳
    timestamp = int(beijing_now.timestamp() * 1000)

    # 固定基准点（84坐标系）
    base_lon = 121.41656079345167
    base_lat = 31.112601183948296

    # 生成 device1 到 device10 之间的随机设备编号
    device_id = f"device{random.randint(1, 1)}"

    # 格式化为 YYYY-MM-DD HH:MM:SS
    time_str = beijing_now.strftime("%Y-%m-%d %H:%M:%S")

    # 经纬度在基准点附近随机波动（±0.001° 约等于 ±110米）
    longitude = round(base_lon + random.uniform(-0.001, 0.001), 8)
    latitude = round(base_lat + random.uniform(-0.001, 0.001), 8)

    # head固定为四个值之一
    head_values = [0, 90, 180, 360]
    head = random.choice(head_values)

    # pitch固定为20度
    pitch = 20.0

    return {
        "sn": device_id,
        "timestamp": timestamp,
        "time": time_str,
        "longitude": str(longitude),  # 保持字符串格式
        "latitude": str(latitude),  # 保持字符串格式
        "height": 120,
        "elevation": round(100 + (500 * (hash(uuid4()) % 100) / 100), 2),
        "head": head,  # 从预设值中选择
        "roll": round((hash(uuid4()) % 40) - 20, 2),
        "pitch": pitch,  # 固定为20度
    }


def generate_aircraft_data2():
    # 获取当前UTC时间并转换为UTC+8
    utc_now = datetime.now(timezone.utc)
    beijing_tz = timezone(timedelta(hours=8))
    beijing_now = utc_now.astimezone(beijing_tz)

    # 从北京时间获取毫秒级时间戳
    timestamp = int(beijing_now.timestamp() * 1000)
    # 格式化为 YYYY-MM-DD HH:MM:SS
    time_str = beijing_now.strftime("%Y-%m-%d %H:%M:%S")

    return {
        "sn": "device3",
        "timestamp": timestamp,
        "time": time_str,
        "longitude": "106.5294647",
        "latitude": "29.58119202",
        "height": 77.15307617,
        "elevation": round(100 + (500 * (hash(uuid4()) % 100) / 100), 2),
        "head": -129.531311,
        "roll": round((hash(uuid4()) % 40) - 20, 2),
        "pitch": -26.9856739,
    }


def send_aircraft_data(producer, topic, data):
    """发送飞机状态数据到Kafka"""
    try:
        # 将数据转换为JSON格式
        json_data = json.dumps(data).encode("utf-8")

        # 异步发送消息
        producer.produce(topic=topic, value=json_data, callback=delivery_report)

        # 等待消息发送回调
        producer.poll(0)

    except Exception as e:
        print(f"发送消息时发生错误: {str(e)}")


def main():
    try:
        # 发送10条测试消息
        for _ in range(10):
            # 生成飞机状态数据
            # aircraft_data = generate_aircraft_data()
            aircraft_data = generate_aircraft_data2()

            # 发送数据
            send_aircraft_data(producer, TOPIC, aircraft_data)

            # 模拟数据生成间隔
            time.sleep(1)

        # 确保所有消息都被发送
        producer.flush()

    except KeyboardInterrupt:
        print("\n程序被用户中断")
    finally:
        # 关闭生产者连接
        producer.poll(1)
        producer.flush()
        print("生产者已关闭")


if __name__ == "__main__":
    main()
