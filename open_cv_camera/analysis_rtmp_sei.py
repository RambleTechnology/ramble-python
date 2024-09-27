import cv2
import subprocess
import numpy as np

# RTMP 地址
rtmp_url = "rtmp://192.168.1.115:1935/live/room-2"

# 使用 FFmpeg 命令获取 RTMP 流，实现从标准输出读取数据
ffmpeg_command = [
    "ffmpeg",
    "-i",
    rtmp_url,  # 输入 RTMP 流
    "-c",
    "copy",  # 直接复制
    "-f",
    "h264",  # 以 H.264 格式输出
    "pipe:1",  # 输出到标准输出
]

# 启动 FFmpeg 进程
process = subprocess.Popen(
    ffmpeg_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE
)

while True:
    # 读取一帧数据
    frame_data = process.stdout.read(188)  # 假设数据每帧为188字节
    if not frame_data:
        break

    # 检查并解析 SEI (在实际实现中需要根据 SEI 帧的格式提取数据)
    # 这里假设 `frame_data` 包含 SEI 帧
    # 你可能需要根据 SEI 结构进行解析，自行添加解析逻辑
    if b"\x06" in frame_data:  # SEI 类型为 6
        print("Found SEI frame!")

        # 解析 SEI 数据
        sei_start = frame_data.find(b"\x06")
        payload_size = frame_data[sei_start + 1]  # 假设第二个字节是有效负载大小
        cml_data_start = sei_start + 2  # 假设 cml_data 在 SEI 头部之后
        cml_data_end = cml_data_start + payload_size  # 根据你存储数据的长度

        # 确保只取有效的字节范围
        if cml_data_end <= len(frame_data):
            cml_data_bytes = frame_data[cml_data_start:cml_data_end]

            try:
                # 尝试解码 cml_data
                cml_data = cml_data_bytes.decode("utf-8")
                print(f"cml_data: {cml_data}")
            except UnicodeDecodeError as e:
                print(f"Decode error: {e}. cml_data bytes: {cml_data_bytes}")
        else:
            print("cml_data range exceeds frame_data length.")

# 释放资源
process.terminate()
process.wait()
