# ...existing code...
from kafka import KafkaProducer
import json

# Kafka配置
# KAFKA_SERVER = '192.168.1.182:9092'  # 修改为你的Kafka服务器地址
KAFKA_SERVER = '192.168.1.145:9092' 
TOPIC = 'AIRCRAFT_STATE'

# 要推送的数据
data = {
    "sn": "device3",
    "longitude": "106.5294647",
    "latitude": "29.58119202",
    "height": 77.15307617,
    "elevation": 100,
    "head": -129.531311,
    "roll": 90,
    "pitch": -26.9856739,
}

# 创建Kafka生产者（修复语法错误：在 value_serializer 后添加缺失的逗号）
producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,  # Kafka服务器地址
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),  # <-- 已添加逗号
    # security_protocol='SASL_PLAINTEXT',  # 如果需要 TLS，改为 'SASL_SSL' 并配置 SSL 参数
    # sasl_mechanism='PLAIN',
    # sasl_plain_username='admin',
    # sasl_plain_password='Ap2uH77YyYW5n8ddFHt7'
)

# 发送数据到Kafka
# ...existing code...
# 同步等待发送结果（阻塞，适合脚本或需要确认的场景）
try:
    future = producer.send(TOPIC, value=data)
    record_metadata = future.get(timeout=10)  # 等待最多10秒
    print(f"发送成功：topic={record_metadata.topic}, partition={record_metadata.partition}, offset={record_metadata.offset}, timestamp={record_metadata.timestamp}")
except Exception as e:
    print(f"发送失败（同步）：{e}")

# 或者使用回调（非阻塞，适合高吞吐场景）
def on_send_success(record_metadata):
    print(f"回调：发送成功 topic={record_metadata.topic}, partition={record_metadata.partition}, offset={record_metadata.offset}")

def on_send_error(excp):
    print(f"回调：发送失败：{excp}")

producer.send(TOPIC, value=data).add_callback(on_send_success).add_errback(on_send_error)

# 确保所有消息发送完成（等待回调执行）
producer.flush()

# 打印消息内容（可选）
print(f"消息发送流程已完成，topic: {TOPIC}，消息内容：{data}")

# 关闭Kafka连接
producer.close()
# ...existing code...