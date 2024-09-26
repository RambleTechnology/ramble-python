import pymysql
import random
from datetime import datetime


# 仅治理带逗号的tag
def ttl_tag_with_contain_comma():
    # 建立数据库连接
    connection = pymysql.connect(
        host='192.168.1.92',
        user='root',
        password='J48Y5zVo1rpo7o25',
        # database='cml',
        port=3306
    )
    # 创建游标对象
    cursor = connection.cursor()
    # 查询业务资源和标签关联关系数据
    cursor.execute("SELECT logic_id as tag_logic_id , 业务标签类型 as tag_code , create_time as create_time  from  ngh_jd_event. merged_resources_info where demo_mark='Y' and  属性标签代码 is not NULL and 业务标签类型  like '%,%'")
    tags = cursor.fetchall()
    for tag in tags:
        # 业务资源id
        tag_logic_id = tag[0]
        # 创建时间，如果为空，获取当前时间
        create_time = tag[2]
        if create_time is None:
            create_time = datetime.now()
        # 多个标签库类型，用英文逗号隔开
        tag_code_str = tag[1]
        tag_codes = tag_code_str.split(',')
        for tag_code in tag_codes:
            # 根据 tagLogicId 和 tagCode 查询一遍，如果不存在才 insert
            cursor.execute(
                f"SELECT * from cml.hkcy_tag_info_tag_copy1  where tag_logic_id='{tag_logic_id}' and tag_code='{tag_code}'")
            exist_tag = cursor.fetchall()
            if len(exist_tag) == 0:
                insert_sql = f"INSERT into cml.hkcy_tag_info_tag_copy1(tag_logic_id , tag_code , create_time,create_user)	VALUES ('{tag_logic_id}','{tag_code}','{create_time}','手工治理')"
                cursor.execute(insert_sql)
                print(
                    f"insert success , tag_logic_id={tag_logic_id},tag_code={tag_code}")

        # 提交
        connection.commit()

# 第一次全量治理


def ttl_v1():

    # 建立数据库连接
    connection = pymysql.connect(
        host='192.168.1.92',
        user='root',
        password='J48Y5zVo1rpo7o25',
        # database='cml',
        port=3306
    )
    # 创建游标对象
    cursor = connection.cursor()
    # 查询业务资源和标签关联关系数据
    cursor.execute("SELECT logic_id as tag_logic_id , 业务标签类型 as tag_code , create_time as create_time  from  ngh_jd_event. merged_resources_info where demo_mark='Y' and  属性标签代码 is not NULL and 业务标签类型 is not null ")
    tags = cursor.fetchall()
    for tag in tags:
        # 业务资源id
        tag_logic_id = tag[0]
        # 创建时间，如果为空，获取当前时间
        create_time = tag[2]
        if create_time is None:
            create_time = datetime.now()
        # 多个标签库类型，用英文逗号隔开
        tag_code_str = tag[1]
        tag_codes = tag_code_str.split(',')
        for tag_code in tag_codes:
            # 根据 tagLogicId 和 tagCode 查询一遍，如果不存在才 insert
            cursor.execute(
                f"SELECT * from cml.hkcy_tag_info_tag_copy1  where tag_logic_id='{tag_logic_id}' and tag_code='{tag_code}'")
            exist_tag = cursor.fetchall()
            if len(exist_tag) == 0:
                insert_sql = f"INSERT into cml.hkcy_tag_info_tag_copy1(tag_logic_id , tag_code , create_time,create_user)	VALUES ('{tag_logic_id}','{tag_code}','{create_time}','手工治理')"
                cursor.execute(insert_sql)
                print(
                    f"insert success , tag_logic_id={tag_logic_id},tag_code={tag_code}")

        # 提交
        connection.commit()


# 第二次增量治理：通州区7月份新增 16 条数据


