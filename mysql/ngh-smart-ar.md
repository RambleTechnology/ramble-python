


### algorithm_task_record (算法任务记录表) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 4 | algorithm_type | int | YES | 算法类型：1溺水  2非机动车乱停放 |
| 2 | camera_index_code | varchar(255) | YES | 相机设备编号 |
| 11 | create_time | datetime | YES | 创建时间 |
| 10 | create_user | varchar(100) | YES | 创建者账号 |
| 6 | end_time | datetime | YES | 结束时间 |
| 7 | execute_interval | int | YES | 间隔：秒 |
| 8 | has_del | int | YES | 是否删除 |
| 1 | id | int | NO |  |
| 3 | identification_range | varchar(255) | YES | 需要识别的范围：水域等 |
| 9 | remark | varchar(255) | YES | 备注 |
| 5 | start_time | datetime | YES | 启动时间 |
| 13 | update_time | datetime | YES | 更新时间 |
| 12 | update_user | varchar(100) | YES | 更新者账号 |



### aoi_info (矢量绘制aoi上图) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 3 | address | varchar(255) | YES | 地址 |
| 4 | coordinates | text | YES | 坐标值 |
| 11 | create_time | datetime | YES | 创建时间 |
| 10 | create_user | varchar(255) | YES | 创建人 |
| 7 | drawing_type | int | YES | 类型：1=线型；2=区域型 |
| 9 | has_del | int | YES | 逻辑删除标识 |
| 1 | id | bigint | NO | 主键 |
| 2 | name | varchar(255) | YES | 名称 |
| 8 | source | varchar(255) | YES | 来源 |
| 5 | state | int | YES | 0=未撒点；1=已撒点；2=无关联设备；3=待更新 |
| 6 | tag_type | varchar(255) | YES | 标签类型: 业务资源子节点 |
| 13 | update_time | datetime | YES | 更新时间 |
| 12 | update_user | varchar(255) | YES | 更新人 |



### ar_map_config () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | config_group | varchar(255) | YES | 配置组 |
| 3 | config_key | varchar(255) | YES | 配置项目 |
| 4 | config_value | varchar(3000) | YES | 配置值 |
| 8 | create_time | datetime | YES | 创建时间 |
| 7 | create_user | varchar(100) | YES | 创建人 |
| 5 | description | varchar(600) | YES | 描述 |
| 6 | has_del | smallint | YES | 逻辑删除标识：0=未删除；1=已删除 |
| 1 | id | int | NO | 主键id |
| 10 | update_time | datetime | YES | 更新时间 |
| 9 | update_user | varchar(100) | YES | 更新人 |



### ar_map_config_202410222310 () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | config_group | varchar(255) | YES | 配置组 |
| 3 | config_key | varchar(255) | YES | 配置项目 |
| 4 | config_value | varchar(3000) | YES | 配置值 |
| 8 | create_time | datetime | YES | 创建时间 |
| 7 | create_user | varchar(100) | YES | 创建人 |
| 5 | description | varchar(600) | YES | 描述 |
| 6 | has_del | smallint | YES | 逻辑删除标识：0=未删除；1=已删除 |
| 1 | id | int | NO | 主键id |
| 10 | update_time | datetime | YES | 更新时间 |
| 9 | update_user | varchar(100) | YES | 更新人 |



### ar_map_config_group () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 6 | create_time | datetime | YES | 创建时间 |
| 5 | create_user | varchar(100) | YES | 创建人 |
| 4 | has_del | smallint | YES | 逻辑删除标识：0=未删除；1=已删除 |
| 1 | id | int | NO |  |
| 2 | name | varchar(255) | YES | 配置组名称 |
| 8 | update_time | datetime | YES | 更新时间 |
| 7 | update_user | varchar(100) | YES | 更新人 |
| 3 | version | int | YES | 版本 |



### calibration_ball (联动标定球机记录表) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 3 | bd_image_url | varchar(255) | YES | 标定球机截图URL |
| 7 | bd_points | text | YES | 标定点信息 |
| 2 | calibration_union_id | int | YES | 联动标定ID |
| 8 | create_time | datetime | YES | 创建时间 |
| 9 | create_user | varchar(255) | YES | 创建者 |
| 4 | dp | double | YES | 标定截图时，相机的水平旋转角度 |
| 5 | dt | double | YES | 标定截图时，相机的垂直旋转角度 |
| 6 | dz | double | YES | 标定截图时，相机的焦距倍数 |
| 1 | id | int | NO |  |
| 10 | update_time | datetime | YES | 更新时间 |
| 11 | update_user | varchar(255) | YES | 更新者 |



### calibration_source (标定录入信息) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 3 | bd_image_url | varchar(255) | YES | 标定截图URL |
| 7 | bd_points | text | YES | 标定点信息 |
| 2 | camera_index | varchar(255) | NO | 相机编号 |
| 8 | create_time | datetime | YES | 创建时间 |
| 9 | create_user | varchar(255) | YES | 创建者 |
| 4 | dp | double | YES | 标定截图时，相机的水平旋转角度 |
| 5 | dt | double | YES | 标定截图时，相机的垂直旋转角度 |
| 6 | dz | double | YES | 标定截图时，相机的焦距倍数 |
| 1 | id | int | NO |  |
| 10 | update_time | datetime | YES | 更新时间 |
| 11 | update_user | varchar(255) | YES | 更新者 |



### calibration_union_record (联合标定记录表) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 3 | bd_image_url | varchar(255) | YES | 全景标定截图URL |
| 2 | camera_index | varchar(255) | YES | 全景相机编号 |
| 4 | create_time | datetime | YES | 创建时间 |
| 5 | create_user | varchar(255) | YES | 创建者 |
| 1 | id | int | NO |  |
| 6 | update_time | datetime | YES | 更新时间 |
| 7 | update_user | varchar(255) | YES | 更新者 |



### carousel_detail (轮播详情表) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 3 | camera_index_code | varchar(255) | YES | 相机设备编号 |
| 2 | carousel_id | int | YES | 轮播ID |
| 10 | create_time | datetime | YES | 创建时间 |
| 9 | create_user | varchar(100) | YES | 创建者账号 |
| 7 | has_del | int | YES | 是否删除 |
| 1 | id | int | NO |  |
| 5 | play_interval | int | YES | 播放间隔 |
| 8 | remark | varchar(255) | YES | 备注 |
| 6 | sort | int | YES | 排序字段 |
| 4 | type | varchar(255) | YES | 相机类型 |
| 12 | update_time | datetime | YES | 更新时间 |
| 11 | update_user | varchar(100) | YES | 更新者账号 |



### carousel_info (轮播信息表) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 7 | create_time | datetime | YES | 创建时间 |
| 6 | create_user | varchar(100) | YES | 创建者账号 |
| 4 | has_del | int | YES | 是否删除 |
| 1 | id | int | NO |  |
| 2 | name | varchar(255) | YES | 轮播名称 |
| 5 | remark | varchar(255) | YES | 备注 |
| 3 | status | int | YES | 是否启用状态：0未启用   1启用 |
| 9 | update_time | datetime | YES | 更新时间 |
| 8 | update_user | varchar(100) | YES | 更新者账号 |



### client_version_record (客户端版本记录) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 9 | create_time | datetime | YES | 创建时间 |
| 8 | create_user | varchar(100) | YES | 创建者账号 |
| 4 | description | varchar(500) | YES | 版本说明 |
| 5 | download_url | varchar(500) | YES | 下载地址 |
| 6 | has_del | int | YES | 是否删除 |
| 1 | id | int | NO |  |
| 3 | name | varchar(255) | YES | 客户端名称 |
| 12 | publish | int | YES | 发布状态：0未发布1已发布 |
| 7 | remark | varchar(255) | YES | 备注 |
| 11 | update_time | datetime | YES | 更新时间 |
| 10 | update_user | varchar(100) | YES | 更新者账号 |
| 2 | version | varchar(255) | YES | 版本号 |



### dynamic_resource_history (动态资源轨迹历史表) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 5 | create_time | datetime | YES | 创建时间 |
| 2 | device_code | varchar(50) | YES | 资源编号 |
| 1 | id | bigint | NO |  |
| 4 | latitude | double | YES | 纬度 |
| 3 | longitude | double | YES | 经度 |



### dynamic_resource_info (动态资源对象主表) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 7 | base_info | json | YES | 基本信息，详情页面扩展信息json |
| 10 | create_time | datetime | YES | 创建时间 |
| 8 | create_user | varchar(100) | YES | 创建者账号 |
| 2 | device_code | varchar(50) | YES | 资源编号 |
| 3 | device_name | varchar(100) | YES | 资源名称 |
| 1 | id | bigint | NO |  |
| 4 | label_type_logic_id | varchar(100) | YES | 资源类型 |
| 6 | latitude | double | YES | 纬度 |
| 17 | locations | text | YES | 绘制的线 |
| 5 | longitude | double | YES | 经度 |
| 16 | mock_end_time | varchar(50) | YES | 模拟结束时间 |
| 15 | mock_start_time | varchar(50) | YES | 模拟开始时间 |
| 13 | region_id | varchar(50) | YES | 区域ID |
| 12 | source | varchar(20) | YES | 来源 |
| 14 | update_frequency | varchar(20) | YES | 更新频率 |
| 11 | update_time | datetime | YES | 更新时间 |
| 9 | update_user | varchar(100) | YES | 更新者账号 |



### event_graph (事件上图关联关系表) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 6 | create_time | datetime | YES | 创建时间 |
| 5 | create_user | varchar(255) | YES | 创建者账号 |
| 2 | event_id | varchar(255) | YES | 事件的ID |
| 1 | id | int | NO | 主键ID |
| 3 | layer_id | varchar(255) | YES | 上图资源 |
| 7 | region_code | varchar(20) | YES |  |
| 4 | type | int | YES | 事件类型（1.事件 2.兴趣点 3.政务公开） |



### gis_label_type () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 29 | ambiguity | varchar(255) | YES | 模糊程度 |
| 38 | auth_field_1 | varchar(100) | YES |  |
| 47 | auth_field_10 | varchar(100) | YES |  |
| 39 | auth_field_2 | varchar(100) | YES |  |
| 40 | auth_field_3 | varchar(100) | YES |  |
| 41 | auth_field_4 | varchar(100) | YES |  |
| 42 | auth_field_5 | varchar(100) | YES |  |
| 43 | auth_field_6 | varchar(100) | YES |  |
| 44 | auth_field_7 | varchar(100) | YES |  |
| 45 | auth_field_8 | varchar(100) | YES |  |
| 46 | auth_field_9 | varchar(100) | YES |  |
| 18 | click_style | varchar(255) | YES | 线面：点击样式 |
| 17 | clickable | int | YES | 点线面：是否可点击：1是  0否 |
| 33 | create_time | datetime | YES | 创建时间 |
| 32 | create_user | varchar(255) | YES | 创建人 |
| 6 | default_above | int | YES | 默认上图： 1是  0否 |
| 10 | default_effect | varchar(255) | YES | 默认效果 |
| 24 | display_gif | int | YES | 线：是否显示动图：1是 0否 |
| 26 | display_point | int | YES | 面：撒点是否显示：1是 0否 |
| 25 | gif_url | varchar(255) | YES | 线：动图url |
| 30 | gradual_change | varchar(255) | YES | 渐变区间 |
| 31 | has_del | int | YES | 逻辑删除标识：0=未删除；1=已删除 |
| 9 | icon_url | varchar(500) | YES | 图标url |
| 1 | id | int | NO | 主键ID |
| 12 | leaf | int | YES | 是否为叶子节点：0=否；1=是 |
| 7 | legend_display | int | YES | 图例显示： 1是 0否 |
| 13 | legend_flag | tinyint(1) | YES | 图例是否配置上图资源 1-true 0-false |
| 5 | level | int | YES | 级别 |
| 2 | logic_id | varchar(255) | YES | 逻辑id |
| 3 | name | varchar(255) | YES | 名称 |
| 37 | org_id | varchar(50) | YES |  |
| 4 | parent_id | varchar(255) | YES | 父级id |
| 15 | point_icon_url | varchar(255) | YES | 点面：撒点图标url |
| 16 | polygon_default_style | varchar(255) | YES | 点：默认效果；线面：默认样式 |
| 27 | radius | varchar(255) | YES | 单个点半径 |
| 36 | region_code | varchar(20) | YES |  |
| 11 | select_effect | varchar(255) | YES | 选中效果 |
| 19 | select_effect_two | varchar(255) | YES | 点面：选中效果 |
| 8 | sort | int | YES | 排序：正整数，值越大越靠后 |
| 23 | text_click_style | varchar(255) | YES | 点线面：文本点击样式 |
| 22 | text_default_style | varchar(500) | YES |  |
| 20 | text_display | int | YES | 点线面：文本是否显示：1是  0否 |
| 21 | text_location | int | YES | 点线面：文本显示位置：1上中  2下中 |
| 28 | transparency | varchar(255) | YES | 透明度 |
| 14 | type | int | YES | 上图类型：1点 2线 3面 |
| 35 | update_time | datetime | YES | 更新时间 |
| 34 | update_user | varchar(255) | YES | 更新人 |



