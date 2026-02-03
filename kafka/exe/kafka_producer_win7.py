# kafka_producer_win7.py
from kafka import KafkaProducer
import json
import sys

def push_to_kafka():
    try:
        producer = KafkaProducer(
            bootstrap_servers="47.111.155.82:30090",
            value_serializer=lambda v: json.dumps(v).encode("utf-8")
        )
        data = {"a": 1}
        producer.send("OPEN_API_DEVICE_EVENT", value=data)
        producer.flush()
        producer.close()
        print("消息已成功发送到Kafka")
        return True
    except Exception as e:
        print(f"发送消息时出错: {str(e)}")
        return False

if __name__ == "__main__":
    print("正在尝试发送消息到Kafka服务器...")
    success = push_to_kafka()
    if success:
        print("操作成功完成")
    else:
        print("操作失败")
    input("按Enter键退出...")  # 保持窗口打开