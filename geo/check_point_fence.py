from shapely.geometry import Point, Polygon

def is_point_in_fence(lng_lat, fence):
    # 转换输入点和电子围栏为 Shapely 对象
    point = Point(lng_lat[0], lng_lat[1])
    
    # 将电子围栏转换为多边形
    polygon_coords = [(coord['lng'], coord['lat']) for coord in fence[0]]
    polygon = Polygon(polygon_coords)
    
    # 检查点是否在多边形内
    return polygon.contains(point)

# 示例用法 ， 基于84坐标系
point = (121.41953920109717, 31.25054935054596)
fence = [[{"lng":121.3568217,"lat":31.2597675},{"lng":121.35764799,"lat":31.259451},{"lng":121.35749046,"lat":31.25920104},{"lng":121.35737185,"lat":31.25924126},{"lng":121.35712913,"lat":31.25876298},{"lng":121.35618518,"lat":31.25918669},{"lng":121.35618509,"lat":31.25928166},{"lng":121.3568217,"lat":31.2597675}]]

print(is_point_in_fence(point, fence))  # 输出: True 或 False
