import psycopg2
from psycopg2 import Error

try:
    # 连接到 PostgreSQL 数据库
    connection = psycopg2.connect(user="db_suriver_services",
                                  password="admin@123!",
                                  host="192.168.1.224",
                                  port="5432",
                                  database="ngh_test")

    cursor = connection.cursor()

    # 插入数据的 SQL 语句
    postgres_insert_query = """INSERT INTO "ar"."poi_info" ("logic_id", "poi_name", "address", "longitude", "latitude", "state", "poi_source", "org_id", "dept_id", "has_del", "create_user", "create_time", "update_user", "label_type_logic_id", "ad_code", "auth_field_1", "auth_field_2", "auth_field_3", "auth_field_4", "auth_field_5", "auth_field_6", "auth_field_7", "auth_field_8", "auth_field_9", "auth_field_10", "electronic_fence", "floor_id", "build_id", "ad_code_fill_status", "type_code") 
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    
    # 要插入的数据
    record_to_insert = ('1111', 'poi_name_value', 'address_value', 0.0, 0.0, 0, 'poi_source_value', 'org_id_value', 'dept_id_value', 0, 'create_user_value', '2024-05-13 10:00:00', 'update_user_value', 'label_type_logic_id_value', 'ad_code_value', 'auth_field_1_value', 'auth_field_2_value', 'auth_field_3_value', 'auth_field_4_value', 'auth_field_5_value', 'auth_field_6_value', 'auth_field_7_value', 'auth_field_8_value', 'auth_field_9_value', 'auth_field_10_value', 'electronic_fence_value', 'floor_id_value', 'build_id_value', 0, 'type_code_value')

    # 执行 SQL 语句
    # cursor.execute(postgres_insert_query, record_to_insert)
     

    # 提交事务
    connection.commit()
    print("数据插入成功")

except (Exception, Error) as error:
    print("数据插入失败:", error)

finally:
    # 关闭数据库连接
    if connection:
        cursor.close()
        connection.close()
        print("连接已关闭")