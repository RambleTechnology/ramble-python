import pymysql
import time
import random
from datetime import datetime


def etl_v2():
    # 建立数据库连接
    connection = pymysql.connect(
        host="192.168.1.115",
        user="root",
        password="J48Y5zVo1rpo7o25",
        port=3306,
        database="ngh-smart-ar",
    )

    # 创建游标对象
    cursor = connection.cursor()
    cursor.execute(
        f"SELECT id ,  longitude , latitude  from `hkcy_tag_info_aircraft` order by id limit 40000 ,10000 "
    )
    data = cursor.fetchall()
    for row in data:
        # print(f"老的经纬度{row}")
        id = row[0]
        print(id)
        lon = row[1] + random.uniform(-0.09, 0.09)
        lat = row[2] + random.uniform(-0.09, 0.09)
        # print(f"新的经纬度{lon} , {lat}")
        lonlat = str(lon) + "," + str(lat)
        # print(lonlat)
        update = f"update hkcy_tag_info_aircraft set longitude ={lon}   , latitude  = {lat}  , longandlat = '{lonlat}'  where id = {id} "
        cursor.execute(update)
        
    connection.commit()
    

if __name__ == "__main__":
    etl_v2()
