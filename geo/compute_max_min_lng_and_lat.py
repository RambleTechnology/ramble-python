import json

# 读取JSON文件
with open('lngAndlat.json', 'r') as f:
    data = json.load(f)

# 初始化最大最小值
max_longitude = float('-inf')
max_latitude = float('-inf')
min_longitude = float('inf')
min_latitude = float('inf')

# 遍历数据中的坐标点
for entry in data:
    # 获取第二项，其中包含了坐标信息
    coordinates = entry[1]
    
    # 遍历所有坐标点
    for coord in coordinates:
        longitude = coord["longitude"]
        latitude = coord["latitude"]
        
        # 更新最大和最小值
        if longitude > max_longitude:
            max_longitude = longitude
        if latitude > max_latitude:
            max_latitude = latitude
        if longitude < min_longitude:
            min_longitude = longitude
        if latitude < min_latitude:
            min_latitude = latitude

# 输出结果
print("最大经度: ", max_longitude)
print("最大纬度: ", max_latitude)
print("最小经度: ", min_longitude)
print("最小纬度: ", min_latitude)
