import cv2
import ffmpeg
import numpy as np


def extract_frames_from_rtmp(rtmp_url):
    # 使用 ffmpeg 读取 RTMP 流
    process = (
        ffmpeg.input(rtmp_url)
        .output("pipe:", format="rawvideo", pix_fmt="bgr24")
        .run_async(pipe_stdout=True)
    )

    while True:
        # 从 FFmpeg 进程中读取视频数据
        in_bytes = process.stdout.read(640 * 480 * 3)  # 假设分辨率是 640x480 和每帧 RGB
        if not in_bytes:
            break

        # 使用 NumPy 将字节数据转换为数组
        frame = np.frombuffer(in_bytes, np.uint8).reshape((480, 640, 3))

        # 使用 OpenCV 显示视频帧
        cv2.imshow("RTMP Stream", frame)

        # 处理键盘事件，按 'q' 键退出
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # 释放资源
    process.stdout.close()
    process.wait()
    cv2.destroyAllWindows()


# RTMP 流地址
rtmp_url = "rtmp://192.168.1.115/hls/home"
extract_frames_from_rtmp(rtmp_url)
