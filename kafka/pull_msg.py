from kafka import KafkaConsumer
import json
import datetime

# Kafka配置
KAFKA_SERVER = "192.168.1.133:9092"  # 修改为你的Kafka服务器地址
TOPIC = "AIRCRAFT"


def pull():
    # 创建消费者
    consumer = KafkaConsumer(
        "OPEN_API_DEVICE_EVENT",
        bootstrap_servers="47.111.155.82:30090",
        auto_offset_reset="earliest",  # 从最早的消息开始读取
        enable_auto_commit=True,  # 自动提交偏移量
        group_id="file_logger_group",  # 设置消费者组
    )

    # 创建日志文件，文件名包含当前日期时间
    log_filename = (
        f"kafka_messages_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    )

    try:
        with open(log_filename, "a", encoding="utf-8") as log_file:
            print(f"开始接收消息，日志文件: {log_filename}")

            for message in consumer:
                # 解码消息
                message_value = message.value.decode("utf-8")
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # 打印到控制台
                print(f"[{timestamp}] 收到消息: {message_value}")

                # 写入文件
                log_entry = f"[{timestamp}] {message_value}\n"
                log_file.write(log_entry)
                log_file.flush()  # 确保立即写入磁盘

    except KeyboardInterrupt:
        print("\n程序被用户中断")
    except Exception as e:
        print(f"发生错误: {e}")
    finally:
        consumer.close()
        print("消费者已关闭")


if __name__ == "__main__":
    pull()
