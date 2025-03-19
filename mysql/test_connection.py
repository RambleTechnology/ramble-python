# -*- coding: utf-8 -*-

import pymysql

# 数据库连接配置
db_config = {
    # "host": "192.168.1.92",  # 替换为你的数据库地址
    "host": "127.0.0.1",
    "user": "root",  # 替换为你的数据库用户名
    "password": "J48Y5zVo1rpo7o25",  # 替换为你的数据库密码
    "database": "cml",  # 替换为你的数据库名称
}

# 连接数据库
connection = pymysql.connect(**db_config)
cursor = connection.cursor()

try:
    # 查询 bams_dept 表中 dept_name 为 '万州区' 的数据
    cursor.execute("SELECT VERSION()")
    result = cursor.fetchall()

    # 如果查询到数据
    if result:
        print("result=%s", result)
    else:
        print("No departments found")

except pymysql.MySQLError as e:
    print("Error occurred: %s",e)
    connection.rollback()

finally:
    cursor.close()
    connection.close()