### gis_operation_report () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 15 | auth_field | varchar(16) | YES |  |
| 11 | create_time | datetime | YES | 创建时间 |
| 10 | create_user | varchar(255) | YES | 创建人 |
| 9 | has_del | int | YES | 逻辑删除标识：0=未删除；1=已删除 |
| 1 | id | bigint | NO |  |
| 3 | logic_id | varchar(50) | YES | 图层id |
| 4 | name | varchar(255) | YES | 图层名称 |
| 5 | operation_report_exists | tinyint(1) | YES | 是否存在运维报告 |
| 6 | operation_report_url | varchar(255) | YES | 运维报告是否存在 |
| 14 | org_id | varchar(50) | YES |  |
| 7 | region_code | varchar(255) | YES | 区划id |
| 8 | region_name | varchar(255) | YES | 区划名称 |
| 2 | task_id | varchar(50) | YES | 任务id |
| 13 | update_time | datetime | YES | 更新时间 |
| 12 | update_user | varchar(255) | YES | 更新人 |



### gis_type_region () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | logic_id | varchar(50) | YES | 标签分类logicId |
| 1 | region_id | varchar(50) | YES | 行政区划id |



### hkcy_business_log (预案操作日志) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 5 | api_type | int | YES | 接口类型-1视角，2预案，3排期 |
| 2 | business_id | varchar(50) | YES | 业务id |
| 11 | create_time | datetime | YES | 创建时间 |
| 10 | create_user | varchar(100) | YES | 创建者账号 |
| 7 | dept_id | varchar(50) | YES | 所属部门 |
| 9 | has_del | smallint | YES | 是否删除 |
| 1 | id | int | NO |  |
| 4 | operate_type | int | YES | 操作类型-3更新、2新增、4删除、1查询、0其他(未设置) |
| 3 | operation | varchar(100) | YES | 操作内容 |
| 6 | org_id | varchar(50) | YES | 所属组织 |
| 8 | remark | varchar(200) | YES | 备注 |



### hkcy_camera_equipment_alias (设备别名表) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 5 | camera_equipment_alias | varchar(200) | YES | 设备别名 |
| 4 | camera_index_code | varchar(50) | YES | 设备编号 |
| 9 | create_time | datetime | YES | 创建时间 |
| 8 | create_user | varchar(20) | YES | 创建者账号 |
| 2 | dept_id | varchar(50) | YES | 部门id |
| 3 | dept_name | varchar(200) | YES | 部门名称 |
| 6 | has_del | smallint | YES | 是否删除 |
| 1 | id | int | NO | 主键 |
| 7 | remark | varchar(255) | YES | 备注 |
| 11 | update_time | datetime | YES | 更新时间 |
| 10 | update_user | varchar(20) | YES | 更新者账号 |



### hkcy_camera_equipment_info (摄像设备信息表) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 60 | ad_logic_id | varchar(64) | YES | 所属行政区划（智广）。已作废，当前区划用auth_field_1-10维护 |
| 82 | ad_logic_id_fill_status | int | YES | ad_logic_id填充状态： 0手动填充 1自动填充成功 2自动填充失败 |
| 4 | altitude | double | YES | 海拔 |
| 61 | auth_field_1 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 70 | auth_field_10 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 62 | auth_field_2 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 63 | auth_field_3 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 64 | auth_field_4 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 65 | auth_field_5 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 66 | auth_field_6 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 67 | auth_field_7 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 68 | auth_field_8 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 69 | auth_field_9 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 74 | calibration | text | YES | 相机标定信息 |
| 81 | calibration_union | text | YES | 全景球机联合标定信息 |
| 9 | camera_height | double | YES | 摄像头可视域高度 |
| 79 | camera_height_type | int | YES |  |
| 2 | camera_index_code | varchar(100) | YES | 监控点唯一标识 |
| 8 | camera_radius | double | YES | 摄像头可视域半径 |
| 55 | camera_resolution | varchar(255) | YES | 设备视频分辨率 |
| 31 | camera_type | int | YES | 监控点类型0-枪机,1-半球,2-快球,3-带云台枪机 |
| 20 | camera_type_name | varchar(255) | YES | 监控点类型说明 |
| 36 | capability_set | text | YES | 能力集（详见数据字典，typeCode为xresmgr.capability_set） |
| 11 | capability_set_name | text | YES | 能力集说明 |
| 27 | chan_num | int | YES | 通道号 |
| 15 | channel_type | varchar(255) | YES | 通道类型 |
| 24 | channel_type_name | varchar(255) | YES | 通道子类型说明 |
| 40 | competent_unit | varchar(255) | YES | 主管单位（新增字段） |
| 85 | coord_govern_type | int | YES | 1：人工精细化治理、2：高德坐标反查、null：未作处理 |
| 47 | create_time | varchar(255) | YES | 创建时间 |
| 52 | dept_id | varchar(50) | YES | 部门id |
| 45 | describe | varchar(255) | YES | 设备描述（新增字段） |
| 12 | device_index_code | varchar(255) | YES | 所属设备编号（通用唯一识别码UUID） |
| 13 | device_resource_type | varchar(255) | YES | 所属设备类型 |
| 14 | device_resource_type_name | varchar(255) | YES | 所属设备类型说明 |
| 77 | external_camera_id | varchar(255) | YES | 三方设备id |
| 80 | floor_id | varchar(40) | YES | 楼层id |
| 29 | gb_index_code | varchar(255) | YES | 监控点国标编号 |
| 50 | has_lock | smallint | YES | 是否锁定 0未锁定 1锁定 |
| 46 | hasdel | int | YES | 删除状态 |
| 72 | hik_lat | double | YES | 海康原始纬度 |
| 71 | hik_lng | double | YES | 海康原始经度 |
| 75 | horizontal | double | YES | 水平视角 |
| 1 | id | int | NO | 主键 |
| 73 | img_url | varchar(100) | YES | 设备缩略图 |
| 10 | install_place | varchar(255) | YES | 安装位置 |
| 19 | intelligent_set | varchar(255) | YES | 智能分析能力集 |
| 34 | intelligent_set_name | varchar(255) | YES | 智能分析能力集说明 |
| 6 | latitude | double | YES | 纬度 |
| 57 | level | int | YES | 锁定设备的用户级别 |
| 58 | lock_account | varchar(50) | YES | 锁定用户 |
| 59 | lock_camera_time | int | YES | 锁定时间  分 |
| 51 | lock_time | datetime | YES | 最后调整视角时间 |
| 5 | longitude | double | YES | 经度 |
| 42 | maintenance_unit | varchar(255) | YES | 维护单位（新增字段） |
| 28 | matrix_code | varchar(255) | YES | 矩阵编号 |
| 3 | name | varchar(255) | YES | 监控点名称 |
| 84 | one_screen | int | YES | 是否为一屏多播设备 1是0否 |
| 56 | org_id | varchar(50) | YES | 组织id |
| 41 | ownership_unit | varchar(255) | YES | 权属单位（新增字段） |
| 53 | pan_pos | double | YES | 角度信息:P参数（水平参数） |
| 43 | person_liable | varchar(255) | YES | 责任人（新增字段） |
| 44 | person_liable_phone | varchar(255) | YES | 责任人联系电话（新增字段） |
| 26 | pixel | int | YES | 摄像机像素（1-普通像素，2-130万高清，3-200万高清，4-300万高清，取值参考数据字典，typeCode为xresmgr.piexl） |
| 30 | ptz_controller | varchar(255) | YES | 云台控制说明 |
| 17 | ptz_controller_name | varchar(255) | YES | 云台控制说明 |
| 18 | record_location | varchar(255) | YES | 录像存储位置（0-中心存储，1-设备存储，取值参考数据字典，typeCode为xresmgr.record_location） |
| 22 | record_location_name | varchar(255) | YES | 录像存储位置说明 |
| 49 | region_index_code | varchar(255) | YES | 行政区划逻辑id |
| 37 | scene_id | varchar(100) | YES | 高点编号id |
| 38 | scene_index_code | varchar(100) | YES | 高点id |
| 78 | source_type | smallint | YES | 平台类型：10-海康IOT、ISC、PVIA    11-海康8200    20-大华    30-宇视（暂无、预留）    40-紫光（暂无、预留）    50-芯翌    60-东方电子 |
| 83 | state | int | YES | 状态（0=待撒点；1=已撒点） |
| 39 | status | int | YES | 在线状态（0-不在线，1-在线，取值参考数据字典，typeCode为xresmgr.status） |
| 21 | status_name | varchar(255) | YES | 状态说明 |
| 54 | tilt_pos | double | YES | 角度信息:T参数（垂直参数） |
| 35 | trans_type | int | YES | 传输协议（0-UDP，1-TCP） |
| 25 | trans_type_name | varchar(255) | YES | 传输协议类型说明 |
| 32 | treaty_type | varchar(255) | YES | 接入协议（详见数据字典，typeCode为xresmgr.protocol_type） |
| 23 | treaty_type_name | varchar(255) | YES | 接入协议类型说明 |
| 7 | type | int | YES | 设备类型：0—枪机、1---高空瞭望、2---鹰眼、3---球机 |
| 33 | unit_index_code | varchar(255) | YES | 所属组织编号（通用唯一识别码UUID） |
| 48 | update_time | varchar(255) | YES | 更新时间 采用ISO8601标准，如2018-07-26T21:30:08+08:00 表示北京时间2017年7月26日21时30分08秒 |
| 76 | vertical | double | YES | 垂直视角 |
| 16 | viewshed | varchar(255) | YES | 可视域相关 |



### hkcy_camera_equipment_info_202409062011 (摄像设备信息表) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 60 | ad_logic_id | varchar(64) | YES | 所属行政区划（智广）。已作废，当前区划用auth_field_1-10维护 |
| 82 | ad_logic_id_fill_status | int | YES | ad_logic_id填充状态： 0手动填充 1自动填充成功 2自动填充失败 |
| 4 | altitude | double | YES | 海拔 |
| 61 | auth_field_1 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 70 | auth_field_10 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 62 | auth_field_2 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 63 | auth_field_3 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 64 | auth_field_4 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 65 | auth_field_5 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 66 | auth_field_6 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 67 | auth_field_7 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 68 | auth_field_8 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 69 | auth_field_9 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 74 | calibration | text | YES | 相机标定信息 |
| 81 | calibration_union | text | YES | 全景球机联合标定信息 |
| 9 | camera_height | double | YES | 摄像头可视域高度 |
| 79 | camera_height_type | int | YES | 1---低空设备（普通低空球机、枪机） 2---高空设备（如鹰眼、鹰眼球机、瞭望等） |
| 2 | camera_index_code | varchar(100) | YES | 监控点唯一标识 |
| 8 | camera_radius | double | YES | 摄像头可视域半径 |
| 55 | camera_resolution | varchar(255) | YES | 设备视频分辨率 |
| 31 | camera_type | int | YES | 监控点类型0-枪机,1-半球,2-快球,3-带云台枪机 |
| 20 | camera_type_name | varchar(255) | YES | 监控点类型说明 |
| 36 | capability_set | text | YES | 能力集（详见数据字典，typeCode为xresmgr.capability_set） |
| 11 | capability_set_name | text | YES | 能力集说明 |
| 27 | chan_num | int | YES | 通道号 |
| 15 | channel_type | varchar(255) | YES | 通道类型 |
| 24 | channel_type_name | varchar(255) | YES | 通道子类型说明 |
| 40 | competent_unit | varchar(255) | YES | 主管单位（新增字段） |
| 85 | coord_govern_type | int | YES | 1：人工精细化治理、2：高德坐标反查、null：未作处理 |
| 47 | create_time | varchar(255) | YES | 创建时间 |
| 52 | dept_id | varchar(50) | YES | 部门id |
| 45 | describe | varchar(255) | YES | 设备描述（新增字段） |
| 12 | device_index_code | varchar(255) | YES | 所属设备编号（通用唯一识别码UUID） |
| 13 | device_resource_type | varchar(255) | YES | 所属设备类型 |
| 14 | device_resource_type_name | varchar(255) | YES | 所属设备类型说明 |
| 77 | external_camera_id | varchar(255) | YES | 三方设备id |
| 80 | floor_id | varchar(40) | YES | 楼层id |
| 29 | gb_index_code | varchar(255) | YES | 监控点国标编号 |
| 50 | has_lock | smallint | YES | 是否锁定 0未锁定 1锁定 |
| 46 | hasdel | int | YES | 删除状态 |
| 72 | hik_lat | double | YES | 海康原始纬度 |
| 71 | hik_lng | double | YES | 海康原始经度 |
| 75 | horizontal | double | YES | 水平视角 |
| 1 | id | int | NO | 主键 |
| 73 | img_url | varchar(100) | YES | 设备缩略图 |
| 10 | install_place | varchar(255) | YES | 安装位置 |
| 19 | intelligent_set | varchar(255) | YES | 智能分析能力集 |
| 34 | intelligent_set_name | varchar(255) | YES | 智能分析能力集说明 |
| 6 | latitude | double | YES | 纬度 |
| 57 | level | int | YES | 锁定设备的用户级别 |
| 58 | lock_account | varchar(50) | YES | 锁定用户 |
| 59 | lock_camera_time | int | YES | 锁定时间  分 |
| 51 | lock_time | datetime | YES | 最后调整视角时间 |
| 5 | longitude | double | YES | 经度 |
| 42 | maintenance_unit | varchar(255) | YES | 维护单位（新增字段） |
| 28 | matrix_code | varchar(255) | YES | 矩阵编号 |
| 3 | name | varchar(255) | YES | 监控点名称 |
| 84 | one_screen | int | YES | 是否为一屏多播设备 1是0否 |
| 56 | org_id | varchar(50) | YES | 组织id |
| 41 | ownership_unit | varchar(255) | YES | 权属单位（新增字段） |
| 53 | pan_pos | double | YES | 角度信息:P参数（水平参数） |
| 43 | person_liable | varchar(255) | YES | 责任人（新增字段） |
| 44 | person_liable_phone | varchar(255) | YES | 责任人联系电话（新增字段） |
| 26 | pixel | int | YES | 摄像机像素（1-普通像素，2-130万高清，3-200万高清，4-300万高清，取值参考数据字典，typeCode为xresmgr.piexl） |
| 30 | ptz_controller | varchar(255) | YES | 云台控制说明 |
| 17 | ptz_controller_name | varchar(255) | YES | 云台控制说明 |
| 18 | record_location | varchar(255) | YES | 录像存储位置（0-中心存储，1-设备存储，取值参考数据字典，typeCode为xresmgr.record_location） |
| 22 | record_location_name | varchar(255) | YES | 录像存储位置说明 |
| 49 | region_index_code | varchar(255) | YES | 行政区划逻辑id |
| 37 | scene_id | varchar(100) | YES | 高点编号id |
| 38 | scene_index_code | varchar(100) | YES | 高点id |
| 78 | source_type | smallint | YES | 平台类型：10-海康IOT、ISC、PVIA    11-海康8200    20-大华    30-宇视（暂无、预留）    40-紫光（暂无、预留）    50-芯翌    60-东方电子 |
| 83 | state | int | YES | 状态（0=待撒点；1=已撒点） |
| 39 | status | int | YES | 在线状态（0-不在线，1-在线，取值参考数据字典，typeCode为xresmgr.status） |
| 21 | status_name | varchar(255) | YES | 状态说明 |
| 54 | tilt_pos | double | YES | 角度信息:T参数（垂直参数） |
| 35 | trans_type | int | YES | 传输协议（0-UDP，1-TCP） |
| 25 | trans_type_name | varchar(255) | YES | 传输协议类型说明 |
| 32 | treaty_type | varchar(255) | YES | 接入协议（详见数据字典，typeCode为xresmgr.protocol_type） |
| 23 | treaty_type_name | varchar(255) | YES | 接入协议类型说明 |
| 7 | type | int | YES | 设备类型：0—枪机、1---高空瞭望、2---鹰眼、3---球机 |
| 33 | unit_index_code | varchar(255) | YES | 所属组织编号（通用唯一识别码UUID） |
| 48 | update_time | varchar(255) | YES | 更新时间 采用ISO8601标准，如2018-07-26T21:30:08+08:00 表示北京时间2017年7月26日21时30分08秒 |
| 76 | vertical | double | YES | 垂直视角 |
| 16 | viewshed | varchar(255) | YES | 可视域相关 |



