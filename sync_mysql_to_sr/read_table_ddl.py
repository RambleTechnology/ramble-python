import pandas as pd
import pymysql
import uuid  # 导入uuid模块


def read_ddl():
    # 建立数据库连接
    connection = pymysql.connect(
        host="192.168.1.92",
        user="root",
        password="J48Y5zVo1rpo7o25",
        port=3306,
        database="ngh-smart-ar",
    )

    # 创建游标对象
    cursor = connection.cursor()
    # 获取所有表的列表
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()

    # 获取每个表的 DDL
    for table in tables:
        table_name = table[0]
        cursor.execute(f"SHOW CREATE TABLE {table_name}")
        create_table_ddl = cursor.fetchone()
        print(f"Table: {table_name}")
        print(create_table_ddl[1])  # DDL 语句
        print("\n" + "=" * 50 + "\n")


if __name__ == "__main__":
    read_ddl()
