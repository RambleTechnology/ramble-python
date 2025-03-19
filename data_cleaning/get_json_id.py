import json

# 从文件中读取 JSON 数据
with open('济南撒点.json', 'r', encoding='utf-8') as file:
    parsed_data = json.load(file)

# 提取 id 值
id_values = [item['id'] for item in parsed_data['data']]

# 输出结果
print(id_values)
