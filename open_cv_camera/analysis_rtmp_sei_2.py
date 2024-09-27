import subprocess
import re

# RTMP 流地址
rtmp_url = "rtmp://192.168.1.115:1935/live/room-2"

# FFmpeg 命令构建
ffmpeg_cmd = [
    'ffmpeg',
    '-i', rtmp_url,  # 输入 RTMP 流
    '-c:v', 'libx264',  # 使用 H.264 编码器
    '-f', 'h264',  # 输出格式为 H.264
    'pipe:1'  # 输出到标准输出
]

# 启动 FFmpeg 进程
ffmpeg_process = subprocess.Popen(ffmpeg_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# 存储 SEI 帧的函数
def parse_sei(data):
    # 查找 SEI 帧中的 cml 信息
    # H.264 SEI 帧格式以 0x06 开头
    sei_pattern = re.compile(b'\x00\x00\x00\x01\x06.*?cml=666', re.DOTALL)
    matches = sei_pattern.findall(data)
    return matches

try:
    buffer = b''
    while True:
        # 读取 FFmpeg 的标准输出流
        data = ffmpeg_process.stdout.read(4096)
        if not data:
            break
        
        # 将数据缓冲到一个字符串中，直到检测到完整的 SEI 帧
        buffer += data
        
        # 尝试解析 SEI 帧
        sei_matches = parse_sei(buffer)
        
        # 输出匹配的内容
        for match in sei_matches:
            print("SEI Frame detected: ", match)
            # 从缓冲区中移除已处理的数据
            buffer = buffer[buffer.find(match) + len(match):]

except KeyboardInterrupt:
    print("Stream stopped by user.")
finally:
    ffmpeg_process.stdout.close()
    ffmpeg_process.stderr.close()
    ffmpeg_process.wait()