### hkcy_camera_equipment_info_copy1 (摄像设备信息表) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 60 | ad_logic_id | varchar(64) | YES | 所属行政区划（智广）。已作废，当前区划用auth_field_1-10维护 |
| 82 | ad_logic_id_fill_status | int | YES | ad_logic_id填充状态： 0手动填充 1自动填充成功 2自动填充失败 |
| 4 | altitude | double | YES | 海拔 |
| 61 | auth_field_1 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 70 | auth_field_10 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 62 | auth_field_2 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 63 | auth_field_3 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 64 | auth_field_4 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 65 | auth_field_5 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 66 | auth_field_6 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 67 | auth_field_7 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 68 | auth_field_8 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 69 | auth_field_9 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 74 | calibration | text | YES | 相机标定信息 |
| 81 | calibration_union | text | YES | 全景球机联合标定信息 |
| 9 | camera_height | double | YES | 摄像头可视域高度 |
| 79 | camera_height_type | int | YES |  |
| 2 | camera_index_code | varchar(100) | YES | 监控点唯一标识 |
| 8 | camera_radius | double | YES | 摄像头可视域半径 |
| 55 | camera_resolution | varchar(255) | YES | 设备视频分辨率 |
| 31 | camera_type | int | YES | 监控点类型0-枪机,1-半球,2-快球,3-带云台枪机 |
| 20 | camera_type_name | varchar(255) | YES | 监控点类型说明 |
| 36 | capability_set | text | YES | 能力集（详见数据字典，typeCode为xresmgr.capability_set） |
| 11 | capability_set_name | text | YES | 能力集说明 |
| 27 | chan_num | int | YES | 通道号 |
| 15 | channel_type | varchar(255) | YES | 通道类型 |
| 24 | channel_type_name | varchar(255) | YES | 通道子类型说明 |
| 40 | competent_unit | varchar(255) | YES | 主管单位（新增字段） |
| 85 | coord_govern_type | int | YES | 1：人工精细化治理、2：高德坐标反查、null：未作处理 |
| 47 | create_time | varchar(255) | YES | 创建时间 |
| 52 | dept_id | varchar(50) | YES | 部门id |
| 45 | describe | varchar(255) | YES | 设备描述（新增字段） |
| 12 | device_index_code | varchar(255) | YES | 所属设备编号（通用唯一识别码UUID） |
| 13 | device_resource_type | varchar(255) | YES | 所属设备类型 |
| 14 | device_resource_type_name | varchar(255) | YES | 所属设备类型说明 |
| 77 | external_camera_id | varchar(255) | YES | 三方设备id |
| 80 | floor_id | varchar(40) | YES | 楼层id |
| 29 | gb_index_code | varchar(255) | YES | 监控点国标编号 |
| 50 | has_lock | smallint | YES | 是否锁定 0未锁定 1锁定 |
| 46 | hasdel | int | YES | 删除状态 |
| 72 | hik_lat | double | YES | 海康原始纬度 |
| 71 | hik_lng | double | YES | 海康原始经度 |
| 75 | horizontal | double | YES | 水平视角 |
| 1 | id | int | NO | 主键 |
| 73 | img_url | varchar(100) | YES | 设备缩略图 |
| 10 | install_place | varchar(255) | YES | 安装位置 |
| 19 | intelligent_set | varchar(255) | YES | 智能分析能力集 |
| 34 | intelligent_set_name | varchar(255) | YES | 智能分析能力集说明 |
| 6 | latitude | double | YES | 纬度 |
| 57 | level | int | YES | 锁定设备的用户级别 |
| 58 | lock_account | varchar(50) | YES | 锁定用户 |
| 59 | lock_camera_time | int | YES | 锁定时间  分 |
| 51 | lock_time | datetime | YES | 最后调整视角时间 |
| 5 | longitude | double | YES | 经度 |
| 42 | maintenance_unit | varchar(255) | YES | 维护单位（新增字段） |
| 28 | matrix_code | varchar(255) | YES | 矩阵编号 |
| 3 | name | varchar(255) | YES | 监控点名称 |
| 84 | one_screen | int | YES | 是否为一屏多播设备 1是0否 |
| 56 | org_id | varchar(50) | YES | 组织id |
| 41 | ownership_unit | varchar(255) | YES | 权属单位（新增字段） |
| 53 | pan_pos | double | YES | 角度信息:P参数（水平参数） |
| 43 | person_liable | varchar(255) | YES | 责任人（新增字段） |
| 44 | person_liable_phone | varchar(255) | YES | 责任人联系电话（新增字段） |
| 26 | pixel | int | YES | 摄像机像素（1-普通像素，2-130万高清，3-200万高清，4-300万高清，取值参考数据字典，typeCode为xresmgr.piexl） |
| 30 | ptz_controller | varchar(255) | YES | 云台控制说明 |
| 17 | ptz_controller_name | varchar(255) | YES | 云台控制说明 |
| 18 | record_location | varchar(255) | YES | 录像存储位置（0-中心存储，1-设备存储，取值参考数据字典，typeCode为xresmgr.record_location） |
| 22 | record_location_name | varchar(255) | YES | 录像存储位置说明 |
| 49 | region_index_code | varchar(255) | YES | 行政区划逻辑id |
| 37 | scene_id | varchar(100) | YES | 高点编号id |
| 38 | scene_index_code | varchar(100) | YES | 高点id |
| 78 | source_type | smallint | YES | 平台类型：10-海康IOT、ISC、PVIA    11-海康8200    20-大华    30-宇视（暂无、预留）    40-紫光（暂无、预留）    50-芯翌    60-东方电子 |
| 83 | state | int | YES | 状态（0=待撒点；1=已撒点） |
| 39 | status | int | YES | 在线状态（0-不在线，1-在线，取值参考数据字典，typeCode为xresmgr.status） |
| 21 | status_name | varchar(255) | YES | 状态说明 |
| 54 | tilt_pos | double | YES | 角度信息:T参数（垂直参数） |
| 35 | trans_type | int | YES | 传输协议（0-UDP，1-TCP） |
| 25 | trans_type_name | varchar(255) | YES | 传输协议类型说明 |
| 32 | treaty_type | varchar(255) | YES | 接入协议（详见数据字典，typeCode为xresmgr.protocol_type） |
| 23 | treaty_type_name | varchar(255) | YES | 接入协议类型说明 |
| 7 | type | int | YES | 设备类型：0—枪机、1---高空瞭望、2---鹰眼、3---球机 |
| 33 | unit_index_code | varchar(255) | YES | 所属组织编号（通用唯一识别码UUID） |
| 48 | update_time | varchar(255) | YES | 更新时间 采用ISO8601标准，如2018-07-26T21:30:08+08:00 表示北京时间2017年7月26日21时30分08秒 |
| 76 | vertical | double | YES | 垂直视角 |
| 16 | viewshed | varchar(255) | YES | 可视域相关 |



### hkcy_camera_equipment_info_expand (摄像设备信息拓展表) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 4 | camera_account | varchar(50) | YES | 设备用户名 |
| 6 | camera_brand | int | YES | 品牌类型：1-海康  2-大华  3-宇视  4-紫光  5-芯翌  6-东方电子 |
| 13 | camera_channel_id | int | YES | 渠道id |
| 1 | camera_index_code | varchar(100) | NO | 监控点唯一标识 |
| 2 | camera_ip | varchar(20) | YES | 设备ip |
| 7 | camera_model | varchar(50) | YES | 设备型号 |
| 9 | camera_panel_interface | int | YES | 云台控制类型：0-设备直连    10-海康IOT、ISC、PVIA    11-海康8200    20-大华    30-宇视（暂无、预留）    40-紫光（暂无、预留）    50-芯翌    60-东方电子 |
| 3 | camera_port | varchar(10) | YES | 设备端口 |
| 8 | camera_ptz_interface | int | YES | PTZ类型：0-设备直连    1-插件    10-海康IOT、ISC、PVIA    11-海康8200    20-大华    30-宇视（暂无、预留）    40-紫光（暂无、预留）    50-芯翌    60-东方电子 |
| 5 | camera_pw | varchar(50) | YES | 设备密码 |
| 10 | camera_stream_interface | int | YES | 取流类型：0-设备直连    10-海康IOT、ISC、PVIA    11-海康8200    20-大华    30-宇视（暂无、预留）    40-紫光（暂无、预留）    50-芯翌    60-东方电子 |
| 11 | camera_stream_port | varchar(50) | YES | RTSP视频流播放端口，拼接流用 |
| 12 | camera_stream_type | int | YES | 海康码流：0 ，主码流；1，子码流 ；宇视码流：1 ，主码流；2，子码流； 紫光码流：0-主码流 1-子码流 2-三码流 |
| 15 | camera_stream_type_h5 | int | YES | H5码流类型 |
| 14 | need_transform_ptz | smallint | YES | 是否需要对ptz做转换。0：不需要；1：需要。默认0 |



### hkcy_camera_equipment_tag (设备标签关系表) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | camera_id | varchar(40) | YES | 设备编号 |
| 5 | create_time | datetime | YES | 创建时间 |
| 4 | create_user | varchar(100) | YES | 创建者账号 |
| 1 | id | int | NO |  |
| 3 | tag_code | varchar(40) | YES | 标签编号 |



### hkcy_camera_permission (设备权限表) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 15 | camera_equipment_alias | varchar(255) | YES | 监控设备别名 |
| 4 | camera_index_code | varchar(255) | YES | 设备编号 |
| 12 | create_time | datetime | YES | 创建时间 |
| 11 | create_user | varchar(255) | YES | 创建者账号 |
| 2 | dept_id | varchar(255) | YES | 部门id |
| 3 | dept_name | varchar(255) | YES |  |
| 9 | has_del | smallint | YES | 是否删除 |
| 1 | id | int | NO |  |
| 7 | level | int | YES | 权限等级 |
| 6 | operate_permission | int | YES | 操作权限 0:有操作权限 1:无操作权限 |
| 8 | org_id | varchar(50) | YES | 所属组织 |
| 10 | remark | varchar(255) | YES | 备注 |
| 14 | update_time | datetime | YES | 更新时间 |
| 13 | update_user | varchar(255) | YES | 更新者账号 |
| 5 | view_permission | int | YES | 查看权限 0:有查看权限 1:无查看权限 |



