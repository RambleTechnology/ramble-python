import re


# 假设 SRT 文件路径为 "DJI_20250304125509_0001_W.SRT"
srt_file_path = "DJI_20250304125509_0001_W.SRT"

# 打开并读取 SRT 文件
with open(srt_file_path, 'r', encoding='utf-8') as file:
    lines = file.read().split('\n\n')  # 使用空行分割每条字幕

    # 遍历每条字幕条目
    for entry in lines:
        # 将每条字幕条目分割成行
        lines_in_entry = entry.split('\n')
        
        if len(lines_in_entry) >= 5:
            # 第 4 行作为时间
            timestamp = lines_in_entry[3]
            
            # 获取第 5 行内容并检查是否包含 gb_yaw
            fifth_line = lines_in_entry[4]
            print(f"Fifth line content: {fifth_line}")  # 打印出第 5 行的内容，查看其结构
            

            start_index = fifth_line.find("gb_yaw:")  # 找到 "gb_yaw:" 的起始位置
            end_index = fifth_line.find("gb_pitch:")  # 找到 "gb_pitch:" 的起始位置
            
            if start_index != -1 and end_index != -1:
                yaw_string = fifth_line[start_index + len("gb_yaw:"): end_index].strip()  # 取出 gb_yaw 和 gb_pitch 之间的内容，并去除前后空格

                try:
                    gb_yaw = float(yaw_string)
                    print(f"Found gb_yaw: {gb_yaw}")
                except ValueError:
                    print("Error: Unable to convert the value to float.")
            else:
                print("Error: gb_yaw or gb_pitch not found.")
            
     
