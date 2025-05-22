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
            style="Accent.TButton",
        )
        self.send_button.pack(side=tk.LEFT, padx=5)

        # 隐藏连续发送按钮
        self.continuous_send_button = ttk.Button(
            button_frame,
            text="连续发送",
            command=self.start_continuous_sending,
            width=20,
        )
        self.continuous_send_button.pack(side=tk.LEFT, padx=5)
        self.continuous_send_button.pack_forget()

        self.stop_send_button = ttk.Button(
            button_frame,
            text="停止发送",
            command=self.stop_continuous_sending,
            width=20,
            state=tk.DISABLED,
        )
        self.stop_send_button.pack(side=tk.LEFT, padx=5)
        self.stop_send_button.pack_forget()

        # 日志区域（调整为更大尺寸并支持缩放）
        log_frame = ttk.LabelFrame(main_frame, text="操作日志", padding="10")
        log_frame.pack(fill=tk.BOTH, expand=True, pady=5)

        self.log_text = scrolledtext.ScrolledText(
            log_frame, wrap=tk.WORD, width=80, height=15, font=self.font
        )
        self.log_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.log_text.config(state=tk.DISABLED)

        # 设置权重使界面可伸缩
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)  # 消息内容区域
        main_frame.rowconfigure(3, weight=2)  # 日志区域（权重更大，占用更多空间）

        message_frame.columnconfigure(0, weight=1)
        message_frame.columnconfigure(1, weight=1)
        message_frame.rowconfigure(1, weight=1)

        log_frame.columnconfigure(0, weight=1)
        log_frame.rowconfigure(0, weight=1)

    def generate_example_message(self):
        """生成不含time和timestamp的示例消息"""
        example_data = {
            "sn": "device3",
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
        self.message_text.delete(1.0, tk.END)

    def connect_kafka(self):
        self.log("正在连接Kafka服务器...")
        threading.Thread(target=self._connect_kafka_thread, daemon=True).start()

    def _connect_kafka_thread(self):
        try:
            self.producer = Producer(self.current_config)
            self.producer.produce(
                topic="_connection_test",
                value=b"Connection test",
                callback=self._delivery_report,
            )
            self.producer.poll(0)
            self.producer.flush(10)

            self.log(
                f"成功连接到Kafka服务器: {self.current_config['bootstrap.servers']}"
            )
            self.root.after(0, lambda: messagebox.showinfo("连接成功", "连接完成"))
        except Exception as e:
            self.log(f"连接失败: {str(e)}")
            self.producer = None
            self.root.after(0, lambda: messagebox.showerror("连接失败", str(e)))

    def send_message(self):
        if not self.producer:
            messagebox.showerror("错误", "请先连接Kafka")
            return

        topic = self.topic_var.get().strip()
        if not topic:
            messagebox.showerror("错误", "请输入Topic")
            return

        msg_content = self.message_text.get(1.0, tk.END).strip()
        if not msg_content:
            messagebox.showerror("错误", "消息内容不能为空")
            return

        try:
            msg_data = json.loads(msg_content)
            # 自动生成时间字段（覆盖用户输入）
            beijing_now = datetime.now(timezone(timedelta(hours=8)))
            msg_data["timestamp"] = int(beijing_now.timestamp() * 1000)
            msg_data["time"] = beijing_now.strftime("%Y-%m-%d %H:%M:%S")

            # 打印完整消息内容到日志
            self.log(f"发送到Kafka的完整消息：\n{json.dumps(msg_data, indent=2)}")

            threading.Thread(
                target=self._send_message_thread,
                args=(topic, msg_data),
                daemon=True,
            ).start()

        except json.JSONDecodeError as e:
            messagebox.showerror("JSON错误", f"解析失败: {str(e)}")

    def _send_message_thread(self, topic, msg_data):
        try:
            json_data = json.dumps(msg_data).encode("utf-8")
            self.producer.produce(
                topic=topic, value=json_data, callback=self._delivery_report
            )
            self.producer.poll(0)
            self.log(f"消息已发送到 Topic: {topic}")
        except Exception as e:
            self.log(f"发送失败: {str(e)}")

    def _delivery_report(self, err, msg):
        if err:
            self.log(f"消息发送失败: {err}, 主题: {msg.topic()}")
        else:
            self.log(
                f"消息成功发送到 {msg.topic()}[{msg.partition()}],"
                f" 偏移量: {msg.offset()}, 消息大小: {len(msg.value())}字节"
            )

    # 连续发送功能
    def start_continuous_sending(self):
        if not self.producer:
            messagebox.showerror("错误", "请先连接Kafka")
            return

        topic = self.topic_var.get().strip()
        if not topic:
            messagebox.showerror("错误", "请输入Topic")
            return

        msg_content = self.message_text.get(1.0, tk.END).strip()
        if not msg_content:
            messagebox.showerror("错误", "消息内容不能为空")
            return

        try:
            self.continuous_message_data = json.loads(msg_content)
            self._update_continuous_time()

            self.continuous_sending = True
            self.log("开始连续发送消息（每秒1条）")
            self._continuous_send(topic)

        except json.JSONDecodeError as e:
            messagebox.showerror("JSON错误", f"解析失败: {str(e)}")

    def _update_continuous_time(self):
        """更新连续发送的时间字段"""
        beijing_now = datetime.now(timezone(timedelta(hours=8)))
        self.continuous_message_data["timestamp"] = int(beijing_now.timestamp() * 1000)
        self.continuous_message_data["time"] = beijing_now.strftime("%Y-%m-%d %H:%M:%S")

    def _continuous_send(self, topic):
        if not self.continuous_sending:
            return

        self._update_continuous_time()

        threading.Thread(
            target=self._send_message_thread,
            args=(topic, self.continuous_message_data),
            daemon=True,
        ).start()

        self.root.after(1000, lambda: self._continuous_send(topic))

    def stop_continuous_sending(self):
        self.continuous_sending = False
        self.log("已停止连续发送消息")

    def log(self, message):
        """带时间戳的日志输出"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        self.log_queue.put(f"[{timestamp}] {message}")

    def start_log_consumer(self):
        self.root.after(100, self._process_log_queue)

    def _process_log_queue(self):
        while not self.log_queue.empty():
            try:
                msg = self.log_queue.get()
                self.log_text.config(state=tk.NORMAL)
                self.log_text.insert(tk.END, msg + "\n")
                self.log_text.see(tk.END)
                self.log_text.config(state=tk.DISABLED)
            except queue.Empty:
                pass
        self.root.after(100, self._process_log_queue)


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
