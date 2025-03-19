import json
import pymysql
from sqlalchemy import create_engine
import pandas as pd
import math
import requests
import uuid



def get_region_id(latitude, longitude, biz_id, token):
    """
    调用接口并获取 regionId

    :param latitude: 纬度
    :param longitude: 经度
    :param biz_id: 业务ID
    :param token: 身份认证token
    :return: 返回 regionId（如果存在），否则返回 None
    """
    # 定义接口 URL
    url = "http://192.168.1.92:8088/bams/disposeRegion/dispose/aIjjC7b8YqqCbpaqpHI4ZtVbv"

    # 构建请求头
    headers = {
        "token":token,
        "Content-Type": "application/json"
    }

    # 构建请求体
    payload = {
        "latitude": latitude,
        "longitude": longitude,
        "bizId": biz_id
    }

    # 发送 POST 请求
    try:
        response = requests.post(url, json=payload, headers=headers)

        # 检查响应状态码
        if response.status_code == 200:
            # 解析返回的 JSON 数据
            response_data = response.json()

            # 提取 regionId
            if "regions" in response_data and len(response_data["regions"]) > 0:
                return response_data["regions"][0]["regionId"]
            else:
                print("No regions found in the response.")
                return None
        else:
            print(f"Request failed with status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None





# 常量
x_pi = 3.14159265358979324 * 3000.0 / 180.0
pi = 3.1415926535897932384626  # π
a = 6378245.0  # 长半轴
ee = 0.00669342162296594323  # 偏心率平方


def gcj02_to_bd09(lng, lat):
    """
    火星坐标系(GCJ-02)转百度坐标系(BD-09)
    谷歌、高德——>百度
    :param lng:火星坐标经度
    :param lat:火星坐标纬度
    :return:
    """
    z = math.sqrt(lng * lng + lat * lat) + 0.00002 * math.sin(lat * x_pi)
    theta = math.atan2(lat, lng) + 0.000003 * math.cos(lng * x_pi)
    bd_lng = z * math.cos(theta) + 0.0065
    bd_lat = z * math.sin(theta) + 0.006
    return [bd_lng, bd_lat]


def wgs84_to_gcj02(lng, lat):
    """
    WGS84转GCJ02(火星坐标系)
    :param lng:WGS84坐标系的经度
    :param lat:WGS84坐标系的纬度
    :return:
    """
    if out_of_china(lng, lat):  # 判断是否在国内
        return [lng, lat]
    dlat = _transformlat(lng - 105.0, lat - 35.0)
    dlng = _transformlng(lng - 105.0, lat - 35.0)
    radlat = lat / 180.0 * pi
    magic = math.sin(radlat)
    magic = 1 - ee * magic * magic
    sqrtmagic = math.sqrt(magic)
    dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * pi)
    dlng = (dlng * 180.0) / (a / sqrtmagic * math.cos(radlat) * pi)
    mglat = lat + dlat
    mglng = lng + dlng
    return [mglng, mglat]


def wgs84_to_bd09(lon, lat):
    lon, lat = wgs84_to_gcj02(lon, lat)
    return gcj02_to_bd09(lon, lat)


def out_of_china(lng, lat):
    """
    判断是否在国内，不在国内不做偏移
    :param lng:
    :param lat:
    :return:
    """
    return not (lng > 73.66 and lng < 135.05 and lat > 3.86 and lat < 53.55)


def _transformlng(lng, lat):
    ret = (
        300.0
        + lng
        + 2.0 * lat
        + 0.1 * lng * lng
        + 0.1 * lng * lat
        + 0.1 * math.sqrt(math.fabs(lng))
    )
    ret += (
        (20.0 * math.sin(6.0 * lng * pi) + 20.0 * math.sin(2.0 * lng * pi)) * 2.0 / 3.0
    )
    ret += (20.0 * math.sin(lng * pi) + 40.0 * math.sin(lng / 3.0 * pi)) * 2.0 / 3.0
    ret += (
        (150.0 * math.sin(lng / 12.0 * pi) + 300.0 * math.sin(lng / 30.0 * pi))
        * 2.0
        / 3.0
    )
    return ret


