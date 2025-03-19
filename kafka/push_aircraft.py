from kafka import KafkaProducer
import json

# Kafka配置
KAFKA_SERVER = '192.168.1.133:9092'  # 修改为你的Kafka服务器地址
TOPIC = 'AIRCRAFT'

# 要推送的数据
data = {
    "method": "OnEventNotify",
    "params": "{\"clients\":[\"uavms\",\"uavrpmsweb\"],\"uids\":[\"ljp\",\"test01\",\"tangtang\",\"admin\"],\"ability\":\"event_uav\",\"quids\":[\"ljp\",\"test01\",\"tangtang\",\"admin\"],\"events\":[{\"eventId\":\"CF477AD7-5F82-FF4A-930F-9AFFD59301F3\",\"srcName\":\"Camera_01\",\"data\":{\"dateTime\":\"2024-12-28T11:33:35.173+08:00\",\"dataProcInterval\":\"4\",\"portNo\":8257,\"recvTime\":\"2024-12-28T11:33:35.186+08:00\",\"dataType\":\"uavGps\",\"ipAddress\":\"\",\"targetAttrs\":{\"deviceIndexCode\":\"8b78dc690ada448ca7b55425e1915b43\",\"recognitionSign\":1,\"channelName\":\"Camera_01\",\"picServerIndexCode\":\"\",\"cameraIndexCode\":\"4b47720096fa453980491a93cf061a1d\",\"cameraType\":\"COMMON\"},\"channelName\":\"Camera_01\",\"eventType\":\"uavGpsCollection\",\"gpsCollection\":[{\"UAVStatus\":{\"BatteryRemaining\":100,\"PitchAngle\":-0.5729579925537109,\"HorizontalSpeed\":0.01999999955296516,\"Latitude\":30.06617164611816,\"RouteId\":\"\",\"RouteStatus\":255,\"Longitude\":106.6958236694336,\"HorizonalView\":5084,\"SensorSize\":28,\"Focus\":535,\"UavMode\":1,\"RollAngle\":-1.718873023986816,\"RelativeHeight\":0,\"VerticalView\":2993,\"YawAngle\":32.86999893188477,\"VerticalSpeed\":-0.02999999932944775},\"GSStatus\":{\"DataRadioRSSI\":0,\"DivisionEW\":\"E\",\"Latitude\":106.6958236694336,\"ImageRSSI\":0,\"GimbalYaw\":3254,\"Longitude\":30.06617164611816,\"GimbalPitchAngle\":88},\"targetAttrs\":{\"deviceIndexCode\":\"8b78dc690ada448ca7b55425e1915b43\",\"recognitionSign\":1,\"channelName\":\"Camera_01\",\"picServerIndexCode\":\"\",\"cameraIndexCode\":\"4b47720096fa453980491a93cf061a1d\",\"cameraType\":\"COMMON\"}}],\"channelID\":1,\"sendTime\":\"2024-12-28T11:33:35.190+08:00\"},\"srcParentIndex\":\"8b78dc690ada448ca7b55425e1915b43\",\"eventType\":852225,\"srcIndex\":\"8b78dc690ada448ca7b55425e1915b43\",\"srcType\":\"encodeDevice\",\"timeout\":0,\"happenTime\":\"2024-12-28T11:33:35.173+08:00\",\"status\":0}],\"sendTime\":\"2024-12-28T11:33:35.190+08:00\"}"
}

# 创建Kafka生产者
producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,  # Kafka服务器地址
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # 序列化JSON数据
)

# 发送数据到Kafka
producer.send(TOPIC, value=data)

# 确保所有消息发送完成
producer.flush()

# 打印发送成功消息
print(f"消息已发送到Kafka的 topic: {TOPIC}")

# 关闭Kafka连接
producer.close()
