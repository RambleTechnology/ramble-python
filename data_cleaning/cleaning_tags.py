import pandas as pd
import pymysql
import uuid  # 导入uuid模块


def etl_tags():
    # 建立数据库连接
    connection = pymysql.connect(
        host="192.168.1.82",
        user="root",
        password="",
        port=9030,
        database="test",
    )

    # 创建游标对象
    cursor = connection.cursor()

    # 创建MySQL连接
    try:
        # SQL 查询语句
        sql = """
        SELECT tag_logic_id, `tagname`, `longandlat`, 
               GROUP_CONCAT(tag_code SEPARATOR ',') AS tag_codes  
        FROM `ar_149`.hkcy_tag_info
        WHERE tag_code IS NOT NULL AND tag_code != ''  
        GROUP BY tag_logic_id, `tagname`, `longandlat`;
        """

        # 执行 SQL 查询
        cursor.execute(sql)

        # 获取所有结果
        results = cursor.fetchall()

        # 输出结果到控制台
        for row in results:
            tag_logic_id, tagname, longandlat, tag_codes = row
            print(
                f"tag_logic_id: {tag_logic_id}, tagname: {tagname}, longandlat: {longandlat}, tag_codes: {tag_codes}"
            )
            # 更新 tag_info  的 tags 字段
            update_query = """
                             UPDATE `test`.tag_info
                             SET tags = %s
                             where tagname = %s and  longandlat = %s ;
                            """
            tags = str(tag_codes).split(",")
            cursor.execute(update_query, (tags, tagname, longandlat))
            print("update success!!!")
        connection.commit()
    except pymysql.MySQLError as err:
        print("MySQL error:", err)
    finally:
        # 关闭连接
        cursor.close()
        connection.close()


if __name__ == "__main__":
    etl_tags()
