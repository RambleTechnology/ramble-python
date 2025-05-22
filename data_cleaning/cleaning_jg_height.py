import mysql.connector
import json

import requests


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
                # 遍历坐标点并增加height和altitudeHeight字段
                for coord in geo_data["coordinates"]:
                    if len(coord) == 2:  # 确保每个坐标点只有经纬度
                        coord.append(0)  # 添加height
                        ele = get_alititude_height(coord[0], coord[1])
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


def get_alititude_height(lng, lat):

    # 定义 API URL
    url = "https://api.open-elevation.com/api/v1/lookup"

    # 定义请求体参数
    data = {"locations": [{"latitude": lat, "longitude": lng}]}

    # 发送 POST 请求
    response = requests.post(url, json=data)

    # 检查请求是否成功
    if response.status_code == 200:
        # 解析 JSON 响应
        response_data = response.json()

        # 提取 elevation 值
        if "results" in response_data and len(response_data["results"]) > 0:
            elevation = response_data["results"][0]["elevation"]
            print(f"Elevation: {elevation} meters")
            return elevation
        else:
            print("No results found in the response.")
    else:
        print(f"Request failed with status code: {response.status_code}")
    return 0


if __name__ == "__main__":
    jg_height()
