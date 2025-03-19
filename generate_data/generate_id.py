import pymysql
import random


def fun():
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
        f"SELECT id, COUNT(*) as count                 FROM hkcy_tag_info_aircraft                 GROUP BY id                 HAVING count > 1 "
    )
    data = cursor.fetchall()
    for row in data:
        id = row[0]
        

if __name__ == "__main__":
    fun()
