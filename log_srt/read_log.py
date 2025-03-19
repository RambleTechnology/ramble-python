import re

# 假设log文件路径为"log_file.log"
log_file_path = "osd.txt"

# 定义一个正则表达式来提取时间和head值


log_pattern = re.compile(r'"head":(-?[\d.]+).*?"time":"([^"]+)"')

# 打开并逐行读取日志文件，指定编码为utf-8
with open(log_file_path, 'r', encoding='utf-8') as file:
    for line in file:
        # 打印当前处理的行（用于调试）
        print(f"Processing line: {line.strip()}")  
        
        # 查找匹配
        match = log_pattern.search(line)
        if match:
            head = match.group(1)  # 提取时间
            time = match.group(2)  # 提取head值
            print(f"head: {time}, time: {head}")
        else:
            print("No match found in this line.")  # 如果没有匹配，输出提示
