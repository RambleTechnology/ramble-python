import http.client
import json


# 接口前缀
url_prefix = "es-flight-api-cn.djigate.com"

# token
token = "eyJhbGciOiJIUzUxMiIsImNyaXQiOlsidHlwIiwiYWxnIiwia2lkIl0sImtpZCI6IjhiZmRiZmRkLWM4OGYtNGE5Yi04NzI3LWQ0ZGYzYWE5OTJlOSIsInR5cCI6IkpXVCJ9.eyJhY2NvdW50IjoiMTgyMjI3MDY5ODYiLCJleHAiOjIwNjEwODMwOTgsIm5iZiI6MTc0NTU1MDI5OCwib3JnYW5pemF0aW9uX3V1aWQiOiI3YjgxYTM1YS0yNTVkLTQ1NjUtOGFiNy04NzE3MWNkM2MxZDUiLCJwcm9qZWN0X3V1aWQiOiIiLCJzdWIiOiJmaDIiLCJ1c2VyX2lkIjoiMTc3MDAwODc2NzI3NTAxMjA5NiJ9.JJGGFjHFy-vIhx9m39E6CCaDz1v5rF5_7gQUYJ-hInu8SBjJZEeTS2k9CfQVfqm4phKSkUFA4GZRPfrqfCqlvg"

# 济阳项目  project_id
projcet_id = "b96b008f-f9b6-4686-acd0-446a07d2488a"

conn = http.client.HTTPSConnection("es-flight-api-cn.djigate.com")


"""获取组织下项目列表
成功响应：
{
    "code": 0,
    "message": "OK",
    "data": {
        "pagination": {
            "page": 1,
            "page_size": 10,
            "total": 1
        },
        "list": [
            {
                "name": "济阳项目",
                "introduction": "",
                "uuid": "b96b008f-f9b6-4686-acd0-446a07d2488a",
                "project_id": "BVJJA5",
                "org_uuid": "7b81a35a-255d-4565-8ab7-87171cd3c1d5",
                "status": "project-status-run",
                "c2c_enable": false,
                "dock_rotation_disabled": false,
                "c2c_task_enable": false,
                "created_at": 1745477055,
                "updated_at": 1745548662,
                "project_work_center_point": {
                    "latitude": 36.976439328799245,
                    "longitude": 117.16591001110616
                },
                "project_fast_join": null,
                "project_weather_blocking": {
                    "cloud_weather_blocking_status": true,
                    "airport_weather_station_blocking_status": true,
                    "cloud_weather_blocking_config": null,
                    "airport_weather_station_blocking_config": null,
                    "blocking_config_by_dock": {
                        "3-1-0": {
                            "cloud_weather_blocking_config": {
                                "wind_speed_limit": 15,
                                "precipitation_limit": 3
                            },
                            "airport_weather_station_blocking_config": {
                                "wind_speed_limit": 12,
                                "precipitation_limit": 3
                            }
                        },
                        "3-2-0": {
                            "cloud_weather_blocking_config": {
                                "wind_speed_limit": 12,
                                "precipitation_limit": 3
                            },
                            "airport_weather_station_blocking_config": {
                                "wind_speed_limit": 8,
                                "precipitation_limit": 3
                            }
                        },
                        "3-3-0": {
                            "cloud_weather_blocking_config": {
                                "wind_speed_limit": 12,
                                "precipitation_limit": 3
                            },
                            "airport_weather_station_blocking_config": {
                                "wind_speed_limit": 12,
                                "precipitation_limit": 3
                            }
                        }
                    }
                },
                "project_share_config": {
                    "live_disable": false,
                    "media_disable": false
                },
                "project_type": 0,
                "project_crs_config": null,
                "role": "",
                "organization_user_role": "",
                "organization_user_callsign": "",
                "is_show_project_manage_icon": false,
                "is_show_project_enter_button": false,
                "project_commanders": [
                    {
                        "project_commander_user_id": "1770008767275012096",
                        "project_commander_organization_callsign": "济阳测试账户2"
                    },
                    {
                        "project_commander_user_id": "1770682342278021120",
                        "project_commander_organization_callsign": "济阳测试账号1"
                    },
                    {
                        "project_commander_user_id": "1876532235536445440",
                        "project_commander_organization_callsign": "马兖龙"
                    },
                    {
                        "project_commander_user_id": "1896370917857808384",
                        "project_commander_organization_callsign": "济阳测试账号3"
                    }
                ]
            }
        ]
    }
}
"""