### hkcy_camera_user_source (监控设备用户评分) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 4 | camera_index_code | varchar(100) | YES | 监控点唯一标识 |
| 8 | create_time | datetime | YES | 创建时间 |
| 6 | evaluations_num | int | YES | 评价数量 |
| 1 | id | int | NO |  |
| 5 | score | double | YES | 评价平均分数 |
| 9 | score_latest | double | YES | 最新分数 |
| 7 | total_score | int | YES | 评价累加总分 |
| 2 | user_id | varchar(255) | YES | 用户id |
| 3 | user_name | varchar(255) | YES | 用户名称 |



### hkcy_camera_visual_angle (视角信息) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 4 | camera_id | varchar(50) | YES | 设备id |
| 16 | create_time | datetime | YES | 创建时间 |
| 15 | create_user | varchar(100) | YES | 创建者账号 |
| 12 | dept_id | varchar(50) | YES | 所属部门 |
| 13 | has_del | smallint | YES | 是否删除 |
| 1 | id | int | NO |  |
| 10 | img_url | varchar(100) | YES | 视角截图 |
| 6 | latitude | double | YES | 纬度 |
| 5 | longitude | double | YES | 经度 |
| 11 | org_id | varchar(50) | YES | 所属组织 |
| 7 | pan_pos | double | YES | 角度信息:P参数（水平参数） |
| 14 | remark | varchar(200) | YES | 备注 |
| 19 | status | smallint | YES | 是否相似强制提交 0不是 1是 |
| 8 | tilt_pos | double | YES | 角度信息:T参数（垂直参数） |
| 18 | update_time | datetime | YES | 更新时间 |
| 17 | update_user | varchar(100) | YES | 更新者账号 |
| 2 | visual_angle_id | varchar(50) | YES | 视角id |
| 3 | visual_angle_name | varchar(100) | YES | 视角名称 |
| 9 | zoom_pos | double | YES | 角度信息:Z参数（变倍参数） |



### hkcy_camera_visual_angle_alias (视角别名) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 9 | create_time | datetime | YES | 创建时间 |
| 8 | create_user | varchar(100) | YES | 创建者账号 |
| 5 | dept_id | varchar(50) | YES | 所属部门 |
| 6 | has_del | smallint | YES | 是否删除 |
| 1 | id | int | NO |  |
| 4 | org_id | varchar(50) | YES | 所属组织 |
| 7 | remark | varchar(200) | YES | 备注 |
| 11 | update_time | datetime | YES | 更新时间 |
| 10 | update_user | varchar(100) | YES | 更新者账号 |
| 3 | visual_angle_alias | varchar(100) | YES | 视角别名 |
| 2 | visual_angle_id | varchar(50) | YES | 视角id |



### hkcy_camera_visual_angle_tag (视角标签) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 10 | create_time | datetime | YES | 创建时间 |
| 9 | create_user | varchar(100) | YES | 创建者账号 |
| 6 | dept_id | varchar(50) | YES | 所属部门 |
| 7 | has_del | smallint | YES | 是否删除 |
| 1 | id | int | NO |  |
| 5 | org_id | varchar(50) | YES | 所属组织 |
| 8 | remark | varchar(200) | YES | 备注 |
| 3 | tag_id | varchar(50) | YES | 标签id |
| 4 | tag_name | varchar(100) | YES | 标签名称 |
| 12 | update_time | datetime | YES | 更新时间 |
| 11 | update_user | varchar(100) | YES | 更新者账号 |
| 2 | visual_angle_id | varchar(50) | YES | 视角id |



### hkcy_custom_scene (场景表) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 8 | create_time | datetime | YES | 创建时间 |
| 7 | create_user | varchar(100) | YES | 创建者账号 |
| 6 | description | varchar(500) | YES | 场景描述 |
| 11 | electronic_fence | text | YES | 自定义电子围栏 |
| 5 | has_del | smallint | YES | 是否删除 |
| 1 | id | int | NO |  |
| 12 | management_dept_name | varchar(255) | YES | 管理部门 |
| 4 | region_id | varchar(20) | YES | 行政区划 |
| 2 | scene_id | varchar(50) | YES | 场景ID |
| 3 | scene_name | varchar(100) | YES | 场景名称 |
| 10 | update_time | datetime | YES | 更新时间 |
| 9 | update_user | varchar(100) | YES | 更新者账号 |



### hkcy_custom_scene_camera (场景与设备关系表) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 3 | camera_id | varchar(50) | YES | 设备id |
| 7 | create_time | datetime | YES | 创建时间 |
| 6 | create_user | varchar(100) | YES | 创建者账号 |
| 4 | has_del | smallint | YES | 是否删除 |
| 1 | id | int | NO |  |
| 10 | order | int | YES | 排序 |
| 5 | remark | varchar(200) | YES | 备注 |
| 2 | scene_id | varchar(50) | YES | 场景ID |
| 9 | update_time | datetime | YES | 更新时间 |
| 8 | update_user | varchar(100) | YES | 更新者账号 |



### hkcy_custom_scene_reserve_plan (场景与预案关系表) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 7 | create_time | datetime | YES | 创建时间 |
| 6 | create_user | varchar(100) | YES | 创建者账号 |
| 4 | has_del | smallint | YES | 是否删除 |
| 1 | id | int | NO |  |
| 5 | remark | varchar(200) | YES | 备注 |
| 2 | reserve_plan_id | varchar(50) | YES | 视频预案ID或cms图文id |
| 3 | reserve_plan_type | int | YES | 1视频预案2图文预案（cms） |
| 9 | update_time | datetime | YES | 更新时间 |
| 8 | update_user | varchar(100) | YES | 更新者账号 |



### hkcy_custom_scene_tag_type (场景标签类型关系表) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 7 | create_time | datetime | YES | 创建时间 |
| 6 | create_user | varchar(100) | YES | 创建者账号 |
| 5 | has_del | smallint | YES | 是否删除 |
| 1 | id | int | NO |  |
| 3 | label_big_type | varchar(20) | YES | 标签大类 |
| 4 | label_small_type | varchar(20) | YES | 标签小类 |
| 2 | scene_id | varchar(40) | YES | 设备编号 |
| 9 | update_time | datetime | YES | 更新时间 |
| 8 | update_user | varchar(100) | YES | 更新者账号 |



### hkcy_custom_scene_tag_type_tab_info (场景标签类型tab页关系表) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 7 | create_time | datetime | YES | 创建时间 |
| 6 | create_user | varchar(100) | YES | 创建者账号 |
| 5 | has_del | smallint | YES | 是否删除 |
| 1 | id | int | NO |  |
| 2 | scene_tag_type_id | int | YES | 场景类型表id |
| 3 | tab_name | varchar(20) | YES | 标签大类 |
| 4 | tab_url | varchar(20) | YES | 标签小类 |
| 9 | update_time | datetime | YES | 更新时间 |
| 8 | update_user | varchar(100) | YES | 更新者账号 |



### hkcy_dict (字典表) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | data_name | varchar(255) | YES | 类型名称 |
| 4 | data_type | varchar(100) | YES | 字典类型 |
| 3 | data_value | varchar(45) | YES | 类型值 |
| 5 | has_del | int | YES | 0正常 1删除 |
| 1 | id | int | NO |  |
| 7 | remark | varchar(255) | YES | 备注 |
| 6 | sort | int | YES | 排序 |



### hkcy_division (行政区域) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 19 | auth_field | varchar(20) | YES | 区域类型字段 |
| 12 | create_time | datetime | YES | 创建时间 |
| 11 | create_user | varchar(45) | YES | 创建人  |
| 15 | electronic_fence | longtext | YES | 行政区划电子围栏 |
| 16 | electronic_map | varchar(50) | YES | 电子地图地址 |
| 9 | has_del | smallint | YES | 0未删除 1 删除 |
| 1 | id | bigint | NO | 主键 |
| 20 | is_leaf | int | YES | 是否叶子节点（最后一级）1-是，0-否 |
| 6 | latitude | varchar(255) | NO | 纬度 |
| 7 | level | int | YES | 层级 |
| 5 | longitude | varchar(255) | NO | 经度 |
| 4 | merger_name | varchar(100) | YES | 全路径名称 |
| 10 | order_num | int | YES | 排序 |
| 17 | org_logic_id | varchar(100) | YES | 所属平台组织 新增时填入当前用户组织 |
| 8 | parent_id | varchar(45) | YES | 父节点 |
| 2 | region_id | varchar(45) | YES | 区域id |
| 3 | region_name | varchar(45) | YES | 区域名称 |
| 18 | region_status | int | YES | 区域状态 1启用 0禁用 |
| 14 | update_time | datetime | YES | 更新时间 |
| 13 | update_user | varchar(45) | YES | 更新时间 |



### hkcy_dynamic_trajectory (动态轨迹) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 6 | camera_group | varchar(20) | YES | 设备组 |
| 4 | camera_id | varchar(50) | YES | 设备编号 |
| 5 | camera_position | varchar(20) | YES | 设备位置 |
| 8 | capture_time | datetime | YES | 拍摄时间 |
| 2 | car_id | varchar(255) | YES |  |
| 3 | car_num | varchar(50) | YES | 车次 |
| 20 | create_time | datetime | YES | 创建时间 |
| 19 | create_user | varchar(100) | YES | 创建者账号 |
| 16 | dept_id | varchar(50) | YES | 所属部门 |
| 17 | has_del | smallint | YES | 是否删除 |
| 1 | id | int | NO |  |
| 7 | img_url | varchar(100) | YES | 图片地址 |
| 13 | label_type_logic_id | varchar(100) | YES | 标签类型ID |
| 10 | latitude | double | YES | 纬度 |
| 9 | longitude | double | YES | 经度 |
| 12 | order_num | int | YES | 顺序 |
| 15 | org_id | varchar(50) | YES | 所属组织 |
| 14 | region_id | varchar(50) | YES | 区划ID |
| 18 | remark | varchar(200) | YES | 备注 |
| 11 | trajectory_id | varchar(50) | YES | 轨迹ID |
| 22 | update_time | datetime | YES | 更新时间 |
| 21 | update_user | varchar(100) | YES | 更新者账号 |



### hkcy_file (文件表) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 11 | create_time | datetime | YES | 创建时间 |
| 10 | create_user | varchar(32) | YES | 创建人 |
| 5 | file_id | varchar(255) | YES | 文件逻辑ID |
| 6 | group_dir | varchar(255) | YES | 目录 |
| 8 | has_del | int | YES | 是否删除 0正常 1删除 |
| 1 | id | int | NO | 文件ID |
| 2 | name | varchar(50) | YES | 文件名称 |
| 3 | new_name | varchar(100) | YES | 新文件(服务器)名称 |
| 9 | REMARK | text | YES | 备注 |
| 7 | status | int | YES | 状态 0正常 1禁用 |
| 13 | update_time | datetime | YES | 更新时间 |
| 12 | update_user | varchar(32) | YES | 更新人 |
| 4 | url | varchar(255) | YES | 文件地址 |



### hkcy_fire_behavior (火灾预警) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 10 | address | varchar(100) | YES | 地址 |
| 43 | auth_field_1 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 34 | auth_field_10 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 42 | auth_field_2 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 41 | auth_field_3 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 40 | auth_field_4 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 39 | auth_field_5 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 38 | auth_field_6 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 37 | auth_field_7 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 36 | auth_field_8 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 35 | auth_field_9 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 6 | clue | int | YES | 线索类型 |
| 7 | clue_name | varchar(45) | YES | 线索类型名称 |
| 12 | community_center_phone | varchar(45) | YES | 社区中心电话 |
| 24 | create_time | varchar(45) | YES | 创建时间 |
| 23 | creater | varchar(45) | YES | 创建人 |
| 20 | detail_url | varchar(150) | YES | 链接地址 |
| 18 | device_id | varchar(45) | YES | 设备id |
| 17 | event_detail | text | YES | 事件详情 |
| 16 | event_name | varchar(45) | YES | 事件名称 |
| 13 | fire_alarm_phone | varchar(45) | YES | 火警电话 |
| 22 | has_del | smallint | YES | 0正常 1删除 |
| 1 | id | int | NO |  |
| 28 | img_url | varchar(100) | YES | icon图片 |
| 5 | information_source | varchar(100) | YES | 信息来源 |
| 31 | label_type_logic_id | varchar(100) | YES | 标签类型ID |
| 15 | latitude | varchar(45) | YES | 纬度 |
| 2 | logic_id | varchar(100) | YES | 逻辑id |
| 14 | longitude | varchar(45) | YES | 经度 |
| 33 | org_id | varchar(100) | YES | 组织id |
| 30 | pic_url | varchar(500) | YES |  |
| 11 | police_station_phone | varchar(45) | YES | 派出所电话 |
| 19 | related_aR | text | YES | 设备AR |
| 27 | remark | longtext | YES | 备注 |
| 32 | shot_camera_id | varchar(100) | YES | 识别该事件的相机id |
| 29 | show_status | int | YES | 是否显示 0显示 1不显示 |
| 4 | size_list | varchar(100) | YES | 大小数组 |
| 21 | status | int | YES | 开关 0 ON 1 OFF |
| 9 | tag_id | int | YES | 标签id |
| 3 | type_name | varchar(45) | YES | 预警类型名称 |
| 26 | update_time | varchar(45) | YES | 修改时间 |
| 25 | updater | varchar(45) | YES | 修改人 |
| 8 | warning_time | varchar(45) | YES | 预警发生时间 |



