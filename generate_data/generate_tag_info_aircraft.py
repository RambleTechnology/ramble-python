import pymysql
import time
import random
from datetime import datetime


def etl_v1():
    # 建立数据库连接
    connection = pymysql.connect(
        host="192.168.1.115",
        user="root",
        password="J48Y5zVo1rpo7o25",
        port=3306,
        database="ngh-smart-ar",
    )

    # 创建游标对象
    cursor = connection.cursor()

    try:
        while True:  # Start an infinite loop
            # 查询 hkcy_tag_info_aircraft 表数据，若小于15W，就新增数据
            query = "SELECT COUNT(1) FROM hkcy_tag_info_aircraft"
            cursor.execute(query)
            count = cursor.fetchone()[0]  # Get the count value from the result

            if count < 150000:
                print(f"Current record count: {count}. Inserting new data...")

                # 每次插入前休眠2秒
                time.sleep(0.1)

                # 新增数据
                insert = """
                INSERT INTO `hkcy_tag_info_aircraft` 
                (`tag_logic_id`, `tagname`, `longitude`, `latitude`, `longandlat`, `address`, 
                `imgaddress`, `has_del`, `hik_status`, `hik_msg`, `tag_source`, `create_time`, 
                `creater`, `updater`, `update_time`, `org_id`, `tag_base_info`, 
                `external_label_id`, `label_type_logic_id`, `auth_field_1`, `auth_field_2`, 
                `auth_field_3`, `auth_field_4`, `auth_field_5`, `auth_field_6`, 
                `auth_field_7`, `auth_field_8`, `auth_field_9`, `auth_field_10`, 
                `electronic_fence`, `height`) 
                SELECT 
                `tag_logic_id`, CONCAT(`tagname`, UUID()) AS tagname, `longitude`, `latitude`, 
                `longandlat`, `address`, `imgaddress`, `has_del`, `hik_status`, `hik_msg`, 
                `tag_source`, `create_time`, `creater`, `updater`, `update_time`, `org_id`, 
                `tag_base_info`, `external_label_id`, `label_type_logic_id`, `auth_field_1`, 
                `auth_field_2`, `auth_field_3`, `auth_field_4`, `auth_field_5`, `auth_field_6`, 
                `auth_field_7`, `auth_field_8`, `auth_field_9`, `auth_field_10`, 
                `electronic_fence`, `height` 
                FROM `hkcy_tag_info_aircraft_backup-20241009`
                """
                cursor.execute(insert)
                connection.commit()  # Commit the transaction after insert
                print("Data inserted successfully.")
            else:
                print(
                    f"Record count is {count}, which exceeds the limit. Terminating the program."
                )
                break  # Exit the loop if the record count exceeds or meets the limit

            time.sleep(0.1)  # Optional: Sleep before the next check

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    etl_v1()