def get_org_project():
    payload = json.dumps({})
    headers = {"X-Organization-Key": token, "Content-Type": "application/json"}
    conn.request(
        "GET", "/manage/api/v1.0/projects?page=1&page_size=10", payload, headers
    )
    res = conn.getresponse()
    data = res.read()
    print(f"组织下的项目列表=" + data.decode("utf-8"))


"""获取项目下的设备列表
成功响应：
{
    "code": 0,
    "message": "OK",
    "data": {
        "pagination": {
            "page": 1,
            "page_size": 11,
            "total": 11
        },
        "list": [
            {
                "sn": "1581F6GKB236G003000Q",
                "nickname": "M350 RTK",
                "device_model": {
                    "key": "0-89-0",
                    "domain": "0",
                    "type": "89",
                    "sub_type": "0",
                    "name": "M350 RTK",
                    "class": "drone",
                    "develop_code": "pm431"
                },
                "is_org_device": false,
                "device_organization_callsign": ""
            },
            {
                "sn": "1581F6Q8X252U00G05FH",
                "nickname": "M3TD",
                "device_model": {
                    "key": "0-91-1",
                    "domain": "0",
                    "type": "91",
                    "sub_type": "1",
                    "name": "M3TD",
                    "class": "drone",
                    "develop_code": "ea220t"
                },
                "is_org_device": false,
                "device_organization_callsign": ""
            },
            {
                "sn": "1581F7FVC253900D1DWQ",
                "nickname": "Matrice 4E",
                "device_model": {
                    "key": "0-99-0",
                    "domain": "0",
                    "type": "99",
                    "sub_type": "0",
                    "name": "Matrice 4E",
                    "class": "drone",
                    "develop_code": "wa345e"
                },
                "is_org_device": false,
                "device_organization_callsign": ""
            },
            {
                "sn": "1581F7K3C24C300A896K",
                "nickname": "Matrice 4T",
                "device_model": {
                    "key": "0-99-1",
                    "domain": "0",
                    "type": "99",
                    "sub_type": "1",
                    "name": "Matrice 4T",
                    "class": "drone",
                    "develop_code": "wa345t"
                },
                "is_org_device": true,
                "device_organization_callsign": "Matrice 4T"
            },
            {
                "sn": "1ZMBHBP00300RQ",
                "nickname": "DJI RC",
                "device_model": {
                    "key": "2-56-0",
                    "domain": "2",
                    "type": "56",
                    "sub_type": "0",
                    "name": "DJI RC",
                    "class": "rc",
                    "develop_code": "rm500"
                },
                "is_org_device": false,
                "device_organization_callsign": ""
            },
            {
                "sn": "1ZNBHBS00C004G",
                "nickname": "M300 RTK",
                "device_model": {
                    "key": "0-60-0",
                    "domain": "0",
                    "type": "60",
                    "sub_type": "0",
                    "name": "M300 RTK",
                    "class": "drone",
                    "develop_code": "pm430"
                },
                "is_org_device": true,
                "device_organization_callsign": "M300 RTK"
            },
            {
                "sn": "4LFCK340010G9A",
                "nickname": "DJI RC Plus",
                "device_model": {
                    "key": "2-119-0",
                    "domain": "2",
                    "type": "119",
                    "sub_type": "0",
                    "name": "DJI RC Plus",
                    "class": "rc",
                    "develop_code": "rm700"
                },
                "is_org_device": false,
                "device_organization_callsign": ""
            },
            {
                "sn": "5YSZK6N0010059",
                "nickname": "RM510",
                "device_model": {
                    "key": "2-144-0",
                    "domain": "2",
                    "type": "144",
                    "sub_type": "0",
                    "name": "RM510",
                    "class": "rc",
                    "develop_code": "rm510"
                },
                "is_org_device": false,
                "device_organization_callsign": ""
            },
            {
                "sn": "5YSZN1K00311WJ",
                "nickname": "RM510-1",
                "device_model": {
                    "key": "2-144-0",
                    "domain": "2",
                    "type": "144",
                    "sub_type": "0",
                    "name": "RM510",
                    "class": "rc",
                    "develop_code": "rm510"
                },
                "is_org_device": false,
                "device_organization_callsign": ""
            },
            {
                "sn": "9N9CMC30010ML8",
                "nickname": "DJI RC Plus 2",
                "device_model": {
                    "key": "2-174-0",
                    "domain": "2",
                    "type": "174",
                    "sub_type": "0",
                    "name": "DJI RC Plus 2",
                    "class": "rc",
                    "develop_code": "rc701"
                },
                "is_org_device": false,
                "device_organization_callsign": ""
            },
            {
                "sn": "9N9CN2P0012M2U",
                "nickname": "DJI RC Plus 2-1",
                "device_model": {
                    "key": "2-174-0",
                    "domain": "2",
                    "type": "174",
                    "sub_type": "0",
                    "name": "DJI RC Plus 2",
                    "class": "rc",
                    "develop_code": "rc701"
                },
                "is_org_device": false,
                "device_organization_callsign": ""
            }
        ]
    }
}
"""