### hkcy_floor_info (机场楼层) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 17 | build_id | varchar(40) | YES | 建筑id |
| 16 | build_name | varchar(100) | YES | 建筑名称 |
| 21 | central_distance | int | YES | 可视域中心店到建筑物中心点默认值 |
| 10 | create_time | datetime | YES |  |
| 9 | create_user | varchar(20) | YES |  |
| 13 | electronic_fence | longtext | YES | 电子围栏 |
| 18 | extent | varchar(255) | YES | 建筑图片定位 |
| 2 | floor_id | varchar(40) | YES | 楼层id |
| 3 | floor_name | varchar(100) | YES | 楼层名称 |
| 8 | has_del | smallint | YES | 逻辑删除 |
| 20 | height | int | YES | 建筑图片高 |
| 1 | id | int | NO | 主键 |
| 7 | img_url | varchar(100) | YES | 图片url |
| 14 | is_default | int | YES | 是否默认楼层：0否，1是 |
| 6 | latitude | double | YES | 纬度 |
| 5 | longitude | double | YES | 经度 |
| 15 | order_num | int | YES | 排序 |
| 4 | region_id | varchar(40) | YES | 所属区域编码 |
| 12 | update_time | datetime | YES |  |
| 11 | update_user | varchar(20) | YES |  |
| 19 | width | int | YES | 建筑图片宽 |



### hkcy_incident_info (事件列表) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 7 | address | varchar(255) | YES | 地址 |
| 13 | basic_information | text | YES | 标签基本信息 |
| 15 | create_time | varchar(100) | YES | 创建时间 |
| 16 | creater | varchar(50) | YES | 创建人 |
| 12 | external_label_id | varchar(255) | YES | 外来的标签ID |
| 14 | has_del | int | YES | 0非 1删 |
| 1 | id | int | NO |  |
| 5 | latitude | double | YES | 纬度 |
| 2 | logic_id | varchar(255) | YES | 编号 |
| 6 | longandlat | varchar(255) | YES |  |
| 4 | longitude | double | YES | 经度 |
| 3 | name | varchar(255) | YES | 名称 |
| 9 | source_id | int | YES | 来源id |
| 8 | source_name | varchar(255) | YES | 来源名称 |
| 11 | type_id | varchar(255) | YES | 类型id |
| 10 | type_name | varchar(255) | YES | 类型名称 |
| 18 | update_time | varchar(100) | YES | 修改人 |
| 17 | updater | varchar(50) | YES | 修改时间 |



### hkcy_label_camera (相机关联的标签) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 21 | ad_code | varchar(50) | YES | 行政区划编码 |
| 22 | auth_field_1 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 31 | auth_field_10 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 23 | auth_field_2 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 24 | auth_field_3 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 25 | auth_field_4 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 26 | auth_field_5 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 27 | auth_field_6 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 28 | auth_field_7 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 29 | auth_field_8 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 30 | auth_field_9 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 4 | camera_index_code | varchar(255) | NO | 相机编号 |
| 14 | camera_type | int | YES | 相机类型 |
| 10 | create_time | datetime | YES | 创建时间 |
| 11 | creater | varchar(255) | YES | 创建者 |
| 18 | distance | double | YES | 标签与相机距离 |
| 5 | draw_type | tinyint | YES | 上图类型：1=自动打标，2=矢量绘制 |
| 19 | external_label_id | varchar(255) | YES | 外来的标签ID |
| 8 | global_x | double | YES | 角度坐标 |
| 9 | global_y | double | YES | 角度坐标 |
| 1 | id | bigint | NO |  |
| 17 | label_address | varchar(255) | YES | 标签地址 |
| 2 | label_logic_id | varchar(255) | NO | 标签编号 |
| 3 | label_name | varchar(255) | YES |  |
| 20 | label_type_logic_id | varchar(100) | YES | 标签类型ID |
| 16 | latitude | double | YES | 标签纬度 |
| 15 | longitude | double | YES | 标签经度 |
| 6 | pixel_x | double | YES | 像素坐标 |
| 7 | pixel_y | double | YES | 像素坐标 |
| 12 | update_time | datetime | YES | 更新时间 |
| 13 | updater | varchar(255) | YES | 更新者 |



### hkcy_map_info (上海poi记录) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 14 | ad_code | varchar(50) | YES | 区域编码 |
| 15 | ad_name | varchar(255) | YES | 区域名称 |
| 4 | address | varchar(500) | YES | 地址 |
| 20 | bd_latitude | double | YES | bd02坐标系-纬度 |
| 19 | bd_longitude | double | YES | bd02坐标系-经度 |
| 12 | city_code | varchar(50) | YES | 城市编码 |
| 13 | city_name | varchar(255) | YES | 城市名 |
| 21 | create_time | timestamp | YES | 创建时间 |
| 23 | electronic_fence | text | YES | 电子围栏 |
| 25 | floor_id | varchar(40) | YES | 楼层id |
| 16 | grid_code | varchar(50) | YES | 地理格ID |
| 22 | has_del | smallint | YES | 逻辑删除 |
| 1 | id | bigint | NO | map主键 |
| 24 | label_type_logic_id | varchar(100) | YES | 标签类型ID |
| 6 | latitude | varchar(20) | YES | 纬度 |
| 5 | longitude | varchar(20) | YES | 经度 |
| 2 | map_id | varchar(50) | YES | mapId |
| 3 | name | varchar(255) | YES | 名称 |
| 9 | parent | varchar(50) | YES | 父id |
| 18 | photos | varchar(1000) | YES | 照片相关信息-url，用 || 分隔 |
| 10 | province_code | varchar(50) | YES | POI所在省份编码 |
| 11 | province_name | varchar(255) | YES | POI所在省份名称 |
| 17 | tel | varchar(255) | YES | POI的电话 |
| 8 | type | varchar(255) | YES | 类型 |
| 7 | type_code | varchar(255) | YES | 兴趣点类型编码 |



### hkcy_point_camera (撒点校验) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 4 | camera_index_code | varchar(255) | NO | 相机编号 |
| 15 | camera_type | int | YES | 相机类型 |
| 11 | create_time | datetime | YES | 创建时间 |
| 12 | creater | varchar(255) | YES | 创建者 |
| 9 | global_x | double | YES | 角度坐标 |
| 10 | global_y | double | YES | 角度坐标 |
| 1 | id | bigint | NO |  |
| 18 | label_address | varchar(255) | YES | 标签地址 |
| 5 | label_big_type | varchar(20) | YES | 标签大类 |
| 2 | label_logic_id | varchar(255) | NO | 标签编号 |
| 3 | label_name | varchar(255) | YES |  |
| 6 | label_small_type | varchar(20) | YES | 标签小类 |
| 17 | latitude | double | YES | 标签纬度 |
| 16 | longitude | double | YES | 标签经度 |
| 7 | pixel_x | double | YES | 像素坐标 |
| 8 | pixel_y | double | YES | 像素坐标 |
| 13 | update_time | datetime | YES | 更新时间 |
| 14 | updater | varchar(255) | YES | 更新者 |



### hkcy_region (行政区划表) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 12 | create_time | datetime | YES | 创建时间 |
| 11 | create_user | varchar(100) | YES | 创建者账号 |
| 8 | dept_id | varchar(50) | YES | 所属部门 |
| 9 | has_del | smallint | YES | 是否删除 |
| 1 | id | int | NO |  |
| 2 | index_code | varchar(255) | YES | 区划id |
| 16 | index_path | longtext | YES | 区划id全路径 |
| 17 | index_path_name | longtext | YES | 全路径名称 |
| 6 | level | int | YES | 级别 |
| 4 | name | varchar(100) | YES | 名称 |
| 7 | org_id | varchar(50) | YES | 所属组织 |
| 5 | parent_index_code | varchar(255) | YES | 父区划id |
| 10 | remark | varchar(200) | YES | 备注 |
| 15 | source_type | smallint | YES | 平台类型：10-海康IOT、ISC、PVIA    11-海康8200    20-大华    30-宇视（暂无、预留）    40-紫光（暂无、预留）    50-芯翌    60-东方电子 |
| 3 | tree_code | varchar(255) | YES | 国际树标识 0 |
| 14 | update_time | datetime | YES | 更新时间 |
| 13 | update_user | varchar(100) | YES | 更新者账号 |



### hkcy_region_202409062007 (行政区划表) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 12 | create_time | datetime | YES | 创建时间 |
| 11 | create_user | varchar(100) | YES | 创建者账号 |
| 8 | dept_id | varchar(50) | YES | 所属部门 |
| 9 | has_del | smallint | YES | 是否删除 |
| 1 | id | int | NO |  |
| 2 | index_code | varchar(255) | YES | 区划id |
| 6 | level | int | YES | 级别 |
| 4 | name | varchar(100) | YES | 名称 |
| 7 | org_id | varchar(50) | YES | 所属组织 |
| 5 | parent_index_code | varchar(255) | YES | 父区划id |
| 10 | remark | varchar(200) | YES | 备注 |
| 15 | source_type | smallint | YES | 平台类型：10-海康IOT、ISC、PVIA    11-海康8200    20-大华    30-宇视（暂无、预留）    40-紫光（暂无、预留）    50-芯翌    60-东方电子 |
| 3 | tree_code | varchar(255) | YES | 国际树标识 0 |
| 14 | update_time | datetime | YES | 更新时间 |
| 13 | update_user | varchar(100) | YES | 更新者账号 |



### hkcy_region_202410222006 (行政区划表) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 12 | create_time | datetime | YES | 创建时间 |
| 11 | create_user | varchar(100) | YES | 创建者账号 |
| 8 | dept_id | varchar(50) | YES | 所属部门 |
| 9 | has_del | smallint | YES | 是否删除 |
| 1 | id | int | NO |  |
| 2 | index_code | varchar(255) | YES | 区划id |
| 16 | index_path | longtext | YES | 区划id全路径 |
| 17 | index_path_name | longtext | YES | 全路径名称 |
| 6 | level | int | YES | 级别 |
| 4 | name | varchar(100) | YES | 名称 |
| 7 | org_id | varchar(50) | YES | 所属组织 |
| 5 | parent_index_code | varchar(255) | YES | 父区划id |
| 10 | remark | varchar(200) | YES | 备注 |
| 15 | source_type | smallint | YES | 平台类型：10-海康IOT、ISC、PVIA    11-海康8200    20-大华    30-宇视（暂无、预留）    40-紫光（暂无、预留）    50-芯翌    60-东方电子 |
| 3 | tree_code | varchar(255) | YES | 国际树标识 0 |
| 14 | update_time | datetime | YES | 更新时间 |
| 13 | update_user | varchar(100) | YES | 更新者账号 |



### hkcy_report_base (运维报告基本信息表) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 5 | ad_logic_id | varchar(50) | YES | 所属区域id |
| 6 | ad_name | varchar(50) | YES | 所属区域名称 |
| 11 | camera_total_num | int | YES | 已建设监控数量 |
| 14 | create_time | datetime | YES | 创建时间 |
| 13 | create_user | varchar(100) | YES | 创建者账号 |
| 1 | id | int | NO |  |
| 9 | manage_invalid_num | int | YES | 无效管理对象数量 |
| 10 | manage_miss_num | int | YES | 缺失管理对象数量 |
| 8 | manage_normal_num | int | YES | 正常管理对象数量 |
| 7 | manage_obj_num | int | YES | 管理对象数量 |
| 4 | manage_type | varchar(50) | YES | 管理对象类型 |
| 3 | manage_type_id | varchar(50) | YES | 管理对象类型id |
| 15 | pdf_url | varchar(200) | YES | 生成pdf地址 |
| 2 | report_id | varchar(40) | YES | 报告id |
| 12 | report_time | datetime | YES | 报告时间 |



### hkcy_report_object (运维对象明细表) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 5 | address | varchar(500) | YES | 管理对象地址 |
| 11 | create_time | datetime | YES | 创建时间 |
| 10 | create_user | varchar(100) | YES | 创建者账号 |
| 1 | id | int | NO |  |
| 12 | label_type_logic_id | varchar(50) | YES | 对象来源类型 |
| 7 | latitude | double | YES | 纬度 |
| 6 | longitude | double | YES | 经度 |
| 2 | report_id | varchar(40) | YES | 报告id |
| 8 | status | smallint | YES | 状态 0-缺失 1-有效 2-无效 |
| 9 | suggest | varchar(500) | YES | 建议 |
| 3 | tag_logic_id | varchar(50) | YES | 管理对象id |
| 4 | tag_name | varchar(100) | YES | 管理对象名称 |



### hkcy_report_object_camera (运维对象与设备关系表) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 4 | camera_index_code | varchar(100) | YES | 设备id |
| 5 | camera_name | varchar(200) | YES | 设备名称 |
| 12 | create_time | datetime | YES | 创建时间 |
| 11 | create_user | varchar(100) | YES | 创建者账号 |
| 1 | id | int | NO |  |
| 10 | img_url | varchar(200) | YES |  |
| 8 | latitude | double | YES | 纬度 |
| 7 | longitude | double | YES | 经度 |
| 2 | report_id | varchar(40) | YES | 报告id |
| 9 | status | smallint | YES | 状态 1-有效监控 0-无效监控 |
| 3 | tag_logic_id | varchar(40) | YES | 管理对象id |
| 6 | type | int | YES | 设备类型：0—枪机、1---高空瞭望、2---鹰眼、3---球机 |



