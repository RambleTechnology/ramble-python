import av


def check_sei_frames(rtmp_url):
    try:
        # 打开 RTMP 流
        container = av.open(rtmp_url)

        sei_found = False

        # 遍历每个视频流
        for stream in container.streams:
            if stream.type == "video":
                for packet in container.demux(stream):
                    # 遍历每个包，检查数据
                    for frame in packet.decode():
                        # 检查 NAL 单元
                        for nal_unit in frame.to_ndarray():  # 转换为 NumPy 数组
                            # 检查 NAL 单元的类型
                            if nal_unit[0] & 0x1F == 6:  # SEI NAL 单元的类型是 6
                                print("Found SEI frame")
                                sei_found = True
                                # 打印 SEI 数据
                                sei_data = nal_unit[
                                    1:
                                ]  # 取出 SEI 数据，通常在第一个字节后
                                # 尝试将 SEI 数据解码为字符串
                                try:
                                    # 将 NumPy 数组转换为字节串
                                    sei_bytes = bytes(sei_data)
                                    sei_string = sei_bytes.decode(
                                        "utf-8", errors="ignore"
                                    )  # 尝试使用 UTF-8 解码
                                    print(f"SEI Data (String): {sei_string}")
                                except Exception as decode_error:
                                    print(f"Error decoding SEI data: {decode_error}")

        if not sei_found:
            print("No SEI frames found in the stream.")

    except Exception as e:
        print(f"An error occurred: {e}")


# 示例 RTMP 流 URL
rtmp_url = "rtmp://192.168.1.115:1935/live/room-2"
check_sei_frames(rtmp_url)
