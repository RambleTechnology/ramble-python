import pandas as pd
import pymysql
import uuid
import requests
import http.client
import json
from pypinyin import lazy_pinyin



def find_parent_value(target_value):
    """
    从给定的 JSON 文件中查找指定区域的父级值。

    :param file_name: JSON 文件的路径
    :param target_value: 要查找的区域值
    :return: 找到的父级值，如果未找到则返回 None
    """
    file_name = "省市区.json"
    found_parent_value = None

    with open(file_name, "r", encoding="utf-8") as file:
        data = json.load(file)  # 读取 JSON 数据

        for city in data["city"]:
            for area in city["area"]:
                if area["value"] == target_value:
                    found_parent_value = city["value"]  # 找到父级 value
                    break  # 找到后退出区域循环
            if found_parent_value:  # 如果已经找到父级，退出城市循环
                break

    return found_parent_value




def etl_region():
    # 建立数据库连接
    connection = pymysql.connect(
        host="192.168.1.115",
        user="root",
        password="J48Y5zVo1rpo7o25",
        port=3306,
        database="shan-dong-jiashicang",
    )

    # 创建游标对象
    cursor = connection.cursor()

    # 读取Excel文件
    file_path = "区域.xlsx"  # 替换为你的Excel文件路径
    data = pd.read_excel(file_path)

    # 创建MySQL连接
    try:
        # 插入数据到gov_region表
        for index, row in data.iterrows():
            code = row[0]  # 区域编码
            name = row[1]  # 区域名称
            print(name)

            # 检查数据是否已存在
            cursor.execute("SELECT COUNT(*) FROM szzf_region WHERE code = %s", (code,))
            exists = cursor.fetchone()[0]

            if exists == 0:  # 仅在记录不存在时插入

                # 构建插入语句
                insert_stmt = """
                INSERT INTO szzf_region ( name, code, level, parent_code, sort, create_user)
                VALUES ( %s, %s, %s, %s, %s, %s)
                """
                # 计算级别
                level = 0
                if name == "山东省":
                    level = 1
                if len(name) == 2:
                    level = 2
                if name.endswith("政府"):
                    level = 3
                if name.endswith("委员会"):
                    level = 3
                if name.endswith("开发区"):
                    level = 3
                if name.endswith("试验区"):
                    level = 3
                if name.endswith("管委会"):
                    level = 3

                # 计算parentCode
                parentCode = None
                if len(name) == 2:
                    parentCode = "3700000071"
                else:
                    parentCode = find_parent_value(code)

                data_tuple = (
                    name,
                    code,
                    level,
                    parentCode,
                    0,
                    "import_user",
                )  # 'import_user' 为创建人

                # 执行插入
                cursor.execute(insert_stmt, data_tuple)
            else:
                print(f"重复数据，区域编码 {code}  - {name} 已存在，跳过插入。")

        # 提交事务
        connection.commit()

    except pymysql.MySQLError as err:
        print("MySQL error:", err)
    finally:
        # 关闭连接
        cursor.close()
        connection.close()


if __name__ == "__main__":
    etl_region()
  
    # parent = find_parent_value("3702020002")
    # print(parent)
