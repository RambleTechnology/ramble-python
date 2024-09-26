import pymysql
import random
from datetime import datetime


def etl_v1():

    # 建立数据库连接
    connection = pymysql.connect(
        host='192.168.1.128',
        user='root',
        password='J48Y5zVo1rpo7o25',
        port=3306
    )


    # 创建游标对象
    cursor = connection.cursor()

    for n in range(5,4000):
        camera_id=f"cml测试相机-{n}"
        name=f"cml测试相机-{n}"
        sql = f"INSERT INTO `ngh-smart-ar`.`hkcy_camera_equipment_info` ( `camera_index_code`, `name`, `altitude`, `longitude`, `latitude`, `type`, `camera_radius`, `camera_height`, `install_place`, `capability_set_name`, `device_index_code`, `device_resource_type`, `device_resource_type_name`, `channel_type`, `viewshed`, `ptz_controller_name`, `record_location`, `intelligent_set`, `camera_type_name`, `status_name`, `record_location_name`, `treaty_type_name`, `channel_type_name`, `trans_type_name`, `pixel`, `chan_num`, `matrix_code`, `gb_index_code`, `ptz_controller`, `camera_type`, `treaty_type`, `unit_index_code`, `intelligent_set_name`, `trans_type`, `capability_set`, `scene_id`, `scene_index_code`, `status`, `competent_unit`, `ownership_unit`, `maintenance_unit`, `person_liable`, `person_liable_phone`, `describe`, `hasdel`, `create_time`, `update_time`, `region_index_code`, `has_lock`, `lock_time`, `dept_id`, `pan_pos`, `tilt_pos`, `camera_resolution`, `org_id`, `level`, `lock_account`, `lock_camera_time`, `ad_logic_id`, `auth_field_1`, `auth_field_2`, `auth_field_3`, `auth_field_4`, `auth_field_5`, `auth_field_6`, `auth_field_7`, `auth_field_8`, `auth_field_9`, `auth_field_10`, `hik_lng`, `hik_lat`, `img_url`, `calibration`, `horizontal`, `vertical`, `external_camera_id`, `source_type`, `camera_height_type`, `floor_id`, `calibration_union`, `ad_logic_id_fill_status`, `state`, `one_screen`) VALUES ( '{camera_id}', '{name}', NULL, NULL, NULL, 0, 1000, NULL, '', '@Video Capability@', '', '', '', '', '', NULL, '0_1', '', 'Box Camera', 'Online', 'Central storage_Device storage', '', '', 'TCP', NULL, NULL, '', '52011501011328014389', '', 0, '', '52011501012168000074', '', 1, '@vss@', NULL, NULL, 1, NULL, NULL, NULL, NULL, NULL, NULL, 0, '2024-05-19T20:22:20.756+08:00', '2024-07-21T04:00:02.440+08:00', '52011501012168000074', 0, '2024-07-21 04:00:03', NULL, NULL, NULL, NULL, 'TuwObP5type29ImJ3GAOtXnAR', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '/ngh-file/ar/camera/52011501011328014389.jpg', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, NULL);"
        cursor.execute(sql)
        # 提交
    connection.commit()


if __name__ == "__main__":

    etl_v1()
