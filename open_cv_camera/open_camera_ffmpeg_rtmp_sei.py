import cv2
import subprocess
import numpy as np
import time
from datetime import datetime

# FFmpeg RTMP 推送命令
""" 各参数详解：

-y：

允许覆盖输出文件。如果输出文件已经存在，此参数将使 FFmpeg 在处理时直接覆盖而无需提示。
-f rawvideo：

指定输入数据的格式为原始视频流。这意味着输入没有任何编码，用于高效传输视频帧。
-pixel_format rgb24：

指定输入的像素格式为 RGB 24 位。RGB 24 表示每个像素由 3 个字节构成（每个颜色通道 8 位）。
-video_size 640x480：

指定输入视频的分辨率为 640 像素宽和 480 像素高。这是 DVD 和许多在线视频的常见分辨率。
-framerate 25：

指定输入视频的帧率为 25帧每秒。这对于流畅播放视频来说是一个合理的帧率。
-i -：

指定输入来源为标准输入（stdin）。这个符号 "-" 表示 FFmpeg 将从标准输入接收视频数据。通常，与管道结合使用。
-c:v libx264：

指定使用 x264 编码器来压缩视频数据。x264 是一种非常流行且高效的视频编码器，广泛用于生成高质量的 H.264 视频。
-pix_fmt yuv420p：

指定输出视频的像素格式为 YUV 4:2:0，这是一种被广泛支持的视频格式，适用于几乎所有的播放器和流媒体平台。YUV 4:2:0 是一种具有较高压缩效率的格式，能够有效降低视频文件的大小。
-f flv：

指定输出文件的格式为 FLV（Flash Video）。FLV 是一种流媒体文件格式，常用于在线视频流服务。
rtmp://192.168.1.115:1935/live/room-2：

指定输出流的地址，这里是一个 RTMP 流地址，目的是将编码后的视频流发送到指定的 RTMP 服务器。这是用于实时广播和流媒体传输的重要步骤。

"""


# FFmpeg RTMP 推送命令，增加了 -metadata 选项来添加 SEI 信息
cml_data = "888"  # 你的 CML 数据，这里替换为你的内容
sei_payload = f"cml={cml_data}".encode("utf-8")  # 将字符串转换为字节


ffmpeg_command = [
    "ffmpeg",
    "-y",  # 允许覆盖输出文件
    "-f",
    "rawvideo",
    "-pixel_format",
    "rgb24",
    "-video_size",
    "640x480",
    "-framerate",
    "25",
    "-i",
    "-",  # 表示从标准输入读取
    "-c:v",
    "libx264",
    "-pix_fmt",
    "yuv420p",
    "-sei",
    sei_payload.hex(),  # 将 SEI 数据转换为十六进制表示
    "-f",
    "flv",
    "rtmp://192.168.1.115:1935/live/room-2",  # 替换为您的RTMP服务器地址
]

# 启动 FFmpeg 进程
process = subprocess.Popen(ffmpeg_command, stdin=subprocess.PIPE)

# 捕获摄像头
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        # 转换颜色格式 BGR -> RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # 获取当前时间，并放到 sei_payload 中
        #current_time = datetime.now().strftime("%Y%m%d %H:%M:%S:%f")[            :-4        ]  # 获取当前时间并取前3位毫秒
      #  cml_data = current_time  # 将格式化的时间赋值给 cml_data
       # sei_payload = f"cml={cml_data}".encode("utf-8")

        # 将图像数据写入到 FFmpeg 的标准输入
        process.stdin.write(frame.tobytes())

        # 显示摄像头画面
        cv2.imshow("Camera", frame)

        # 按 'q' 键退出
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

# 释放资源
cap.release()
process.stdin.close()
process.wait()
cv2.destroyAllWindows()
