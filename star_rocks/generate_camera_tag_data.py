import pymysql
import random


def test_connection():
    # 建立数据库连接
    connection = pymysql.connect(
        host='192.168.1.82',
        user='root',
        # password='your_password',
        database='test',
        port=9030
    )

    # 创建游标对象
    cursor = connection.cursor()

    # 执行SQL查询
    cursor.execute(
        "SELECT * FROM tag  where tags  is null  order by id desc  limit 1  ")

    # 获取查询结果
    result = cursor.fetchall()

    # 打印结果
    for row in result:
        print(row)

    # 关闭游标和连接
    cursor.close()
    connection.close()


def test():
    data = [
        (3239532, '00000000GsTdd8gvMF', '3504120102',
         'datetime.datetime(2020, 11, 23, 17, 17, 26)'),
        (3239532, '00000000GsTdd8gvMF', '3504120102',
         'datetime.datetime(2020, 11, 23, 17, 17, 26)'),
        (3239532, '00000000GsTdd8gvMF', '3504120103',
         'datetime.datetime(2020, 11, 23, 17, 17, 26)'),
        (3239532, '00000000GsTdd8gvMF', '3504120102',
         'datetime.datetime(2020, 11, 23, 17, 17, 26)')
    ]

    # 使用列表推导式提取第三个元素，并拼接成字符串
    concatenated = ''.join([item[2] for item in data])
    codes = set()
    for item in data:
        codes.add(item[2])
    str = ','.join(codes)

    print('['+str+']')


def test_insert():
    # 建立数据库连接
    connection = pymysql.connect(
        host='192.168.1.92',
        user='root',
        password='J48Y5zVo1rpo7o25',
        database='ngh-smart-ar',
        port=3306
    )
    # 创建游标对象
    cursor = connection.cursor()
    id = "1"
    tag_code = "2"
    insert_sql = f"INSERT into hkcy_camera_equipment_tag (camera_id , tag_code) VALUES ('{id}','{tag_code}')"
    cursor.execute(insert_sql)
    connection.commit()


def build_camera_tags():

    # 建立数据库连接
    connection = pymysql.connect(
        host='192.168.1.92',
        user='root',
        password='J48Y5zVo1rpo7o25',
        database='ngh-smart-ar',
        port=3306
    )
    # 创建游标对象
    cursor = connection.cursor()

    # 标签的链接
    tag_connection = pymysql.connect(
        host='192.168.1.92',
        user='root',
        password='J48Y5zVo1rpo7o25',
        database='ngh-smart-tag',
        port=3306
    )
    # 标签链接对应的游标
    tag_cursor = tag_connection.cursor()

    batch_size = 3000
    startId = 500000
    endId = 1052798

    # 查询标签数据
    tag_cursor.execute("SELECT tag_code from tag_info")
    tags = tag_cursor.fetchall()
    while startId < endId:
        print(
            f"分批生成 camera_tag ,当前批次，startId={startId},endId={startId+batch_size}")
        # 查询相机数据
        cursor.execute(
            f"SELECT camera_index_code FROM hkcy_camera_equipment_info  where id>= '{startId}' and id <'{startId+batch_size}'")
        cameras = cursor.fetchall()

        for camera_id in cameras:
            # 相机id
            id = camera_id[0]
            # 随机获取一个标签
            tag_code = random.choice(tags)[0]
            # 向cameraTag 表插入数据
            insert_sql = f"INSERT into hkcy_camera_equipment_tag (camera_id , tag_code) VALUES ('{id}','{tag_code}')"
            cursor.execute(insert_sql)

            # print(f"insert success , camera_index_code={id}")
        # 提交
        connection.commit()
        # 增加循环变量
        startId = startId+batch_size

def build_camera_tags_2():

    # 建立数据库连接
    connection = pymysql.connect(
        host='192.168.1.92',
        user='root',
        password='J48Y5zVo1rpo7o25',
        database='ngh-smart-ar',
        port=3306
    )
    # 创建游标对象
    cursor = connection.cursor()

    # 标签的链接
    tag_connection = pymysql.connect(
        host='192.168.1.92',
        user='root',
        password='J48Y5zVo1rpo7o25',
        database='ngh-smart-tag',
        port=3306
    )
    # 标签链接对应的游标
    tag_cursor = tag_connection.cursor()

    batch_size = 3000
    startId = 1000000
    endId = 700000

    # 查询标签数据
    tag_cursor.execute("SELECT tag_code from tag_info")
    tags = tag_cursor.fetchall()
    while startId < endId:
        print(
            f"分批生成 camera_tag ,当前批次，startId={startId},endId={startId+batch_size}")
        # 查询相机数据
        cursor.execute(
            f"SELECT camera_index_code FROM hkcy_camera_equipment_info where camera_index_code not in (SELECT camera_id  from hkcy_camera_equipment_tag GROUP BY camera_id ) and id>= '{startId}' and id <'{startId+batch_size}'")
        cameras = cursor.fetchall()

        for camera_id in cameras:
            # 相机id
            id = camera_id[0]
            # 随机获取一个标签
            tag_code = random.choice(tags)[0]
            # 向cameraTag 表插入数据
            insert_sql = f"INSERT into hkcy_camera_equipment_tag (camera_id , tag_code) VALUES ('{id}','{tag_code}')"
            cursor.execute(insert_sql)

            # print(f"insert success , camera_index_code={id}")
        # 提交
        connection.commit()
        # 增加循环变量
        startId = startId+batch_size

if __name__ == "__main__":

    # test_connection()
    # build_tags()
    build_camera_tags()
    # build_camera_tags_2()
    # test_insert()
