import redis
import json

# Redis连接配置
r = redis.Redis(
    host='192.168.1.132',
    port=6379,
    password='ZAQ!xsw2',
    decode_responses=True
)

# 扫描前缀key并获取数据
keys = []
cursor = 0
while True:
    cursor, partial_keys = r.scan(cursor, match='login_tokens*', count=1000)
    keys.extend(partial_keys)
    if cursor == 0:
        break

# 批量获取value并解析为JSON对象
data = {}
if keys:
    values = r.mget(keys)
    for key, value in zip(keys, values):
        try:
            # 先去除可能的外层引号，再解析JSON
            clean_value = value.strip('"') if value else value
            data[key] = json.loads(clean_value) if clean_value else None
        except (json.JSONDecodeError, TypeError):
            # 解析失败则保留原始字符串
            data[key] = value

# 保存为格式化的JSON文件
with open('redis_login_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f'已保存 {len(data)} 条数据到 redis_login_data.json')