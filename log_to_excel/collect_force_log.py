def read_log_and_filter(filename):
    """
    读取指定的日志文件，返回包含 'AircraftConsumer_Received_message' 关键字的所有行，去重。
    :param filename: 日志文件路径
    :return: 包含匹配行的集合
    """
    matched_lines = set()

    try:
        # 打开并读取日志文件
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                if "AircraftConsumer_Received_message" in line:
                    matched_lines.add(line.strip())  # 去除每行末尾的换行符

        # 将匹配的内容写入到输出文件
        output_filename = "C:\\Users\\cml\\Desktop\\1228飞行数据\\log_filter_result.log"
        with open(output_filename, "w", encoding="utf-8") as output_file:
            for line in matched_lines:
                output_file.write(line + "\n")  # 每行结束后加上换行符
    except FileNotFoundError:
        print(f"错误：文件 {filename} 未找到！")
    except Exception as e:
        print(f"读取文件时发生错误: {e}")

    return matched_lines


def main():
    log_filename = "C:\\Users\\cml\\Desktop\\1228飞行数据\\ngh-aircraft-2024-12-28.0log(2024-12-28T132929至2024-12-28T133758).log"  # 替换为实际的日志文件路径
    result = read_log_and_filter(log_filename)

    if result:
        print(f"匹配到 {len(result)} 行包含 'AircraftConsumer_Received_message':")
        for line in result:
            print(line)
    else:
        print("未找到匹配的行。")


if __name__ == "__main__":
    main()
