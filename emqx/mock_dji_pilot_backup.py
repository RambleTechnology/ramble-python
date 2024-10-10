import paho.mqtt.client as mqtt
import time
from datetime import datetime
import uuid
import json
import random

# MQTT 连接设置
BROKER = "192.168.1.82"
PORT = 1883

# 主题：thing/product/+/osd
osd_topic_prefix = "thing/product/"
osd_topic_suffix = "/osd"


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")


# 获取设备实时状态
def generate_json():
    # 生成 UUID 和当前时间戳
    tid = str(uuid.uuid4())
    bid = str(uuid.uuid4())
    timestamp = int(time.time() * 1000)  # 当前时间的毫秒级时间戳

    # 构建 JSON 对象
    json_object = {
        "tid": tid,
        "bid": bid,
        "timestamp": timestamp,
        "data": {
            "attitude_head": 80,
            "attitude_roll": 80,
            "attitude_pitch": 80,
            "longitude": 120.098,
            "latitude": 30.098,
            "height": 66,
            "elevation":77,
            "job_number": 492,
            "acc_time": 1859010,
            "activation_time": 0,
            "maintain_status": {
                "maintain_status_array": [
                    {
                        "state": 0,
                        "last_maintain_type": 17,
                        "last_maintain_time": 0,
                        "last_maintain_work_sorties": 0,
                    }
                ]
            },
            "electric_supply_voltage": 231,
            "working_voltage": 25440,
            "working_current": 1120,
            "backup_battery": {"voltage": 26631, "temperature": 27.9, "switch": 1},
            "drone_battery_maintenance_info": {
                "maintenance_state": 0,
                "maintenance_time_left": 0,
            },
        },
        "gateway": "dock_sn",
    }

    return json.dumps(json_object, indent=4)


def publish_messages():
    # 创建 MQTT 客户端实例
    client = mqtt.Client()
    client.on_connect = on_connect

    # 连接到 MQTT 代理
    client.connect(BROKER, PORT, 60)

    # 启动网络循环
    client.loop_start()

    try:
        while True:
            # 发布消息到主题
            # sn = f"device{uuid.uuid1()}"
            sn = f"device{ random.randint(1, 9)}"
            device_sn = sn.replace("-", "")
            # timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # message = f"Hello from Program A! Timestamp: {timestamp}"
            topic = osd_topic_prefix + device_sn + osd_topic_suffix
            message = generate_json()
            client.publish(topic, message)
            print(f"Message '{message}' published to topic '{topic}'")
            # 等待 2 秒
            time.sleep(2)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        client.loop_stop()
        client.disconnect()


def main():
    publish_messages()


if __name__ == "__main__":
    main()
