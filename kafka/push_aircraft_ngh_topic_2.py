import json
import time
import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk
from uuid import uuid4
from confluent_kafka import Producer, KafkaError
from datetime import datetime, timezone, timedelta
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
            "bootstrap.servers": "192.168.1.145:9092",
            "client.id": "python-producer-" + str(uuid4()),
        }

        # 存储按钮引用的变量
        self.continuous_send_button = None
        self.stop_send_button = None

        self.create_widgets()
        self.start_log_consumer()

        # 生成示例消息
        self.generate_example_message()

    def create_widgets(self):
        # 创建主框架
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
            message_frame, wrap=tk.WORD, width=80, height=15, font=self.font
        )
        self.message_text.grid(
            row=1, column=0, columnspan=4, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5
        )

        # 按钮区域
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=5)

        # 创建按钮并保存引用
        self.send_button = ttk.Button(
            button_frame,
            text="发送消息",
            command=self.send_message,
            width=20,
            style="Accent.TButton",
        )
        self.send_button.pack(side=tk.LEFT, padx=5)

        self.continuous_send_button = ttk.Button(
            button_frame,
            text="连续发送",
            command=self.start_continuous_sending,
            width=20,
        )
        self.continuous_send_button.pack(side=tk.LEFT, padx=5)

        self.stop_send_button = ttk.Button(
            button_frame,
            text="停止发送",
            command=self.stop_continuous_sending,
            width=20,
            state=tk.DISABLED,
        )
        self.stop_send_button.pack(side=tk.LEFT, padx=5)

        # 日志区域
        log_frame = ttk.LabelFrame(main_frame, text="操作日志", padding="10")
        log_frame.pack(fill=tk.BOTH, expand=True, pady=5)

        self.log_text = scrolledtext.ScrolledText(
            log_frame, wrap=tk.WORD, width=80, height=10, font=self.font
        )
        self.log_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.log_text.config(state=tk.DISABLED)

        # 设置权重使界面可伸缩
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)
        main_frame.rowconfigure(3, weight=1)

        message_frame.columnconfigure(0, weight=1)
        message_frame.columnconfigure(1, weight=1)
        message_frame.rowconfigure(1, weight=1)

        log_frame.columnconfigure(0, weight=1)
        log_frame.rowconfigure(0, weight=1)

    def generate_example_message(self):
        """生成示例消息内容"""
        utc_now = datetime.now(timezone.utc)
        beijing_tz = timezone(timedelta(hours=8))
        beijing_now = utc_now.astimezone(beijing_tz)

        timestamp = int(beijing_now.timestamp() * 1000)
        time_str = beijing_now.strftime("%Y-%m-%d %H:%M:%S")

        example_data = {
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

        self.message_text.delete(1.0, tk.END)
        self.message_text.insert(
            tk.END, json.dumps(example_data, indent=2, ensure_ascii=False)
        )

    def clear_message(self):
        """清空消息文本框"""
        self.message_text.delete(1.0, tk.END)

    def connect_kafka(self):
        """连接到Kafka服务器"""
        self.log("正在连接Kafka服务器...")

        # 更新配置
        self.current_config["bootstrap.servers"] = self.bootstrap_servers_var.get()
        self.current_config["client.id"] = self.client_id_var.get()

        # 在新线程中连接Kafka，避免阻塞UI
        threading.Thread(target=self._connect_kafka_thread, daemon=True).start()

    def _connect_kafka_thread(self):
        try:
            self.producer = Producer(self.current_config)

            # 测试连接
            self.producer.produce(
                topic="_connection_test",
                value=b"Connection test",
                callback=self._delivery_report,
            )
            self.producer.poll(0)
            self.producer.flush(10)  # 等待最多10秒

            self.log(
                f"成功连接到Kafka服务器: {self.current_config['bootstrap.servers']}"
            )
            self.log(f"Client ID: {self.current_config['client.id']}")

            # 更新UI状态
            self.root.after(
                0, lambda: messagebox.showinfo("连接成功", "已成功连接到Kafka服务器")
            )
        except Exception as e:
            self.log(f"连接Kafka失败: {str(e)}")
            self.producer = None
            self.root.after(
                0, lambda: messagebox.showerror("连接失败", f"连接Kafka失败: {str(e)}")
            )

    def send_message(self):
        """发送消息到Kafka"""
        if self.producer is None:
            messagebox.showerror("错误", "请先连接到Kafka服务器")
            return

        topic = self.topic_var.get()
        if not topic:
            messagebox.showerror("错误", "请输入Topic")
            return

        message_text = self.message_text.get(1.0, tk.END).strip()
        if not message_text:
            messagebox.showerror("错误", "消息内容不能为空")
            return

        # 解析JSON
        try:
            message_data = json.loads(message_text)
        except json.JSONDecodeError as e:
            messagebox.showerror("JSON解析错误", f"无效的JSON格式: {str(e)}")
            return

        # 在新线程中发送消息，避免阻塞UI
        threading.Thread(
            target=self._send_message_thread, args=(topic, message_data), daemon=True
        ).start()

    def _send_message_thread(self, topic, message_data):
        try:
            # 转换为JSON字符串
            json_data = json.dumps(message_data).encode("utf-8")

            # 发送消息
            self.producer.produce(
                topic=topic, value=json_data, callback=self._delivery_report
            )
            self.producer.poll(0)

            self.log(f"已发送消息到 topic: {topic}")
        except Exception as e:
            self.log(f"发送消息失败: {str(e)}")

    def _delivery_report(self, err, msg):
        """消息传递回调函数"""
        if err is not None:
            self.log(f"消息发送失败: {err}")
        else:
            self.log(
                f"消息已成功发送到 {msg.topic()} [{msg.partition()}]，偏移量: {msg.offset()}"
            )

    def start_continuous_sending(self):
        """开始连续发送消息"""
        if self.producer is None:
            messagebox.showerror("错误", "请先连接到Kafka服务器")
            return

        topic = self.topic_var.get()
        if not topic:
            messagebox.showerror("错误", "请输入Topic")
            return

        message_text = self.message_text.get(1.0, tk.END).strip()
        if not message_text:
            messagebox.showerror("错误", "消息内容不能为空")
            return

        # 解析JSON
        try:
            self.continuous_message_data = json.loads(message_text)
        except json.JSONDecodeError as e:
            messagebox.showerror("JSON解析错误", f"无效的JSON格式: {str(e)}")
            return

        self.continuous_sending = True
        self.log("开始连续发送消息...")

        # 更新按钮状态
        self.continuous_send_button.config(state=tk.DISABLED)
        self.stop_send_button.config(state=tk.NORMAL)

        # 开始连续发送
        self._continuous_send(topic)

    def _continuous_send(self, topic):
        if not self.continuous_sending:
            return

        # 发送消息
        threading.Thread(
            target=self._send_message_thread,
            args=(topic, self.continuous_message_data),
            daemon=True,
        ).start()

        # 1秒后再次发送
        self.root.after(1000, lambda: self._continuous_send(topic))

    def stop_continuous_sending(self):
        """停止连续发送消息"""
        self.continuous_sending = False
        self.log("已停止连续发送消息")

        # 更新按钮状态
        self.continuous_send_button.config(state=tk.NORMAL)
        self.stop_send_button.config(state=tk.DISABLED)

    def log(self, message):
        """添加日志消息"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.log_queue.put(f"[{timestamp}] {message}")

    def start_log_consumer(self):
        """启动日志消费者线程"""
        self.root.after(100, self._process_log_queue)

    def _process_log_queue(self):
        """处理日志队列"""
        while not self.log_queue.empty():
            try:
                message = self.log_queue.get()
                self.log_text.config(state=tk.NORMAL)
                self.log_text.insert(tk.END, message + "\n")
                self.log_text.see(tk.END)
                self.log_text.config(state=tk.DISABLED)
            except queue.Empty:
                pass
        self.root.after(100, self._process_log_queue)


if __name__ == "__main__":
    # 设置样式
    root = tk.Tk()
    style = ttk.Style()

    # 尝试配置主题
    try:
        if "clam" in style.theme_names():
            style.theme_use("clam")
    except:
        pass

    # 自定义样式
    style.configure("TLabel", font=("SimHei", 10))
    style.configure("TButton", font=("SimHei", 10))
    style.configure("TEntry", font=("SimHei", 10))
    style.configure("TFrame", background="#f0f0f0")
    style.configure("TLabelframe", background="#f0f0f0")
    style.configure(
        "TLabelframe.Label", background="#f0f0f0", font=("SimHei", 10, "bold")
    )

    # 创建强调按钮样式
    style.configure("Accent.TButton", foreground="white", background="#4a86e8")

    app = KafkaMessageSenderApp(root)
    root.mainloop()