def ttl_v2():
    # 建立数据库连接
    connection = pymysql.connect(
        host='192.168.1.92',
        user='root',
        password='J48Y5zVo1rpo7o25',
        # database='cml',
        port=3306
    )
    # 创建游标对象
    cursor = connection.cursor()
    # 查询业务资源和标签关联关系数据
    cursor.execute("SELECT logic_id as tag_logic_id , 业务标签类型 as tag_code , create_time as create_time  from  ngh_jd_event. merged_resources_info where demo_mark='Y' and  属性标签代码 in ('001921002001','001902005002') and `城市`='通州区'  and  业务标签类型 is not NULL ")
    tags = cursor.fetchall()
    for tag in tags:
        # 业务资源id
        tag_logic_id = tag[0]
        # 创建时间，如果为空，获取当前时间
        create_time = tag[2]
        if create_time is None:
            create_time = datetime.now()
        # 多个标签库类型，用英文逗号隔开
        tag_code_str = tag[1]
        tag_codes = tag_code_str.split(',')
        for tag_code in tag_codes:
            # 根据 tagLogicId 和 tagCode 查询一遍，如果不存在才 insert
            cursor.execute(
                f"SELECT * from cml.hkcy_tag_info_tag_copy1  where tag_logic_id='{tag_logic_id}' and tag_code='{tag_code}'")
            exist_tag = cursor.fetchall()
            if len(exist_tag) == 0:
                insert_sql = f"INSERT into cml.hkcy_tag_info_tag_copy1(tag_logic_id , tag_code , create_time,create_user)	VALUES ('{tag_logic_id}','{tag_code}','{create_time}','手工治理')"
                cursor.execute(insert_sql)
                print(
                    f"insert success , tag_logic_id={tag_logic_id},tag_code={tag_code}")

        # 提交
        connection.commit()

# 第三次增量治理：杭州市7月10号新增 180 条数据


def ttl_v3():

    # 建立数据库连接
    connection = pymysql.connect(
        host='192.168.1.92',
        user='root',
        password='J48Y5zVo1rpo7o25',
        # database='cml',
        port=3306
    )
    # 创建游标对象
    cursor = connection.cursor()
    # 查询业务资源和标签关联关系数据
    cursor.execute("SELECT logic_id as tag_logic_id , 业务标签类型 as tag_code , create_time as create_time  from  ngh_jd_event. merged_resources_info where demo_mark='Y' and  城市='杭州市' and `属性标签代码` in ('001915013004','001915013012','001906008002','001906006002','001911030002') and create_time>DATE('2024-07-10') and  业务标签类型 is not NULL ")
    tags = cursor.fetchall()
    for tag in tags:
        # 业务资源id
        tag_logic_id = tag[0]
        # 创建时间，如果为空，获取当前时间
        create_time = tag[2]
        if create_time is None:
            create_time = datetime.now()
        # 多个标签库类型，用英文逗号隔开
        tag_code_str = tag[1]
        tag_codes = tag_code_str.split(',')
        for tag_code in tag_codes:
            # 根据 tagLogicId 和 tagCode 查询一遍，如果不存在才 insert
            cursor.execute(
                f"SELECT * from cml.hkcy_tag_info_tag_copy1  where tag_logic_id='{tag_logic_id}' and tag_code='{tag_code}'")
            exist_tag = cursor.fetchall()
            if len(exist_tag) == 0:
                insert_sql = f"INSERT into cml.hkcy_tag_info_tag_copy1(tag_logic_id , tag_code , create_time,create_user)	VALUES ('{tag_logic_id}','{tag_code}','{create_time}','手工治理')"
                cursor.execute(insert_sql)
                print(
                    f"insert success , tag_logic_id={tag_logic_id},tag_code={tag_code}")

        # 提交
        connection.commit()

"""
此脚本用来治理 hkcy_tag_info_tag 表的数据

属性标签代码 = 资源分类 ， 即 labelType
业务标签类型 = 标签库中的标签类型，即 tag 工程中的 tag_info

ttl_tag_with_contain_comma方法用来治理 业务标签类型 字段中带逗号的数据
ttl_v1方法用来治理 全量数据
ttl_v2增量治理：通州区7月份新增 16 条数据
ttl_v3增量治理：杭州市7月10号新增 180 条数据

"""
if __name__ == "__main__":

    # 仅治理带逗号的标签
    # ttl_tag_with_contain_comma()

    # 第一次全量治理
    # ttl_v1()

    # 第二次增量治理：通州区7月份新增 16 条数据
    # ttl_v2()

    # 第三次增量治理：杭州市7月10号新增 180 条数据
    ttl_v3()
