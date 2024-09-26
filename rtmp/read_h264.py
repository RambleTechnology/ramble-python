import ffmpeg

def extract_sei_from_h264(input_file, output_file):
    try:
        # 使用 ffmpeg-python 执行命令
        ffmpeg.input(input_file).output(output_file, bsf='h264_metadata=sei=1', format='data').run(capture_stdout=True, capture_stderr=True)
        print(f"SEI data has been extracted to {output_file}.")
    except ffmpeg.Error as e:
        # 输出错误信息
        print(f"An error occurred: {e.stderr.decode() if e.stderr else 'No stderr output'}")

if __name__ == '__main__':
    input_file = 'E:/RedMi_E盘_person/code/Python/ramble-python/rtmp/output_fromrtmp.h264'  # Replace with your H.264 file path
    output_file = 'sei_data.bin'
    extract_sei_from_h264(input_file, output_file)
