import subprocess
import numpy as np
import cv2
import json
import time

# 设置 RTMP URL
rtmp_url = "rtmp://192.168.1.115:1935/live/room-3"


# 生成一个示例视频流（640x480，30fps），可以替换为实际的视频输入
def generate_video_stream():
    width, height, fps = 640, 480, 30
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter("output.avi", fourcc, fps, (width, height))

    # 生成一些示例帧
    for _ in range(fps * 100):  # 10秒
        frame = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
        out.write(frame)

    out.release()


# 生成视频流
generate_video_stream()

# FFmpeg 命令
ffmpeg_cmd = [
    "ffmpeg",
    "-y",  # 覆盖输出文件
    "-i",
    "output.avi",  # 输入文件
    "-c:v",
    "libx264",  # 使用 H.264 编码
    "-x264-params",
    "sei=1",  # 添加 SEI 数据
    "-f",
    "flv",  # 输出格式
    rtmp_url,  # 输出 RTMP URL
]

# 启动 FFmpeg 进程
ffmpeg_process = subprocess.Popen(ffmpeg_cmd)

# 等待一些时间以确保流开始
time.sleep(5)


# 解析 SEI 数据
def extract_sei_data(stream_url):
    # 使用 ffprobe 提取视频流信息，包括 SEI 数据
    command = [
        "ffprobe",
        "-show_frames",
        "-select_streams",
        "v:0",
        "-show_entries",
        "frame=pkt_pts_time,side_data_list",
        "-of",
        "json",
        stream_url,
    ]

    result = subprocess.run(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )

    if result.returncode != 0:
        print("Error running ffprobe:", result.stderr)
        return []

    # 解析输出 JSON
    frames_info = json.loads(result.stdout)

    sei_data = []

    # 遍历所有帧，提取 SEI 数据
    for frame in frames_info.get("frames", []):
        side_data = frame.get("side_data_list", [])
        for data in side_data:
            if "type" in data and data["type"] == "SEI":
                sei_data.append(
                    {
                        "pts_time": frame["pkt_pts_time"],
                        "sei_data": data.get("data", "N/A"),
                    }
                )

    return sei_data


# 提取 SEI 数据
# 确保 rtsp_url 是正确的并能访问
sei_data = extract_sei_data(rtmp_url)

# 输出 SEI 数据
if sei_data:
    for entry in sei_data:
        print(f"PTS Time: {entry['pts_time']} seconds, SEI Data: {entry['sei_data']}")
else:
    print("没有找到 SEI 数据。")

# 结束 FFmpeg 进程
ffmpeg_process.terminate()
