import mysql.connector
import json
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed


def jg_height():
    # 数据库连接配置
    db_config = {
        "host": "192.168.1.133",  # MySQL主机
        "user": "root",  # MySQL用户名
        "password": "J48Y5zVo1rpo7o25",  # MySQL密码
        "database": "ngh-smart-ar",  # 数据库名称
    }

    # 连接MySQL数据库
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # 查询数据
    query = """
        SELECT id, yswz 
        FROM jg_bh 
        WHERE ysmc='防火道路' 
        AND yswz IS NOT NULL 
        AND yswz != '' 
    """
    cursor.execute(query)

    tip = 1
    # 遍历查询结果
    for id, yswz in cursor.fetchall():
        try:
            # 解析yswz字段的JSON数据
            geo_data = json.loads(yswz)

            # 确保GeoJSON数据符合预期格式
            if geo_data["type"] == "LineString" and "coordinates" in geo_data:
                coords_to_process = []

                # 收集需要获取海拔的坐标
                for coord in geo_data["coordinates"]:
                    if len(coord) == 2:  # 确保每个坐标点只有经纬度
                        coords_to_process.append(coord)

                # 使用多线程获取海拔数据
                elevation_data = get_alititude_height_batch(coords_to_process)

                # 遍历坐标点并增加height和altitudeHeight字段
                for i, coord in enumerate(geo_data["coordinates"]):
                    if len(coord) == 2:  # 确保每个坐标点只有经纬度
                        coord.append(0)  # 添加height
                        # 获取批量海拔数据中的对应海拔
                        ele = elevation_data[i]
                        print(f"根据经纬度计算到的海拔高度为：{ele}")
                        coord.append(ele)  # 添加altitudeHeight

                # 将修改后的数据转换为JSON字符串
                updated_yswz = json.dumps(geo_data)

                # 更新数据库中的yswz字段
                update_query = "UPDATE jg_bh SET yswz = %s WHERE id = %s"
                cursor.execute(update_query, (updated_yswz, id))
                conn.commit()
                print(f"Updated yswz for id {id}")
                print(f"当前处理的第{tip}条数据。。。")
                tip = tip + 1

        except (json.JSONDecodeError, KeyError) as e:
            print(f"Error processing yswz for id {id}: {e}")

    # 关闭数据库连接
    cursor.close()
    conn.close()


def get_alititude_height_batch(coords):
    """
    批量获取多个坐标点的海拔数据
    :param coords: 坐标列表，格式为 [[lng1, lat1], [lng2, lat2], ...]
    :return: 海拔高度的列表
    """
    # 定义 API URL
    url = "https://api.open-elevation.com/api/v1/lookup"

    # 构建请求体参数，最多可一次性请求50个坐标
    data = {"locations": [{"latitude": lat, "longitude": lng} for lng, lat in coords]}

    # 发送 POST 请求
    response = requests.post(url, json=data)

    # 检查请求是否成功
    if response.status_code == 200:
        # 解析 JSON 响应
        response_data = response.json()

        # 提取 elevation 值
        if "results" in response_data and len(response_data["results"]) == len(coords):
            elevation = [result["elevation"] for result in response_data["results"]]
            return elevation
        else:
            print("No results found or mismatch in number of results.")
    else:
        print(f"Request failed with status code: {response.status_code}")

    return [0] * len(coords)  # 如果请求失败，返回默认值


if __name__ == "__main__":
    jg_height()