### hkcy_reserve_plan (预案) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 15 | create_time | datetime | YES | 创建时间 |
| 14 | create_user | varchar(100) | YES | 创建者账号 |
| 9 | dept_id | varchar(50) | YES | 所属部门 |
| 6 | explain | text | YES | 预案说明 |
| 12 | has_del | smallint | YES | 是否删除 |
| 1 | id | int | NO |  |
| 21 | label_type_logic_id | varchar(50) | YES | 业务资源类型id |
| 24 | latitude | double | YES | 纬度 |
| 23 | longitude | double | YES | 经度 |
| 20 | movingline_flag | int | YES | 是否是动线 1是 0否 |
| 8 | org_id | varchar(50) | YES | 所属组织 |
| 10 | region_id | varchar(50) | YES | 预案从属 |
| 11 | region_level | varchar(50) | YES | 预案级别 |
| 13 | remark | varchar(200) | YES | 备注 |
| 2 | reserve_plan_id | varchar(50) | YES | 预案id |
| 3 | reserve_plan_name | varchar(100) | YES | 预案名称 |
| 5 | scene_type | smallint | YES | 应用类型 0全部 1日常 2应急 |
| 19 | shared | int | YES | 是否共享：0否1是 |
| 18 | sub_code | varchar(40) | YES | 所属专题 |
| 22 | tag_logic_id | varchar(50) | YES | 业务资源id |
| 7 | total_time | int | YES | 总时长 |
| 4 | type | smallint | YES | 预案类型 1定点 2复合 |
| 17 | update_time | datetime | YES | 更新时间 |
| 16 | update_user | varchar(100) | YES | 更新者账号 |



### hkcy_reserve_plan_angle (预案视角) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 12 | create_time | datetime | YES | 创建时间 |
| 11 | create_user | varchar(100) | YES | 创建者账号 |
| 8 | dept_id | varchar(50) | YES | 所属部门 |
| 9 | has_del | smallint | YES | 是否删除 |
| 1 | id | int | NO |  |
| 7 | org_id | varchar(50) | YES | 所属组织 |
| 6 | play_order | int | YES | 播放序列 |
| 5 | play_time | int | YES | 播放时间（分钟） |
| 15 | rel_type | smallint | YES | 关联类型：0代表visual_angle_id储存的是视角ID,1代表visual_angle_id储存的是设备编码 |
| 10 | remark | varchar(200) | YES | 备注 |
| 2 | reserve_plan_id | varchar(50) | YES | 预案id |
| 4 | reserve_plan_sequence_id | varchar(50) | YES | 预案序列id |
| 16 | unit | varchar(5) | YES | 播放时长单位 |
| 14 | update_time | datetime | YES | 更新时间 |
| 13 | update_user | varchar(100) | YES | 更新者账号 |
| 3 | visual_angle_id | varchar(50) | YES | 视角id |



### hkcy_reserve_plan_fence (机场楼层动线预案) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 3 | build_id | varchar(40) | YES | 建筑id |
| 9 | create_time | datetime | YES |  |
| 10 | create_user | varchar(50) | YES |  |
| 4 | floor_id | varchar(40) | YES | 楼层id |
| 8 | has_del | smallint | YES | 逻辑删除 |
| 1 | id | int | NO |  |
| 6 | latitude | double | YES | 点位纬度 |
| 5 | longitude | double | YES | 点位经度 |
| 7 | order_num | int | YES | 排序 |
| 2 | reserve_plan_id | varchar(50) | YES | 预案id |
| 11 | update_time | datetime | YES |  |
| 12 | update_user | varchar(50) | YES |  |



### hkcy_reserve_plan_message (预案变更通知) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 5 | conflict_id | text | YES | 冲突id |
| 7 | conflict_plan_id | varchar(50) | YES | 冲突预案id |
| 6 | conflict_scheduling_id | varchar(50) | YES | 冲突预案排期id |
| 8 | content | text | YES | 内容 |
| 16 | create_time | datetime | YES | 创建时间 |
| 15 | create_user | varchar(100) | YES | 创建者账号 |
| 12 | dept_id | varchar(50) | YES | 所属部门 |
| 14 | has_del | smallint | YES | 是否删除 |
| 1 | id | int | NO |  |
| 2 | message_id | varchar(50) | YES | 消息id |
| 11 | org_id | varchar(50) | YES | 所属组织 |
| 13 | remark | varchar(200) | YES | 备注 |
| 4 | reserve_plan_id | varchar(50) | YES | 预案id |
| 3 | reserve_plan_scheduling_id | varchar(50) | YES | 预案排期id |
| 10 | status | smallint | YES | 是否已读 0未读 1已读 |
| 9 | type | smallint | YES | 消息类型 1修改，2删除，3冲突 |
| 18 | update_time | datetime | YES | 更新时间 |
| 17 | update_user | varchar(100) | YES | 更新者账号 |



### hkcy_reserve_plan_scheduling (预案排期) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 14 | create_time | datetime | YES | 创建时间 |
| 13 | create_user | varchar(100) | YES | 创建者账号 |
| 5 | date | varchar(255) | YES | 指定日期 |
| 9 | dept_id | varchar(50) | YES | 所属部门 |
| 10 | has_del | smallint | YES | 是否删除 |
| 17 | has_verify | smallint | YES | 是否校验冲突：0否1是 |
| 1 | id | int | NO |  |
| 8 | org_id | varchar(50) | YES | 所属组织 |
| 4 | periodic_rule | int | YES | 定期规则 1每日 2工作日 3节假日 4指定日期 |
| 12 | remark | varchar(200) | YES | 备注 |
| 3 | reserve_plan_id | varchar(50) | YES | 预案id |
| 2 | reserve_plan_scheduling_id | varchar(50) | YES | 预案排期id |
| 11 | status | smallint | YES | 是否立即取消 0立即取消 1播放完后取消 |
| 7 | time_end | time | YES | 结束时间 |
| 6 | time_start | time | YES | 开始时间 |
| 16 | update_time | datetime | YES | 更新时间 |
| 15 | update_user | varchar(100) | YES | 更新者账号 |



### hkcy_reserve_plan_scheduling_angle (预案排期冲突视角) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 11 | conflict_date | varchar(255) | YES | 冲突日期 |
| 10 | conflict_date_type | int | YES | 冲突日期类型 1每日 2工作日 3节假日 4指定日期 |
| 17 | conflict_dept_id | varchar(50) | YES | 冲突所属部门 |
| 2 | conflict_id | varchar(50) | YES | 冲突id |
| 16 | conflict_org_id | varchar(50) | YES | 冲突所属组织 |
| 14 | conflict_scheduling_id | varchar(50) | YES | 冲突预案排期id |
| 13 | conflict_time_end | time | YES | 冲突结束时间 |
| 12 | conflict_time_start | time | YES | 冲突开始时间 |
| 15 | conflict_visual_angle_id | varchar(50) | YES | 冲突视角id |
| 25 | create_time | datetime | YES | 创建时间 |
| 24 | create_user | varchar(100) | YES | 创建者账号 |
| 21 | dept_id | varchar(50) | YES | 所属部门 |
| 22 | has_del | smallint | YES | 是否删除 |
| 1 | id | int | NO |  |
| 19 | message_id | varchar(50) | YES | 消息id |
| 9 | old_time_end | time | YES | 原结束时间 |
| 8 | old_time_start | time | YES | 原开始时间 |
| 4 | old_visual_angle_id | varchar(50) | YES | 原视角id |
| 20 | org_id | varchar(50) | YES | 所属组织 |
| 5 | prev_visual_angle_id | varchar(50) | YES | 上一个视角id |
| 28 | rel_type | smallint | YES | 关联类型：0代表新替换的是视角ID,1代表新替换的是设备编码 |
| 23 | remark | varchar(200) | YES | 备注 |
| 3 | scheduling_id | varchar(50) | YES | 预案排期id |
| 18 | scheduling_solution | int | YES | 解决类型 |
| 7 | sequence_id | varchar(50) | YES | 预案序列id |
| 27 | update_time | datetime | YES | 更新时间 |
| 26 | update_user | varchar(100) | YES | 更新者账号 |
| 6 | visual_angle_id | varchar(50) | YES | 新视角id |



### hkcy_reserve_plan_sequence (预案序列) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 22 | build_id | varchar(40) | YES | 建筑id |
| 16 | create_time | datetime | YES | 创建时间 |
| 15 | create_user | varchar(100) | YES | 创建者账号 |
| 12 | dept_id | varchar(50) | YES | 所属部门 |
| 5 | explain | text | YES | 序列描述 |
| 23 | floor_id | varchar(40) | YES | 楼层id |
| 13 | has_del | smallint | YES | 是否删除 |
| 8 | height | int | YES | 高度 |
| 1 | id | int | NO |  |
| 21 | latitude | double | YES | 纬度 |
| 20 | longitude | double | YES | 经度 |
| 11 | org_id | varchar(50) | YES | 所属组织 |
| 10 | play_order | int | YES | 播放序列 |
| 9 | play_time | int | YES | 播放时间（分钟） |
| 14 | remark | varchar(200) | YES | 备注 |
| 4 | reserve_plan_id | varchar(50) | YES | 预案id |
| 2 | reserve_plan_sequence_id | varchar(50) | YES | 序列id |
| 3 | reserve_plan_sequence_name | varchar(100) | YES | 序列名称 |
| 24 | seq_info | text | YES | 每序关注信息 |
| 6 | type | int | YES | 排列方式1：1*1，2：1*2，3：2*2，4：3*3，5：1+2，6：1+5，7：1+7，8：1+8，9：3+4 |
| 19 | unit | varchar(5) | YES | 播放时长单位 |
| 18 | update_time | datetime | YES | 更新时间 |
| 17 | update_user | varchar(100) | YES | 更新者账号 |
| 7 | width | int | YES | 宽度 |



### hkcy_reserve_plan_subject (预案专题表) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 12 | ancestral_name | varchar(255) | YES | 祖籍 |
| 8 | create_time | datetime | YES | 创建时间 |
| 9 | create_user | varchar(50) | YES | 创建人 |
| 13 | free_sort | bigint unsigned | YES | 排序 |
| 6 | has_del | int | YES | 逻辑删除 |
| 1 | id | bigint | NO | 主键 |
| 4 | parent_sub_code | varchar(40) | YES | 父编号 |
| 7 | remark | varchar(255) | YES | 备注 |
| 3 | sub_code | varchar(40) | YES | 编号 |
| 2 | sub_level | int | YES | 级别 |
| 5 | sub_name | varchar(100) | YES | 专题名称 |
| 14 | update_flag | int | YES | 是否可修改 |
| 10 | update_time | datetime | YES | 修改时间 |
| 11 | update_user | varchar(50) | YES | 修改人 |



### hkcy_reserve_plan_tag (预案标签) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 10 | create_time | datetime | YES | 创建时间 |
| 9 | create_user | varchar(100) | YES | 创建者账号 |
| 6 | dept_id | varchar(50) | YES | 所属部门 |
| 7 | has_del | smallint | YES | 是否删除 |
| 1 | id | int | NO |  |
| 5 | org_id | varchar(50) | YES | 所属组织 |
| 8 | remark | varchar(200) | YES | 备注 |
| 2 | reserve_plan_id | varchar(50) | YES | 预案id |
| 3 | tag_id | varchar(50) | YES | 标签id |
| 4 | tag_name | varchar(100) | YES | 标签名称 |
| 12 | update_time | datetime | YES | 更新时间 |
| 11 | update_user | varchar(100) | YES | 更新者账号 |



### hkcy_resource_group () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 5 | auth_field_1 | varchar(100) | YES |  |
| 14 | auth_field_10 | varchar(100) | YES |  |
| 6 | auth_field_2 | varchar(100) | YES |  |
| 7 | auth_field_3 | varchar(100) | YES |  |
| 8 | auth_field_4 | varchar(100) | YES |  |
| 9 | auth_field_5 | varchar(100) | YES |  |
| 10 | auth_field_6 | varchar(100) | YES |  |
| 11 | auth_field_7 | varchar(100) | YES |  |
| 12 | auth_field_8 | varchar(100) | YES |  |
| 13 | auth_field_9 | varchar(100) | YES |  |
| 1 | id | varchar(32) | NO |  |
| 2 | label_type_logic_id | varchar(255) | YES |  |
| 4 | org_id | varchar(50) | YES |  |
| 3 | total_count | int | YES |  |



### hkcy_scene (场景) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 10 | create_time | datetime | YES | 创建时间 |
| 9 | create_user | varchar(100) | YES | 创建者账号 |
| 13 | custom_fence | smallint | YES | 是否自定义围栏 |
| 14 | electronic_fence | text | YES | 自定义电子围栏 |
| 17 | give_equipment | smallint | YES | 是否将场景标签赋予设备 |
| 7 | has_del | smallint | YES | 是否删除 |
| 1 | id | int | NO |  |
| 16 | latitude | double | YES | 自定义电子围栏中心点纬度 |
| 15 | longitude | double | YES | 自定义电子围栏中心点经度 |
| 5 | region_id | varchar(20) | YES | 行政区划 |
| 8 | remark | varchar(200) | YES | 备注 |
| 2 | scene_id | varchar(50) | YES | 场景ID |
| 3 | scene_name | varchar(50) | YES | 场景名称 |
| 6 | scene_params | json | YES | 查询参数 |
| 12 | update_time | datetime | YES | 更新时间 |
| 11 | update_user | varchar(100) | YES | 更新者账号 |
| 4 | user_id | varchar(50) | YES | 所属用户 |



