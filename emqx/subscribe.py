import paho.mqtt.client as mqtt

# MQTT 连接设置
BROKER = "192.168.1.82"
PORT = 1883
TOPIC = "test/1/osd"

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # 订阅主题
    client.subscribe(TOPIC)
    print(f"Subscribed to topic '{TOPIC}'")

def on_message(client, userdata, message):
    print(f"Received message '{message.payload.decode()}' on topic '{message.topic}'")

# 创建 MQTT 客户端实例
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# 连接到 MQTT 代理
client.connect(BROKER, PORT, 60)

# 启动网络循环
client.loop_forever()