def _transformlat(lng, lat):
    ret = (
        -100.0
        + 2.0 * lng
        + 3.0 * lat
        + 0.2 * lat * lat
        + 0.1 * lng * lat
        + 0.2 * math.sqrt(math.fabs(lng))
    )
    ret += (
        (20.0 * math.sin(6.0 * lng * pi) + 20.0 * math.sin(2.0 * lng * pi)) * 2.0 / 3.0
    )
    ret += (20.0 * math.sin(lat * pi) + 40.0 * math.sin(lat / 3.0 * pi)) * 2.0 / 3.0
    ret += (
        (160.0 * math.sin(lat / 12.0 * pi) + 320 * math.sin(lat * pi / 30.0))
        * 2.0
        / 3.0
    )
    return ret


# 数据库连接信息
mysql_config = {
    "host": "192.168.1.92",
    "port": 3306,
    "user": "root",
    "password": "J48Y5zVo1rpo7o25",
    "database": "ngh-smart-ar",
}

starrocks_config = {
    "host": "192.168.1.82",
    "port": 9030,
    "user": "root",
    "password": "",
    "database": "ngh_smart_ar",
}


# 读取 JSON 文件
def read_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


# 将数据插入 MySQL
def insert_into_mysql(data, label_type_logic_id):
    connection = pymysql.connect(**mysql_config)
    cursor = connection.cursor()

    insert_query = """
    INSERT INTO hkcy_tag_info (tag_logic_id, tagname, longitude, latitude , longandlat , has_del, hik_status , hik_msg , org_id , label_type_logic_id , auth_field_1)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s , %s, %s)
    """

    for item in data["data"]:
  
        lon_wgs84 = float(item["longitude"])
        lat_wgs84 = float(item["latitude"])

        # 调用 WGS84 到 BD-09 的转换函数
        bd_lon, bd_lat = wgs84_to_bd09(lon_wgs84, lat_wgs84)

        print(f"WGS84 坐标: ({lon_wgs84}, {lat_wgs84})")
        print(f"转换后的 BD-09 坐标: ({bd_lon}, {bd_lat})")

        biz_id = str(uuid.uuid4())
        token = "d5abbb11-61fc-445e-bce2-9a567b19e580"
        region_id = get_region_id(bd_lat, bd_lon, biz_id, token)
        if region_id is None :
            region_id="001037006"

        cursor.execute(
            insert_query,
            (
                item["id"],
                item["name"],
                # float(item["longitude"]),
                # float(item["latitude"]),
                bd_lon,
                bd_lat,
                str(bd_lon) + "," + str(bd_lat),
                0,  # 假设 has_del 默认是 0
                0,  # 假设 hik_status 默认是 0
                "未上图",
                "aIjjC7b8YqqCbpaqpHI4ZtVbv",
                label_type_logic_id,
                region_id,
            ),
        )

    connection.commit()
    cursor.close()
    connection.close()


# 将数据插入 StarRocks
def insert_into_starrocks(data, label_type_logic_id):
    connection = pymysql.connect(**starrocks_config)
    cursor = connection.cursor()

    insert_query = """
    INSERT INTO hkcy_tag_info (tag_logic_id, tagname, longitude, latitude , longandlat ,  hik_status , hik_msg , org_id , label_type_logic_id , auth_field_1)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s , %s)
    """

    for item in data["data"]:
        
        lon_wgs84 = float(item["longitude"])
        lat_wgs84 = float(item["latitude"])

        # 调用 WGS84 到 BD-09 的转换函数
        bd_lon, bd_lat = wgs84_to_bd09(lon_wgs84, lat_wgs84)

        print(f"WGS84 坐标: ({lon_wgs84}, {lat_wgs84})")
        print(f"转换后的 BD-09 坐标: ({bd_lon}, {bd_lat})")


        # 示例调用

        biz_id = str(uuid.uuid4())
        token = "d5abbb11-61fc-445e-bce2-9a567b19e580"
        region_id = get_region_id(bd_lat, bd_lon, biz_id, token)
        if region_id is None :
            region_id="001037006"
        cursor.execute(
            insert_query,
            (
                item["id"],
                item["name"],
                # float(item["longitude"]),
                # float(item["latitude"]),
                # item["longitude"] + "," + item["latitude"],
                bd_lon,
                bd_lat,
                str(bd_lon) + "," + str(bd_lat),            
                0,  # 假设 hik_status 默认是 0
                "未上图",
                "aIjjC7b8YqqCbpaqpHI4ZtVbv",
                label_type_logic_id,
                region_id,
            ),
        )

    connection.commit()
    cursor.close()
    connection.close()