### hkcy_scene_camera (场景与设备关联关系表) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 4 | camera_id | varchar(50) | YES | 设备id |
| 8 | create_time | datetime | YES | 创建时间 |
| 7 | create_user | varchar(100) | YES | 创建者账号 |
| 5 | has_del | smallint | YES | 是否删除 |
| 1 | id | int | NO |  |
| 6 | remark | varchar(200) | YES | 备注 |
| 2 | scene_id | varchar(50) | YES | 场景ID |
| 10 | update_time | datetime | YES | 更新时间 |
| 9 | update_user | varchar(100) | YES | 更新者账号 |
| 3 | user_id | varchar(50) | YES | 所属用户 |



### hkcy_scene_info (智能场景) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 11 | create_time | datetime | YES | 创建时间 |
| 10 | create_user | varchar(64) | YES | 创建者账号 |
| 6 | event_type_ids | text | YES |  |
| 4 | full_select | text | YES |  |
| 5 | half_select | text | YES |  |
| 1 | id | varchar(32) | NO | 主键 |
| 16 | is_enable_scheme | bit(1) | YES |  |
| 13 | location_setting | varchar(255) | YES | 定位配置(json字符串) |
| 2 | name | varchar(64) | YES | 场景名称 |
| 8 | org_id | varchar(50) | YES |  |
| 9 | region_id | varchar(100) | YES |  |
| 3 | remark | varchar(2048) | YES | 场景说明 |
| 7 | scene_type_id | varchar(32) | YES | 场景类型 |
| 15 | scheme_id | varchar(255) | YES |  |
| 14 | select_label_type_logic_ids | text | YES |  |
| 12 | update_time | datetime | YES | 更新时间 |



### hkcy_scene_info_draw_fence (场景绘制围栏) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 3 | draw_type_id | varchar(255) | YES | 围栏类型 HkcySceneInfoDrawTypeEntity.type = 2|3 |
| 4 | fence | longtext | YES | 围栏json |
| 1 | id | varchar(32) | NO | 主键 |
| 2 | name | varchar(255) | YES | 绘制围栏名称 |
| 5 | scene_info_id | varchar(32) | YES | 场景标识 |



### hkcy_scene_info_draw_point (场景绘制点位) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 3 | draw_type_id | varchar(32) | YES | 绘制点位类型 hkcy_scene_info_draw_type.id |
| 7 | has_del | int | YES |  |
| 1 | id | varchar(32) | NO | 主键 |
| 5 | latitude | double | YES | 纬度 |
| 4 | longitude | double | YES | 经度 |
| 2 | name | varchar(255) | YES | 绘制点位名称 |
| 6 | scene_info_id | varchar(32) | YES | 场景标识 |



### hkcy_scene_info_draw_type (场景绘制类型) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 7 | has_del | bit(1) | YES |  |
| 1 | id | varchar(32) | NO | 主键 |
| 8 | is_default | bit(1) | YES |  |
| 2 | name | varchar(255) | YES | 类型名称 |
| 5 | point_pic | varchar(1024) | YES | 点:图片 |
| 6 | point_select_pic | varchar(1024) | YES | 点:选中图片 |
| 3 | scene_type_id | varchar(32) | YES | 场景类型标识 |
| 4 | type | varchar(32) | YES | 点:1 线:2 面:3 |



### hkcy_scene_info_rel (场景资源中间表) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 3 | entity_id | varchar(64) | YES | 业务ID |
| 1 | id | varchar(64) | NO | 主键 |
| 7 | is_fence_out | bit(1) | YES | 是否是围栏外点位(只有是资源才会有该字段) |
| 8 | is_fence_out_to_in | bit(1) | YES | 是否是围栏外点位转到围栏内(只有是资源才会有该字段) |
| 6 | is_show | bit(1) | YES | 是否展示 |
| 9 | label_type_logic_id | varchar(255) | YES |  |
| 2 | parent_id | varchar(64) | YES | 主键父级ID |
| 4 | scene_info_id | varchar(32) | YES | 场景标识 |
| 10 | scheme_line_id | varchar(255) | YES |  |
| 5 | type | varchar(32) | YES | 围栏分类  DRAW_FENCE_TYPE围栏  DRAW_FENCE资源类型  RESOURCE_TYPE_LABEL  RESOURCE_TYPE_DRAW_FENCE资源  RESOURCE_CAMERA  RESOURCE_POI  RESOURCE_TAG  RESOURCE_DRAW_POINT |



### hkcy_scene_info_reserve_plan (场景资源中间表) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | id | varchar(32) | NO | 主键 |
| 3 | reserve_plan_id | varchar(64) | YES | 预案标识 |
| 2 | scene_info_id | varchar(32) | YES | 场景标识 |



### hkcy_scene_info_scheme (智能场景) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | id | varchar(32) | NO | 主键 |
| 3 | is_public | bit(1) | YES |  |
| 2 | name | varchar(64) | YES | 名称 |
| 4 | scene_info_id | varchar(32) | YES |  |



### hkcy_scene_info_scheme_line (智能场景) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 4 | color | varchar(1024) | YES |  |
| 1 | id | varchar(32) | NO | 主键 |
| 2 | name | varchar(64) | YES |  |
| 3 | scheme_id | varchar(32) | YES |  |



### hkcy_scene_info_tag (智能场景类型) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | id | varchar(32) | NO | 主键 |
| 3 | scene_info_id | varchar(32) | YES |  |
| 2 | tag_code | varchar(255) | YES |  |



### hkcy_scene_info_type (智能场景类型) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 7 | has_del | bit(1) | YES | 是否删除 |
| 1 | id | varchar(32) | NO | 主键 |
| 6 | label_type_logic_ids | text | YES |  |
| 5 | level | int | YES |  |
| 2 | name | varchar(64) | YES | 场景名称 |
| 3 | pid | varchar(32) | YES |  |
| 4 | sort | int | YES |  |



### hkcy_scene_tag (场景标签关系表) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 6 | create_time | datetime | YES | 创建时间 |
| 5 | create_user | varchar(100) | YES | 创建者账号 |
| 4 | has_del | smallint | YES | 是否删除 |
| 1 | id | int | NO |  |
| 2 | scene_id | varchar(40) | YES | 设备编号 |
| 3 | tag_id | varchar(40) | YES | 标签编号 |
| 8 | update_time | datetime | YES | 更新时间 |
| 7 | update_user | varchar(100) | YES | 更新者账号 |



### hkcy_tag_info (点位) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 7 | address | varchar(500) | YES | 地址 |
| 21 | auth_field_1 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 30 | auth_field_10 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 22 | auth_field_2 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 23 | auth_field_3 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 24 | auth_field_4 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 25 | auth_field_5 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 26 | auth_field_6 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 27 | auth_field_7 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 28 | auth_field_8 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 29 | auth_field_9 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 13 | create_time | varchar(100) | YES | 创建时间 |
| 14 | creater | varchar(50) | YES | 创建人 |
| 31 | electronic_fence | longtext | YES | 电子围栏 |
| 19 | external_label_id | varchar(255) | YES | 外来的标签ID |
| 9 | has_del | int | YES | 0非 1删 |
| 32 | height | double | YES | 标签高度 |
| 11 | hik_msg | varchar(255) | YES | 调用海康接口返回信息 |
| 10 | hik_status | int | YES | 海康标签标志 0未发 1已发 |
| 1 | id | int | NO | 主键 |
| 8 | imgaddress | varchar(255) | YES | 图片地址 |
| 20 | label_type_logic_id | varchar(100) | YES | 标签类型ID |
| 5 | latitude | double | YES | 纬度 |
| 6 | longandlat | varchar(255) | YES |  |
| 4 | longitude | double | YES | 经度 |
| 17 | org_id | varchar(50) | YES | 所属组织 |
| 18 | tag_base_info | text | YES | 标签基本信息 |
| 2 | tag_logic_id | varchar(50) | YES |  |
| 12 | tag_source | varchar(255) | YES | 标签来源 |
| 3 | tagname | varchar(255) | YES |  |
| 16 | update_time | varchar(100) | YES | 修改人 |
| 15 | updater | varchar(50) | YES | 修改时间 |



### hkcy_tag_info_aircraft () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 7 | address | varchar(500) | YES | 地址 |
| 21 | auth_field_1 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 30 | auth_field_10 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 22 | auth_field_2 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 23 | auth_field_3 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 24 | auth_field_4 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 25 | auth_field_5 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 26 | auth_field_6 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 27 | auth_field_7 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 28 | auth_field_8 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 29 | auth_field_9 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 13 | create_time | varchar(100) | YES | 创建时间 |
| 14 | creater | varchar(50) | YES | 创建人 |
| 31 | electronic_fence | longtext | YES | 电子围栏 |
| 19 | external_label_id | varchar(255) | YES | 外来的标签ID |
| 9 | has_del | int | YES | 0非 1删 |
| 32 | height | double | YES | 标签高度 |
| 11 | hik_msg | varchar(255) | YES | 调用海康接口返回信息 |
| 10 | hik_status | int | YES | 海康标签标志 0未发 1已发 |
| 1 | id | int | NO | 主键 |
| 8 | imgaddress | varchar(255) | YES | 图片地址 |
| 20 | label_type_logic_id | varchar(100) | YES | 标签类型ID |
| 5 | latitude | double | YES | 纬度 |
| 6 | longandlat | varchar(255) | YES |  |
| 4 | longitude | double | YES | 经度 |
| 17 | org_id | varchar(50) | YES | 所属组织 |
| 18 | tag_base_info | text | YES | 标签基本信息 |
| 2 | tag_logic_id | varchar(50) | YES |  |
| 12 | tag_source | varchar(255) | YES | 标签来源 |
| 3 | tagname | varchar(255) | YES |  |
| 16 | update_time | varchar(100) | YES | 修改人 |
| 15 | updater | varchar(50) | YES | 修改时间 |



### hkcy_tag_info_old (点位) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 28 | ad_logic_id | varchar(64) | YES | 已作废，当前区划用auth_field_1-10维护 |
| 39 | ad_logic_id_fill_status | int | YES | ad_logic_id填充状态： 0手动填充 1自动填充成功 2自动填充失败 |
| 7 | address | varchar(500) | YES | 地址 |
| 9 | affiliatedunits | varchar(255) | YES | 所属单位 |
| 29 | auth_field_1 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 38 | auth_field_10 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 30 | auth_field_2 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 31 | auth_field_3 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 32 | auth_field_4 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 33 | auth_field_5 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 34 | auth_field_6 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 35 | auth_field_7 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 36 | auth_field_8 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 37 | auth_field_9 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 19 | create_time | varchar(100) | YES | 创建时间 |
| 20 | creater | varchar(50) | YES | 创建人 |
| 24 | dept_id | varchar(50) | YES | 所属部门 |
| 40 | electronic_fence | longtext | YES | 电子围栏 |
| 26 | external_label_id | varchar(255) | YES | 外来的标签ID |
| 12 | has_del | int | YES | 0非 1删 |
| 41 | height | double | YES | 标签高度 |
| 14 | hik_msg | varchar(255) | YES | 调用海康接口返回信息 |
| 13 | hik_status | int | YES | 海康标签标志 0未发 1已发 |
| 1 | id | int | NO | 主键 |
| 11 | imgaddress | varchar(255) | YES | 图片地址 |
| 10 | installdate | varchar(255) | YES | 安装日期 |
| 27 | label_type_logic_id | varchar(100) | YES | 标签类型ID |
| 5 | latitude | double | YES | 纬度 |
| 6 | longandlat | varchar(255) | YES |  |
| 4 | longitude | double | YES | 经度 |
| 23 | org_id | varchar(50) | YES | 所属组织 |
| 25 | tag_base_info | text | YES | 标签基本信息 |
| 15 | tag_big_type | int | YES | 大类型 |
| 17 | tag_child_type | int | YES | 子类型 |
| 2 | tag_logic_id | varchar(50) | YES |  |
| 16 | tag_small_type | int | YES | 小类型 |
| 18 | tag_source | varchar(255) | YES | 标签来源 |
| 3 | tagname | varchar(255) | YES |  |
| 22 | update_time | varchar(100) | YES | 修改人 |
| 21 | updater | varchar(50) | YES | 修改时间 |
| 8 | urladdress | varchar(255) | YES | url地址 |



### hkcy_tag_info_tag (业务资源——业务标签映射表) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 4 | create_time | datetime | YES | 创建事件 |
| 5 | create_user | varchar(255) | YES | 创建人 |
| 1 | id | int | NO | 主键 |
| 3 | tag_code | varchar(20) | YES | 业务标签编号 |
| 2 | tag_logic_id | varchar(50) | YES | 业务资源id |



### hkcy_test_hik_log () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | camera_index_code | varchar(100) | YES | 设备编码 |
| 5 | content | text | YES | 日志内容 |
| 6 | create_time | datetime | YES |  |
| 1 | id | int | NO | 主键 |
| 4 | picture_status | smallint | YES | 是否抓图成功 |
| 7 | response_duration | int | YES | 响应时长 |
| 8 | score | int | YES | 图片分数 |
| 3 | stream_status | smallint | YES | 是否获取到流url |



