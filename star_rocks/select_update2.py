import pymysql


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


def build_tags():

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

    for i in range(600000):
        cursor.execute(
            "SELECT * FROM tag  where tags  is null  order by id  desc   limit 1  ")
        result = cursor.fetchall()
        logic_id = result[0][1]
        sql = 'SELECT * FROM hkcy_tag_info_outer_tag  where tag_logic_id =' + '\''+logic_id+'\''
        cursor.execute(sql)
        data = cursor.fetchall()
        codes = set()
        for item in data:
            codes.add(item[2])
        str = '['+','.join(codes)+']'
        update_sql = f"update tag set tags='{str}' where tag_logic_id = '{logic_id}' "
        cursor.execute(update_sql)
        
        print(f"update success , tagLogicId={logic_id}")


if __name__ == "__main__":

    # test_connection()
    build_tags()
    # test()