# 将数据插入 MySQL
def insert_into_mysql_with_jinan(data, label_type_logic_id):
    connection = pymysql.connect(**mysql_config)
    cursor = connection.cursor()

    insert_query = """
    INSERT INTO hkcy_tag_info (tag_logic_id, tagname, longitude, latitude , longandlat , has_del, hik_status , hik_msg , org_id , label_type_logic_id , auth_field_1)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s , %s, %s)
    """

    for item in data["data"]:
        lon_wgs84 = float(item["longitude"])
        lat_wgs84 = float(item["latitude"])

        # 调用 WGS84 到 BD-09 的转换函数
        bd_lon, bd_lat = wgs84_to_bd09(lon_wgs84, lat_wgs84)

        print(f"WGS84 坐标: ({lon_wgs84}, {lat_wgs84})")
        print(f"转换后的 BD-09 坐标: ({bd_lon}, {bd_lat})")

        biz_id = str(uuid.uuid4())
        token = "d5abbb11-61fc-445e-bce2-9a567b19e580"
        region_id = get_region_id(bd_lat, bd_lon, biz_id, token)
        if region_id is None :
            region_id="001037006"

        cursor.execute(
            insert_query,
            (
                item["id"],
                item["name"],
                bd_lon,
                bd_lat,
                str(bd_lon) + "," + str(bd_lat),
                0,  # 假设 has_del 默认是 0
                0,  # 假设 hik_status 默认是 0
                "未上图",
                "aIjjC7b8YqqCbpaqpHI4ZtVbv",
                label_type_logic_id,
                item["regionId"],
            ),
        )

    connection.commit()
    cursor.close()
    connection.close()


# 将数据插入 StarRocks
def insert_into_starrocks_with_jinan(data, label_type_logic_id):
    connection = pymysql.connect(**starrocks_config)
    cursor = connection.cursor()

    insert_query = """
    INSERT INTO hkcy_tag_info (tag_logic_id, tagname, longitude, latitude , longandlat ,  hik_status , hik_msg , org_id , label_type_logic_id , auth_field_1)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s , %s)
    """

    for item in data["data"]:
        lon_wgs84 = float(item["longitude"])
        lat_wgs84 = float(item["latitude"])

        # 调用 WGS84 到 BD-09 的转换函数
        bd_lon, bd_lat = wgs84_to_bd09(lon_wgs84, lat_wgs84)

        print(f"WGS84 坐标: ({lon_wgs84}, {lat_wgs84})")
        print(f"转换后的 BD-09 坐标: ({bd_lon}, {bd_lat})")

        biz_id = str(uuid.uuid4())
        token = "d5abbb11-61fc-445e-bce2-9a567b19e580"
        region_id = get_region_id(bd_lat, bd_lon, biz_id, token)
        if region_id is None :
            region_id="001037006"
        cursor.execute(
            insert_query,
            (
                item["id"],
                item["name"],
                bd_lon,
                bd_lat,
                str(bd_lon) + "," + str(bd_lat),
                0,  # 假设 hik_status 默认是 0
                "未上图",
                "aIjjC7b8YqqCbpaqpHI4ZtVbv",
                label_type_logic_id,
                item["regionId"],
            ),
        )

    connection.commit()
    cursor.close()
    connection.close()


# 主程序
if __name__ == "__main__":

    # 文化休闲/风景名胜/其他旅游景点
    label_type_logic_id_lvyou = "001915013012"

    # json_file_path = "烟台区景区撒点.json"  # 替换为你的 JSON 文件路径
    # json_data = read_json(json_file_path)

    # insert_into_mysql(json_data, label_type_logic_id_lvyou)
    # insert_into_starrocks(json_data, label_type_logic_id_lvyou)

    json_file_path = "济南撒点.json"  # 替换为你的 JSON 文件路径
    json_data = read_json(json_file_path)

    insert_into_mysql_with_jinan(json_data, label_type_logic_id_lvyou)
    insert_into_starrocks_with_jinan(json_data, label_type_logic_id_lvyou)
