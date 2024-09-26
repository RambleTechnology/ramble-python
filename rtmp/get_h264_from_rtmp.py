import subprocess


def extract_h264_from_rtmp(rtmp_url, output_file):
    """
    从 RTMP 流中提取 H.264 裸流文件

    :param rtmp_url: RTMP 流的 URL
    :param output_file: 输出的 H.264 文件名
    """
    # ffmpeg 命令
    command = [
        "ffmpeg",
        "-i",
        rtmp_url,  # 输入 RTMP URL
        "-c:v",
        "copy",  # 直接复制视频流，不进行重新编码
        "-an",  # 不处理音频
        "-f",
        "h264",  # 设置输出格式为 H.264
        output_file,  # 输出文件名
    ]

    try:
        # 调用 ffmpeg 命令
        subprocess.run(command, check=True)
        print(f"H.264 stream has been extracted to {output_file}.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    rtmp_url = "rtmp://192.168.1.115:1935/hls/home"  # RTMP 流的 URL
    output_file = "output_fromrtmp.h264"  # 输出文件名
    extract_h264_from_rtmp(rtmp_url, output_file)