def get_project_device():
    payload = ""
    headers = {"X-Organization-Key": token}
    conn.request(
        "GET", f"/manage/api/v1.0/projects/{projcet_id}/devices", payload, headers
    )
    res = conn.getresponse()
    data = res.read()
    print(f"项目({projcet_id})下的设备列表=" + data.decode("utf-8"))


"""开始码流转发
成功响应：
{
    "code": 0,
    "message": "OK",
    "data": {
        "code": 0,
        "message": "ok",
        "converter_id": "1a3ea550-ebda-4271-b80a-bc899cef385c",
        "create_ts": 1745397425843,
        "update_ts": 1745397425843,
        "converter_state": "connecting",
        "data": {
            "converter_id": "1a3ea550-ebda-4271-b80a-bc899cef385c",
            "create_ts": 1745397425843,
            "update_ts": 1745397425843,
            "converter_state": "connecting"
        }
    }
}

"""


def start_convert():
    payload = json.dumps(
        {
            "region": "cn",
            "converter_name": "convert6",
            # 机场
            # "sn": "7CTXN2T00B07DK",
            # 无人机 1581F6Q8X252U00G05EA
            # "sn": "1ZNBHBS00C004G",
            # "sn": "1581F7K3C24C300A896K",
            # M4E
            # "camera": "88-0-0",
            # "camera": "176-0-0",
            # "sn": "1ZNBJ9700C002H",
            # "camera": "39-0-7",
            "sn": "1581F7FVC253900D1DWQ",
            "camera": "39-0-7",
            "video": "normal-0",
            "video_quality": 0,
        }
    )
    headers = {"X-Organization-Key": token, "Content-Type": "application/json"}
    conn.request("POST", "/manage/api/v1.0/stream-converters", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))


"""获取码流转发频道转码器
成功响应：
{
    "code": 0,
    "message": "OK",
    "data": {
        "total_count": 2,
        "cursor": 0,
        "members": [
            {
                "rtc_channel": "1581F6Q8X252U00G05EA_176-0-0",
                "status": "",
                "converter_name": "test",
                "update_ts": "1745396463",
                "rtmp_url": "rtmp://111.33.143.195:1935/live/ngh/1581F6Q8X252U00G05EA/176-0-0",
                "converter_id": "3ef42255-8638-4acc-b217-1a27b5f21792",
                "idle_timeout": "500",
                "state": "",
                "volc_status": 2,
                "volc_push_stream_state": 1
            },
            {
                "rtc_channel": "1581F6Q8X252U00G05EA_176-0-0",
                "status": "",
                "converter_name": "test33",
                "update_ts": "1745396463",
                "rtmp_url": "rtmp://111.33.143.195:1935/live/ngh/1581F6Q8X252U00G05EA/176-0-0",
                "converter_id": "176b729b-cd3a-446b-b972-66a71e33d62a",
                "idle_timeout": "500",
                "state": "",
                "volc_status": 2,
                "volc_push_stream_state": 1
            }
        ]
    }
}
"""


def get_convert_channel():
    # 机场
    # videoid = "7CTXN2T00B07DK_176-0-0"
    # 无人机
    # videoid="1581F6Q8X252U00G05EA_176-0-0"
    # videoid = "1581F7FVC253900D1DWQ_88-0-0"
    videoid = "1ZNBJ9700C002H_39-0-7"
    payload = ""
    headers = {"X-Organization-Key": token}
    conn.request(
        "GET",
        f"/manage/api/v1.0/stream-converters?channel={videoid}",
        payload,
        headers,
    )
    res = conn.getresponse()
    data = res.read()
    channel = data.decode("utf-8")
    print(channel)
    return channel


"""关闭码流转发
成功响应：
{"code":0,"message":"OK","data":null}
"""


def stop_convert_live_stream(channel):
    payload = ""
    headers = {"X-Organization-Key": token}
    conn.request(
        "DELETE",
        f"/manage/api/v1.0/stream-converters/{channel}",
        payload,
        headers,
    )
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))


if __name__ == "__main__":

    # get_org_project()

    # get_project_device()

    start_convert()

    # channel = get_convert_channel()

    # stop_convert_live_stream("3ef42255-8638-4acc-b217-1a27b5f21792")
    # stop_convert_live_stream("3399A935C04749DA404004BEFA63E26E")
