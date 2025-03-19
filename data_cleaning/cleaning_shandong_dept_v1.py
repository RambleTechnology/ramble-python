import pandas as pd
import pymysql
import uuid  # 导入uuid模块


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
    file_path = "山东区域和机关.xlsx"  # 替换为你的Excel文件路径
    data = pd.read_excel(file_path)

    # 创建MySQL连接
    try:
        # 插入数据到gov_region表
        for index, row in data.iterrows():
            name = row[0]  # 机关名称

            code = str(uuid.uuid4())

            region_code = str(row[2])  # 区域编码

            print(name)

            # 构建插入语句
            insert_stmt = """
            INSERT INTO szzf_dept ( name, code, region_code,  sort, create_user)
            VALUES ( %s, %s, %s, %s, %s)
            """

            data_tuple = (
                name,
                code,
                region_code,
                0,
                "import_user",
            )  # 'import_user' 为创建人

            # 执行插入
            cursor.execute(insert_stmt, data_tuple)

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
