import re

def extract_message_from_log(input_filename, output_filename):
    """
    从日志文件中提取 'AircraftConsumer_Received_message:' 后面的 JSON 部分，并保存到另一个文件。
    :param input_filename: 输入日志文件的路径
    :param output_filename: 输出文件路径，用于存储提取出的消息
    """
    # 正则表达式，用于匹配 'AircraftConsumer_Received_message:' 后面的 JSON 字符串
    pattern = r'AircraftConsumer_Received_message:\s*(\{.*\})'

    try:
        with open(input_filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        matched_messages = []
        for line in lines:
            # 使用正则表达式查找匹配项
            match = re.search(pattern, line)
            if match:
                matched_messages.append(match.group(1))  # 提取并保存 JSON 部分

        # 将匹配到的所有 JSON 数据写入输出文件
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            for message in matched_messages:
                output_file.write(message + '\n')

        print(f"提取的消息已保存到 {output_filename}")

    except FileNotFoundError:
        print(f"错误：文件 {input_filename} 未找到！")
    except Exception as e:
        print(f"处理文件时发生错误: {e}")


# 示例调用
input_filename = 'log_filter_result.log'  # 输入日志文件路径
output_filename = 'log_to_json.json'  # 输出文件路径
extract_message_from_log(input_filename, output_filename)
