import re
from datetime import datetime


# 解析log文件中的时间和head值
def parse_log_file(log_file):
    log_data = []
    log_pattern = re.compile(r'"head":(-?[\d.]+).*?"time":"([^"]+)"')
    with open(log_file, "r", encoding="utf-8") as file:
        for line in file:
            # print(f"Processing line: {line.strip()}")
            match = log_pattern.search(line)
            if match:
                time = match.group(2)  
                head = match.group(1)  
                try:
                    yaw=float(head)
                    # print(f"head: {time}, time: {head}")
                    log_data.append((time, yaw))
                except ValueError:
                        print("Error: Unable to convert the head to float.")
                
            else:
                print("No match found in this line.")
    return log_data


# 解析srt文件中的时间和gb_yaw值
def parse_srt_file(srt_file):
    srt_data = []
    with open(srt_file, "r", encoding="utf-8") as file:
        lines = file.read().split("\n\n")
        for entry in lines:
            lines_in_entry = entry.split("\n")
            if len(lines_in_entry) >= 5:
                time = lines_in_entry[3]
                fifth_line = lines_in_entry[4]
                # print(f"Fifth line content: {fifth_line}")
                start_index = fifth_line.find("gb_yaw:")
                end_index = fifth_line.find("gb_pitch:")
                if start_index != -1 and end_index != -1:
                    yaw_string = fifth_line[
                        start_index + len("gb_yaw:") : end_index
                    ].strip()
                    try:
                        gb_yaw = float(yaw_string)
                        # print(f"Found gb_yaw: {gb_yaw}")
                        srt_data.append((time, gb_yaw))
                    except ValueError:
                        print("Error: Unable to convert the value to float.")
                else:
                    print("Error: gb_yaw or gb_pitch not found.")
    return srt_data


# 匹配log和srt中的时间数据
def match_data(log_data, srt_data, time_diff_threshold=5):
    matches = []
    for log_time, head in log_data:
        for srt_time, gb_yaw in srt_data:
            # 计算时间差，单位为秒
            time_diff = abs((log_time - srt_time).total_seconds())
            if time_diff <= time_diff_threshold:
                matches.append((log_time, head, gb_yaw, time_diff))
    return matches


# 打印匹配结果
def print_matches(matches):
    for match in matches:
        log_time, head, gb_yaw, time_diff = match
        print(
            f"Time: {log_time}, head: {head}, gb_yaw: {gb_yaw}, Time Difference: {time_diff} seconds"
        )


def main(log_file, srt_file):
    log_data = parse_log_file(log_file)
    print(f"log的第一个元素:{log_data[0]}")
    srt_data = parse_srt_file(srt_file)
    print(f"srt的第一个元素:{srt_data[0]}")

    matches = match_data(log_data, srt_data)
    print_matches(matches)


# 文件路径
log_file = "osd.txt" 
srt_file = "DJI_20250304125509_0001_W.srt" 

main(log_file, srt_file)
