import json
import time
import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk
from uuid import uuid4
from confluent_kafka import Producer, KafkaError
from datetime import datetime, timezone
import threading
import queue


class KafkaMessageSenderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kafka消息发送工具")
        self.root.geometry("900x700")
        self.root.minsize(800, 600)

        # 设置中文字体
        self.font = ("SimHei", 10)

        # 创建消息队列用于线程间通信
        self.log_queue = queue.Queue()

        # 初始化Kafka生产者为None
        self.producer = None

        # 存储当前配置
        self.current_config = {
            "bootstrap.servers": "192.168.1.93:9092",
            "client.id": "python-producer-" + str(uuid4()),            
            "retries": 0,   #发送消息的重试次数
            
            "socket.timeout.ms": 1000,  # 设置超时值
            "request.timeout.ms": 1000,  # 设置超时值
            "reconnect.backoff.ms": 0,  # 设置重连间隔为0毫秒
            "error_cb": self.error_callback
        }

        # 连续发送控制变量
        self.continuous_sending = False
        self.continuous_message_data = {}

        self.create_widgets()
        self.start_log_consumer()
        self.generate_example_message()

    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Kafka配置区域
        config_frame = ttk.LabelFrame(main_frame, text="Kafka配置", padding="10")
        config_frame.pack(fill=tk.X, pady=5)

        ttk.Label(config_frame, text="Bootstrap Servers:", font=self.font).grid(
            row=0, column=0, sticky=tk.W, pady=5
        )
        self.bootstrap_servers_var = tk.StringVar(
            value=self.current_config["bootstrap.servers"]
        )
        ttk.Entry(
            config_frame,
            textvariable=self.bootstrap_servers_var,
            width=50,
            font=self.font,
        ).grid(row=0, column=1, sticky=tk.W, pady=5)

        ttk.Label(config_frame, text="Client ID:", font=self.font).grid(
            row=1, column=0, sticky=tk.W, pady=5
        )
        self.client_id_var = tk.StringVar(value=self.current_config["client.id"])
        ttk.Entry(
            config_frame, textvariable=self.client_id_var, width=50, font=self.font
        ).grid(row=1, column=1, sticky=tk.W, pady=5)

        ttk.Button(
            config_frame,
            text="连接Kafka",
            command=self.connect_kafka,
            width=15,
            style="Accent.TButton",
        ).grid(row=0, column=2, rowspan=2, padx=10, pady=5)

        # 消息内容区域
        message_frame = ttk.LabelFrame(main_frame, text="消息内容", padding="10")
        message_frame.pack(fill=tk.BOTH, expand=True, pady=5)

        ttk.Label(message_frame, text="Topic:", font=self.font).grid(
            row=0, column=0, sticky=tk.W, pady=5
        )
        self.topic_var = tk.StringVar(value="AIRCRAFT_STATE")
        ttk.Entry(
            message_frame, textvariable=self.topic_var, width=30, font=self.font
        ).grid(row=0, column=1, sticky=tk.W, pady=5)

        ttk.Button(
            message_frame,
            text="生成示例消息",
            command=self.generate_example_message,
            width=15,
        ).grid(row=0, column=2, padx=5, pady=5)
        ttk.Button(
            message_frame, text="清空消息", command=self.clear_message, width=15
        ).grid(row=0, column=3, padx=5, pady=5)

        self.message_text = scrolledtext.ScrolledText(
            message_frame, wrap=tk.WORD, width=80, height=10, font=self.font
        )
        self.message_text.grid(
            row=1, column=0, columnspan=4, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5
        )

        # 按钮区域
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=5)

        self.send_button = ttk.Button(
            button_frame,
            text="发送消息",
            command=self.send_message,
            width=20,
        )
        self.send_button.pack(pady=10)

    def log(self, message):
        """用于打印和显示日志信息"""
        self.log_queue.put(message)

    def start_log_consumer(self):
        """开始日志消费者线程，显示日志"""
        def _consume_logs():
            while True:
                log_message = self.log_queue.get()
                if log_message == "STOP":
                    break
                self.message_text.insert(tk.END, log_message + "\n")
                self.message_text.yview(tk.END)

        threading.Thread(target=_consume_logs, daemon=True).start()

    def generate_example_message(self):
        """生成示例消息"""
        message = {
            "event_time": datetime.now(timezone.utc).isoformat(),
            "uuid": str(uuid4()),
            "sensor_data": {"temperature": 22.5, "humidity": 60},
        }
        self.message_text.delete(1.0, tk.END)
        self.message_text.insert(tk.END, json.dumps(message, indent=4))

    def clear_message(self):
        """清空消息框"""
        self.message_text.delete(1.0, tk.END)

    def connect_kafka(self):
        """使用线程连接Kafka，避免阻塞主线程"""
        def _connect():
            try:
                self.log(f"连接Kafka服务器{self.bootstrap_servers_var.get()}")
                self.current_config["bootstrap.servers"] = self.bootstrap_servers_var.get()
                self.current_config["client.id"] = self.client_id_var.get()
                if self.producer:
                    self.producer.flush(2)

                self.producer = None
                self.producer = Producer(self.current_config)

                # 连接成功的回调
                self.root.after(0, lambda: messagebox.showinfo("连接成功", "连接完成"))

            except KafkaError as e:
                self.log(f"连接失败: {str(e)}")
                self.producer = None
                # 错误回调处理
                self.root.after(0, lambda: messagebox.showerror("连接失败", str(e)))
            except Exception as e:
                self.log(f"连接失败: {str(e)}")
                self.producer = None
                # 错误回调处理
                self.root.after(0, lambda: messagebox.showerror("连接失败", str(e)))

        # 将连接Kafka的过程放到单独的线程中
        threading.Thread(target=_connect, daemon=True).start()

    def error_callback(self, err):
        """Kafka连接错误回调"""
        self.log("Kafka连接回调")
        if err:
            error_code = err.code()
            error_name = err.name()
            error_reason = err.str()
            is_fatal = err.fatal()
            is_broker_error = err.is_broker_error()
            self.log(f"错误码: {error_code}")
            self.log(f"错误名称: {error_name}")
            self.log(f"错误原因: {error_reason}")
            self.log(f"是否致命: {is_fatal}")
            self.log(f"是否为Broker错误: {is_broker_error}")
        else:
            self.log("没有错误")

    def send_message(self):
        """发送消息到Kafka"""
        def _send():
            try:
                topic = self.topic_var.get()
                message_content = self.message_text.get(1.0, tk.END).strip()
                if not message_content:
                    messagebox.showwarning("错误", "消息内容不能为空")
                    return

                self.producer.produce(topic, message_content, callback=self.delivery_callback)
                self.producer.flush(10)
                self.log(f"消息已发送到主题 {topic}")
            except Exception as e:
                self.log(f"发送失败: {str(e)}")
                messagebox.showerror("发送失败", str(e))

        threading.Thread(target=_send, daemon=True).start()

    def delivery_callback(self, err, msg):
        """生产者消息发送结果回调"""
        if err is not None:
            self.log(f"消息发送失败: {err}")
        else:
            self.log(f"消息发送成功: {msg.topic} {msg.partition} {msg.offset}")


if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style()

    try:
        if "clam" in style.theme_names():
            style.theme_use("clam")
    except:
        pass

    style.configure("TLabel", font=("SimHei", 10))
    style.configure("TButton", font=("SimHei", 10))
    style.configure("TEntry", font=("SimHei", 10))
    style.configure("TFrame", background="#f0f0f0")
    style.configure("TLabelframe", background="#f0f0f0")
    style.configure(
        "TLabelframe.Label", background="#f0f0f0", font=("SimHei", 10, "bold")
    )
    style.configure("Accent.TButton", foreground="white", background="#4a86e8")

    app = KafkaMessageSenderApp(root)
    root.mainloop()
