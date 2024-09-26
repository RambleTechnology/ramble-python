import pymysql
import uuid
from concurrent.futures import ThreadPoolExecutor


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

# 若 cameraIndexCode相同，更新其中一个


def build_camera_index_code():

    # 建立数据库连接
    connection = pymysql.connect(
        host='192.168.1.82',
        user='root',
        # password='your_password',
        database='ngh_smart_ar',
        port=9030
    )

    # 创建游标对象
    cursor = connection.cursor()

    cursor.execute(
        " SELECT any_value(id ) ,  camera_index_code , tag_code  , count(1) as  n   from camera where auth_field_1 is not null  GROUP BY camera_index_code , tag_code  HAVING n>3 ")
    cameras = cursor.fetchall()
    for c in cameras:
        n = c[3]
        cameraId = c[1]
        uid = uuid.uuid1()
        newCameraId = cameraId+str(uid)
        id = c[0]
        if(n > 1):
            cursor.execute(
                f" update  camera  set  camera_index_code='{newCameraId}' where id = {id}")
            print(f"数据更新成功，oldCameraId={cameraId},newCameraId={newCameraId}")


def build_camera_index_code_with_thread_pool():

    # 建立数据库连接
    connection = pymysql.connect(
        host='192.168.1.82',
        user='root',
        # password='your_password',
        database='ngh_smart_ar',
        port=9030
    )

    # 创建游标对象
    cursor = connection.cursor()

    cursor.execute(
        " SELECT any_value(id ) ,  camera_index_code , tag_code  , count(1) as  n   from camera where auth_field_1 is not null  GROUP BY camera_index_code , tag_code  ")
    cameras = cursor.fetchall()
    for c in cameras:
        n = c[3]
        cameraId = c[1]
        uid = uuid.uuid1()
        newCameraId = cameraId+str(uid)
        id = c[0]
        if(n > 1):
            with ThreadPoolExecutor(max_workers=200) as executor:
                executor.submit(do_update, cursor, cameraId, newCameraId, id)


def do_update(cursor, cameraId, newCameraId, id):
    cursor.execute(
        f" update  camera  set  camera_index_code='{newCameraId}' where id = {id}")
    print(f"数据更新成功，oldCameraId={cameraId},newCameraId={newCameraId}")


if __name__ == "__main__":

    # test_connection()
    # build_camera_index_code()
    build_camera_index_code_with_thread_pool()
    # test()
