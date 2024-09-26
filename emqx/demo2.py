import paho.mqtt.client as mqtt

# 定义消息回调函数
def on_message(client, userdata, message):
    print(f"Received message '{message.payload.decode()}' on topic '{message.topic}'")

# 创建 MQTT 客户端实例
client = mqtt.Client()

# 设置连接回调函数（可选）
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # 订阅主题（根据需要订阅）
    client.subscribe("your/topic")

client.on_connect = on_connect

# 注册消息回调函数
client.on_message = on_message

# 连接到 MQTT 代理
client.connect("192.168.1.82", 1883, 60)  # 替换为实际的代理地址和端口
client.publish("your/topic",payload="999",qos=0)

# 启动网络循环以处理消息
client.loop_start()

# 保持主线程运行
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Exiting...")
finally:
    client.loop_stop()
    client.disconnect()