### mock_negotiation (沙盘推演表) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 5 | camera_index_code | varchar(255) | YES | 相机id |
| 10 | create_time | datetime | YES | 创建时间 |
| 11 | create_user | varchar(255) | YES | 创建人 |
| 17 | detail_url | varchar(500) | YES | 详情url |
| 9 | has_del | int | YES | 逻辑删除标识 |
| 14 | icon_type_logic_id | varchar(100) | YES | 图标icon(mock_negotiation_type) |
| 1 | id | bigint | NO | id |
| 2 | logic_id | varchar(100) | YES | 逻辑id |
| 3 | name | varchar(255) | YES | 名称 |
| 19 | org_id | varchar(50) | YES | 所属组织 |
| 6 | p | varchar(255) | YES | 当前相机p值 |
| 15 | point_x | double | YES | 点位x(256制) |
| 16 | point_y | double | YES | 点位y(256制) |
| 4 | remark | varchar(500) | YES | 备注 |
| 18 | shared | int | YES | 是否共享：0否  1是 |
| 7 | t | varchar(255) | YES | 当前相机t值 |
| 12 | update_time | datetime | YES | 更新时间 |
| 13 | update_user | varchar(255) | YES | 更新人 |
| 8 | z | varchar(255) | YES | 当前相机z值 |



### mock_negotiation_type (沙盘推演类型表) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 6 | create_time | datetime | YES | 创建时间 |
| 7 | create_user | varchar(255) | YES | 创建人 |
| 5 | has_del | int | YES | 逻辑删除标识 |
| 10 | icon_url | varchar(255) | YES | 图标icon |
| 1 | id | int | NO | 自增id |
| 2 | logic_id | varchar(100) | YES | 逻辑id |
| 3 | name | varchar(255) | YES | 名称 |
| 11 | parent_logic_id | varchar(100) | YES | 父级逻辑id |
| 4 | remark | varchar(500) | YES | 备注 |
| 8 | update_time | datetime | YES | 更新时间 |
| 9 | update_user | varchar(255) | YES | 更新人 |



### poi_info (实景POI数据表) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 17 | ad_code | varchar(50) | YES | 区域编码。已作废，当前区划用auth_field_1-10维护 |
| 31 | ad_code_fill_status | int | YES | ad_code填充状态： 0手动填充 1自动填充成功 2自动填充失败 |
| 4 | address | varchar(255) | YES | 地址 |
| 18 | auth_field_1 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 27 | auth_field_10 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 19 | auth_field_2 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 20 | auth_field_3 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 21 | auth_field_4 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 22 | auth_field_5 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 23 | auth_field_6 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 24 | auth_field_7 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 25 | auth_field_8 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 26 | auth_field_9 | varchar(100) | YES | 统一字段，自定义区划类型 |
| 30 | build_id | varchar(40) | YES | 建筑物id |
| 13 | create_time | datetime | YES | 创建时间 |
| 12 | create_user | varchar(255) | YES | 创建人 |
| 10 | dept_id | varchar(255) | YES | 部门id |
| 28 | electronic_fence | text | YES | 电子围栏 |
| 29 | floor_id | varchar(40) | YES | 楼层id |
| 11 | has_del | int | YES | 删除状态（0=未删除；1=已删除） |
| 1 | id | int | NO | 自增id |
| 16 | label_type_logic_id | varchar(100) | YES | 标签类型ID |
| 6 | latitude | double | YES | 纬度 |
| 2 | logic_id | varchar(100) | NO | 逻辑id，取mapid |
| 5 | longitude | double | YES | 经度 |
| 9 | org_id | varchar(100) | YES | 组织id |
| 3 | poi_name | varchar(255) | NO | 标签名字 |
| 8 | poi_source | varchar(255) | YES | 标签来源 |
| 7 | state | int | YES | 状态（0=待撒点；1=已撒点） |
| 32 | type_code | varchar(50) | YES | poi小类型编码 |
| 15 | update_time | datetime | YES | 更新时间 |
| 14 | update_user | varchar(255) | YES | 更新人 |



### poi_record () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 7 | address | varchar(255) | YES | 地址 |
| 13 | create_time | varchar(100) | YES | 创建时间 |
| 14 | creater | varchar(50) | YES | 创建人 |
| 10 | division_id | int | YES | 区划id |
| 11 | division_name | varchar(255) | YES | 区划名称 |
| 12 | has_del | int | YES | 0非 1删 |
| 1 | id | int | NO |  |
| 5 | latitude | double | YES | 纬度 |
| 2 | logic_id | varchar(255) | YES | 逻辑id |
| 6 | longandlat | varchar(255) | YES |  |
| 4 | longitude | double | YES | 经度 |
| 3 | name | varchar(255) | YES | 名称 |
| 8 | type_id | varchar(255) | YES | 类型id |
| 9 | type_name | varchar(255) | YES | 类型名称 |
| 16 | update_time | varchar(100) | YES | 修改人 |
| 15 | updater | varchar(50) | YES | 修改时间 |



### poi_tag_mapping (poi-业务资源关系映射表) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 1 | id | int | NO |  |
| 2 | poi_name | varchar(255) | YES | poi名称 |
| 3 | poi_type | varchar(255) | YES | poi类型编码 |
| 4 | tag_name | varchar(255) | YES | 业务资源名称 |
| 5 | tag_type | varchar(255) | YES | 业务资源类型编码 |



### preset_point_info (预置点位信息表) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 7 | camera_index_code | varchar(255) | YES | 相机设备ID |
| 11 | create_time | datetime | YES | 创建时间 |
| 10 | create_user | varchar(100) | YES | 创建者账号 |
| 8 | has_del | int | YES | 是否删除 |
| 1 | id | int | NO |  |
| 2 | name | varchar(255) | YES | 预置点位名称 |
| 3 | pan_pos | double | NO | 角度信息:P参数（水平参数） |
| 9 | remark | varchar(255) | YES | 备注 |
| 4 | tilt_pos | double | YES | 角度信息:T参数（垂直参数） |
| 6 | type | varchar(255) | YES |  |
| 13 | update_time | datetime | YES | 更新时间 |
| 12 | update_user | varchar(100) | YES | 更新者账号 |
| 5 | zoom_pos | double | YES | 角度信息:Z参数（变倍参数） |



### role_camera () 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 3 | camera_index_code | varchar(100) | YES | 设备编码，即ngh-smar-ar.hkcy_camera_equipment_info.camera_index_code |
| 4 | camera_name | varchar(255) | YES | 设备名称 |
| 5 | create_time | datetime | YES | 创建时间 |
| 6 | create_user | varchar(100) | YES | 创建人 |
| 1 | id | bigint | NO | 自增id |
| 2 | role_logic_id | varchar(100) | YES | 角色逻辑id |
| 7 | update_time | datetime | YES | 更新时间 |
| 8 | update_user | varchar(100) | YES | 更新人 |



### tag_drawing (矢量绘制表) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 4 | address | varchar(255) | YES | 地址 |
| 30 | aoi_info_id | bigint | YES | aoi信息表主键 |
| 7 | camera_index_code | varchar(255) | YES | 相机id |
| 25 | create_time | datetime | YES | 创建时间 |
| 26 | create_user | varchar(255) | YES | 创建人 |
| 19 | fill_color | varchar(10) | YES | 填充色 |
| 20 | fill_opacity | float | YES | 填充色透明度 |
| 24 | has_del | int | YES | 逻辑删除标识 |
| 18 | has_end_arrow | tinyint | YES | 是否有结束箭头：0=否；1=是 |
| 17 | has_start_arrow | tinyint | YES | 是否有起始箭头：0=否；1=是 |
| 1 | id | int | NO | 自增id |
| 31 | is_security_zone | int | YES | 是否安全监管区域 |
| 6 | label_type_logic_id | varchar(100) | YES | 标签类型ID |
| 2 | logic_id | varchar(100) | YES | 逻辑id |
| 3 | name | varchar(255) | YES | 名称 |
| 33 | org_id | varchar(50) | YES | 所属组织 |
| 8 | p | varchar(255) | YES | 当前相机p值 |
| 23 | points | json | YES | 点位集 |
| 5 | remark | varchar(500) | YES | 备注 |
| 32 | shared | int | YES | 是否共享：0否  1是 |
| 21 | start_x | int | YES | 开始位置x |
| 22 | start_y | int | YES | 开始位置y |
| 12 | stroke_color | varchar(10) | YES | 画笔颜色 |
| 16 | stroke_dash_array | varchar(10) | YES | 画笔冲刺配置（虚线间隔） |
| 15 | stroke_dash_offset | int | YES | 画笔冲刺偏移量（0=虚线;1=实线） |
| 13 | stroke_opacity | float | YES | 画笔透明度 |
| 14 | stroke_thickness | int | YES | 画笔粗细 |
| 9 | t | varchar(255) | YES | 当前相机t值 |
| 29 | tag_draw_icon | varchar(10) | YES | 图标icon(字典表tag_draw_icon) |
| 11 | type | int | YES | 类型：1=线型；2=区域型 |
| 27 | update_time | datetime | YES | 更新时间 |
| 28 | update_user | varchar(255) | YES | 更新人 |
| 10 | z | varchar(255) | YES | 当前相机z值 |



### track_history (动态轨迹信息表) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | camera_index_code | varchar(255) | NO | 相机编号 |
| 11 | create_time | datetime | YES | 创建时间 |
| 1 | id | bigint | NO | 主键 |
| 5 | label_type_logic_id | varchar(100) | YES | 标签类型ID |
| 9 | latitude | double | YES | 纬度 |
| 8 | longitude | double | YES | 经度 |
| 4 | name | varchar(255) | YES | 名称 |
| 12 | original_id | varchar(32) | YES | 原始id |
| 6 | pixel_x | double | YES | 像素坐标 |
| 7 | pixel_y | double | YES | 像素坐标 |
| 10 | track_time | datetime | YES | 轨迹时间 |
| 3 | unique_number | varchar(255) | YES | 唯一编号 |



### track_info (动态轨迹信息表) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 3 | camera_index_code | varchar(255) | YES | 相机编号 |
| 10 | create_time | datetime | YES | 创建时间 |
| 1 | id | bigint | NO | 主键 |
| 2 | label_camera_id | bigint | NO | 标签表id |
| 6 | label_type_logic_id | varchar(100) | YES | 标签类型ID |
| 8 | latitude | double | YES | 纬度 |
| 7 | longitude | double | YES | 经度 |
| 5 | name | varchar(255) | YES | 名称 |
| 11 | original_id | varchar(32) | YES | 原始id |
| 9 | track_time | datetime | YES | 轨迹时间 |
| 4 | unique_number | varchar(255) | YES | 唯一编号 |



### uav_detail (无人机详细信息) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 2 | brand | varchar(100) | NO | 无人机厂家（数据字典：大疆/极飞） |
| 4 | camera_radius | int | NO | 可视半径 |
| 9 | create_time | datetime | YES | 创建时间 |
| 7 | create_user | varchar(100) | YES | 创建者账号 |
| 5 | horizontal_fov | int | NO | 水平视场角 |
| 1 | id | bigint | NO |  |
| 3 | model | varchar(100) | NO | 无人机型号（数据字典：M3T/M30T） |
| 10 | update_time | datetime | YES | 更新时间 |
| 8 | update_user | varchar(100) | YES | 更新者账号 |
| 6 | vertical_fov | int | NO | 垂直视场角 |



### uav_expand (无人机扩展信息表，无人机为动态资源的一种) 
| 序号 | 字段名称 | 数据类型 | 是否为空 | 字段说明 |
| :--: |----| ---- | ---- | ---- |
| 6 | camera_radius | double | NO | 可视半径 |
| 14 | create_time | datetime | YES | 创建时间 |
| 12 | create_user | varchar(100) | YES | 创建者账号 |
| 18 | desc_info | text | YES | 备注 |
| 2 | device_code | varchar(50) | NO | 设备编号 |
| 17 | flight_parameter_file_path | text | YES | 参数url |
| 7 | h_fov | double | NO | 水平视场角 |
| 1 | id | bigint | NO |  |
| 21 | need_reverse_yaw | int | YES | 是否需要反转偏航角 |
| 11 | param_interface | int | NO | 参数接入方式 |
| 9 | stream_interface | int | NO | 视频接入方式。1=离线方式；2=在线方式 |
| 4 | uav_brand | varchar(100) | NO | 无人机厂家（数据字典：大疆/极飞） |
| 3 | uav_camera_index_code | varchar(100) | YES | 无人机相机id |
| 5 | uav_model | varchar(100) | NO | 无人机型号（数据字典：M3T/M30T） |
| 15 | update_time | datetime | YES | 更新时间 |
| 13 | update_user | varchar(100) | YES | 更新者账号 |
| 8 | v_fov | double | NO | 垂直视场角 |
| 20 | video_duration | bigint | YES | 视频时长 |
| 16 | video_file_path | text | YES | 视频播放URL |
| 10 | video_start_time | datetime | YES | 视频开始时间，仅离线方式（即stream_interface=1）需要配置 |
| 19 | zip_file_path | text | YES | 压缩包路径 |
