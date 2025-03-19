import pymysql
import time
import random
from datetime import datetime
import uuid


class IDGenerator:
    def __init__(self):
        self.current_id = 3110352

    def get_next_id(self):
        self.current_id += 1
        return self.current_id


def etl_v2():

    # 建立数据库连接
    connection = pymysql.connect(
        host="192.168.1.115",
        user="root",
        password="J48Y5zVo1rpo7o25",
        port=3306,
        database="ngh-smart-ar",
    )
    id_generator = IDGenerator()
    # 创建游标对象
    cursor = connection.cursor()
    cursor.execute(
        f"SELECT `tag_logic_id`, `tagname`, `longitude`, `latitude`, `longandlat`, `address`, `imgaddress`, `has_del`, `hik_status`, `hik_msg`, `tag_source`, `create_time`, `creater`, `updater`, `update_time`, `org_id`, `tag_base_info`, `external_label_id`, `label_type_logic_id`, `auth_field_1`, `auth_field_2`, `auth_field_3`, `auth_field_4`, `auth_field_5`, `auth_field_6`, `auth_field_7`, `auth_field_8`, `auth_field_9`, `auth_field_10`, `electronic_fence`, `height` from hkcy_tag_info_aircraft  limit 10000,5000 "
    )
    data = cursor.fetchall()
    for row in data:
        new_id = id_generator.get_next_id()
        tag_logic_id = row[0]
        tagname = row[1] + str(uuid.uuid4())
        if len(tagname) > 250:
            tagname = tagname[:150] + str(uuid.uuid4())
        longitude = row[2] + random.uniform(-0.01, 0.01)
        latitude = row[3] + random.uniform(-0.01, 0.01)
        longandlat = str(longitude) + "," + str(latitude)
        address = row[5]
        imgaddress = row[6]
        hik_status = row[8] if row[8] is not None else ""
        hik_msg = row[9] if row[9] is not None else ""
        tag_source = row[10] if row[10] is not None else ""
        org_id = row[15]
        tag_base_info = row[16] if row[16] is not None else ""
        external_label_id = row[17] if row[17] is not None else ""
        label_type_logic_id = row[18]
        auth_field_1 = row[19]
        auth_field_2 = row[20] if row[20] is not None else ""
        electronic_fence = row[21] if row[21] is not None else ""
        height = row[22] if row[22] is not None else 0
        now = "2024-10-11 10:52:01"
        nowtime = datetime.now()
        nowstr = str(datetime.now())
        # insert = f"INSERT INTO `hkcy_tag_info_aircraft` (id ,  `tag_logic_id`, `tagname`, `longitude`, `latitude`, `longandlat`, `address`, `imgaddress`, `has_del`, `hik_status`, `hik_msg`, `tag_source`, `create_time`, `creater`, `updater`, `update_time`, `org_id`, `tag_base_info`, `external_label_id`, `label_type_logic_id`, `auth_field_1`, `auth_field_2`, `auth_field_3`, `auth_field_4`, `auth_field_5`, `auth_field_6`, `auth_field_7`, `auth_field_8`, `auth_field_9`, `auth_field_10`, `electronic_fence`, `height`) VALUES ( {new_id} , {tag_logic_id} ,{tagname} , {longitude},{latitude},{longandlat},'{address}','{imgaddress}',0,'{hik_status}','{hik_msg}','{tag_source}','{now}','','','{now}',{org_id},'{tag_base_info}','{external_label_id}',{label_type_logic_id},{auth_field_1},'{auth_field_2}','','','','','','','','','{electronic_fence}','{height}')"

        insert = f"""
        INSERT INTO `hkcy_tag_info_aircraft` 
        (id, `tag_logic_id`, `tagname`, `longitude`, `latitude`, `longandlat`, `address`, `imgaddress`, `has_del`, `hik_status`, `hik_msg`, `tag_source`, `create_time`, `creater`, `updater`, `update_time`, `org_id`, `tag_base_info`, `external_label_id`, `label_type_logic_id`, `auth_field_1`, `auth_field_2`, `auth_field_3`, `auth_field_4`, `auth_field_5`, `auth_field_6`, `auth_field_7`, `auth_field_8`, `auth_field_9`, `auth_field_10`, `electronic_fence`,height) 
        VALUES 
        ({new_id}, '{tag_logic_id}', '{tagname}', {longitude}, {latitude}, '{longandlat}', '{address}', '{imgaddress}', 0, 0, '{hik_msg}', '{tag_source}', 
        '{now}', '', '', '{now}', '{org_id}',                            '{tag_base_info}', '{external_label_id}', {label_type_logic_id}, '{auth_field_1}', '{auth_field_2}', '', '', '', '', '', '', '','', '{electronic_fence}', {height})
        """
        cursor.execute(insert)

    connection.commit()


if __name__ == "__main__":
    etl_v2()
