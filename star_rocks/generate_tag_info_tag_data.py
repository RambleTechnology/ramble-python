import pymysql
import random
from datetime import datetime


def build_tag_info_tag():

    # 建立数据库连接
    connection = pymysql.connect(
        host='192.168.1.92',
        user='root',
        password='J48Y5zVo1rpo7o25',
        database='cml',
        port=3306
    )
    # 创建游标对象
    cursor = connection.cursor()

    # 标签的链接
    tag_connection = pymysql.connect(
        host='192.168.1.92',
        user='root',
        password='J48Y5zVo1rpo7o25',
        database='ngh_jd_event',
        port=3306
    )
    # 标签链接对应的游标
    tag_cursor = tag_connection.cursor()

    # 查询标签数据
    tag_cursor.execute("SELECT logic_id as tag_logic_id , 业务标签类型 as tag_code , NOW()  as  create_time , '手工治理' as create_user  from  ngh_jd_event. merged_resources_info where 业务标签类型 is not NULL and 业务标签类型  like '%,%'")
    tags = tag_cursor.fetchall()
    for tag in tags:
        # 业务资源id
        tag_logic_id = tag[0]
        # 多个标签库类型，用英文逗号隔开
        tag_code_str = tag[1]
        lists = tag_code_str.split(',')
        for item in lists:
            tag_code = item
            now_time = datetime.now()
            insert_sql = f"INSERT into hkcy_tag_info_tag(tag_logic_id , tag_code , create_time,create_user)	VALUES ('{tag_logic_id}','{tag_code}','{now_time}','手工治理')"
            cursor.execute(insert_sql)
            print(f"insert success , tag_logic_id={tag_logic_id}")

        # 提交
        connection.commit()



if __name__ == "__main__":


    build_tag_info_tag()

