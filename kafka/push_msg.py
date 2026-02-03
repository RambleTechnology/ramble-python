from kafka import KafkaProducer
from kafka import KafkaConsumer
import json


def push2():
    producer = KafkaProducer(
       bootstrap_servers="47.111.155.82:30090"
         # bootstrap_servers="192.168.1.145:9092",  # Kafka服务器地址
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),  # 序列化JSON数据
    )
    data = {"a": 1}
    producer.send("OPEN_API_DEVICE_EVENT", value=data)

    producer.flush()

    # 打印发送成功消息
    print(f"消息已发送到Kafka的")

    # 关闭Kafka连接
    producer.close()


if __name__ == "__main__":
    push2()
