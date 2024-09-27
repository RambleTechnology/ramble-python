import cv2
import subprocess
import time

# 摄像头设备索引
camera_index = 0  # 如果有多个摄像头，请相应调整
# RTMP 流地址
rtmp_url = "rtmp://192.168.1.115:1935/live/room-2"

# FFmpeg 命令构建
ffmpeg_cmd = [
    'ffmpeg',
    '-y',  # 覆盖输出文件
    '-f', 'rawvideo',  # 输入格式
    '-pixel_format', 'bgr24',  # 输入的像素格式
    '-video_size', '640x480',  # 视频分辨率
    '-framerate', '30',  # 帧率
    '-i', '-',  # 从标准输入读取
    '-f', 'flv',  # 输出格式
    '-metadata:s:v', 'comment=cml=666',  # 添加 SEI 帧
    rtmp_url  # 输出 RTMP 流地址
]

# 启动 FFmpeg 进程
ffmpeg_process = subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE)

# 打开摄像头
cap = cv2.VideoCapture(camera_index)

if not cap.isOpened():
    print("Error: Unable to access the camera.")
    exit()

try:
    while True:
        # 捕获视频帧
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to read frame.")
            break
        
        # 将帧写入 FFmpeg 的标准输入
        ffmpeg_process.stdin.write(frame.tobytes())
        
        # 显示捕获的视频
        cv2.imshow('Camera', frame)

        # 按 'q' 键退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
except KeyboardInterrupt:
    print("Stream stopped by user.")
finally:
    cap.release()
    cv2.destroyAllWindows()
    ffmpeg_process.stdin.close()
    ffmpeg_process.wait()
