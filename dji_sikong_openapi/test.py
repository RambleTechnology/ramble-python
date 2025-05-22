import http.client
import json


# 接口前缀
url_prefix = "es-flight-api-cn.djigate.com"

# token
token = "eyJhbGciOiJIUzUxMiIsImNyaXQiOlsidHlwIiwiYWxnIiwia2lkIl0sImtpZCI6IjhiZmRiZmRkLWM4OGYtNGE5Yi04NzI3LWQ0ZGYzYWE5OTJlOSIsInR5cCI6IkpXVCJ9.eyJhY2NvdW50IjoiMTgyMjI3MDY5ODYiLCJleHAiOjIwNjEwODMwOTgsIm5iZiI6MTc0NTU1MDI5OCwib3JnYW5pemF0aW9uX3V1aWQiOiI3YjgxYTM1YS0yNTVkLTQ1NjUtOGFiNy04NzE3MWNkM2MxZDUiLCJwcm9qZWN0X3V1aWQiOiIiLCJzdWIiOiJmaDIiLCJ1c2VyX2lkIjoiMTc3MDAwODc2NzI3NTAxMjA5NiJ9.JJGGFjHFy-vIhx9m39E6CCaDz1v5rF5_7gQUYJ-hInu8SBjJZEeTS2k9CfQVfqm4phKSkUFA4GZRPfrqfCqlvg"

# 项目 uuid
project_uuid = "b96b008f-f9b6-4686-acd0-446a07d2488a"


conn = http.client.HTTPSConnection(url_prefix)


""" 获取系统状态
 正常响应：
 {"code":0,"message":""}
"""


def get_system_status():
    payload = ""
    headers = {"X-Request-Id": "", "X-Language": "zh", "X-User-Token": token}
    conn.request("GET", "/openapi/v0.1/system_status", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))


"""获取组织下的设备列表
正常响应：
{
    "code": 0,
    "message": "",
    "data": {
        "list": [
            {
                "gateway": {
                    "sn": "7CTXN2T00B07DK",
                    "callsign": "高楼变机场",
                    "device_model": {
                        "key": "3-2-0",
                        "domain": "3",
                        "type": "2",
                        "sub_type": "0",
                        "name": "DJI Dock 2",
                        "class": "airport"
                    },
                    "device_online_status": true,
                    "mode_code": 2,
                    "camera_list": [
                        {
                            "camera_index": "165-0-7",
                            "available_camera_positions": [
                                "indoor",
                                "outdoor"
                            ],
                            "camera_position": "indoor"
                        }
                    ]
                },
                "drone": {
                    "sn": "1581F6Q8X252U00G05EA",
                    "callsign": "M3TD-2",
                    "device_model": {
                        "key": "0-91-1",
                        "domain": "0",
                        "type": "91",
                        "sub_type": "1",
                        "name": "M3TD",
                        "class": "drone"
                    },
                    "device_online_status": true,
                    "mode_code": 0,
                    "camera_list": [
                        {
                            "camera_index": "176-0-0",
                            "lens_list": [
                                {
                                    "available_lens_types": [
                                        "normal"
                                    ],
                                    "lens_type": "normal"
                                }
                            ]
                        },
                        {
                            "camera_index": "81-0-0",
                            "lens_list": [
                                {
                                    "available_lens_types": [
                                        "normal",
                                        "wide",
                                        "zoom",
                                        "ir"
                                    ],
                                    "lens_type": "wide"
                                }
                            ]
                        }
                    ]
                }
            },
            {
                "gateway": {
                    "sn": "7CTXN2T00B07CV",
                    "callsign": "景和变机场",
                    "device_model": {
                        "key": "3-2-0",
                        "domain": "3",
                        "type": "2",
                        "sub_type": "0",
                        "name": "DJI Dock 2",
                        "class": "airport"
                    },
                    "device_online_status": false,
                    "mode_code": 0,
                    "camera_list": [
                        {
                            "camera_index": "165-0-7",
                            "available_camera_positions": [
                                "indoor",
                                "outdoor"
                            ],
                            "camera_position": "outdoor"
                        }
                    ]
                },
                "drone": {
                    "sn": "1581F6Q8X252U00G05HK",
                    "callsign": "M3TD-1",
                    "device_model": {
                        "key": "0-91-1",
                        "domain": "0",
                        "type": "91",
                        "sub_type": "1",
                        "name": "M3TD",
                        "class": "drone"
                    },
                    "device_online_status": false,
                    "mode_code": 0,
                    "camera_list": [
                        {
                            "camera_index": "176-0-0",
                            "lens_list": [
                                {
                                    "available_lens_types": [
                                        "normal"
                                    ],
                                    "lens_type": "normal"
                                }
                            ]
                        },
                        {
                            "camera_index": "81-0-0",
                            "lens_list": [
                                {
                                    "available_lens_types": [
                                        "normal",
                                        "wide",
                                        "zoom",
                                        "ir"
                                    ],
                                    "lens_type": "wide"
                                }
                            ]
                        }
                    ]
                }
            },
            {
                "gateway": {
                    "sn": "7CTXN3500B07PV",
                    "callsign": "灾备中心机场",
                    "device_model": {
                        "key": "3-2-0",
                        "domain": "3",
                        "type": "2",
                        "sub_type": "0",
                        "name": "DJI Dock 2",
                        "class": "airport"
                    },
                    "device_online_status": false,
                    "mode_code": 0,
                    "camera_list": [
                        {
                            "camera_index": "165-0-7",
                            "available_camera_positions": [
                                "indoor",
                                "outdoor"
                            ],
                            "camera_position": "outdoor"
                        }
                    ]
                },
                "drone": {
                    "sn": "1581F6Q8X252U00G05FH",
                    "callsign": "M3TD",
                    "device_model": {
                        "key": "0-91-1",
                        "domain": "0",
                        "type": "91",
                        "sub_type": "1",
                        "name": "M3TD",
                        "class": "drone"
                    },
                    "device_online_status": false,
                    "mode_code": 0,
                    "camera_list": null
                }
            }
        ]
    }
}
"""


def get_device():
    payload = ""
    headers = {"X-Request-Id": "", "X-Language": "zh", "X-User-Token": token}
    conn.request("GET", "/openapi/v0.1/device", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))


""" 获取项目列表
成功响应：
{
  "code": 0,
  "message": "",
  "data": {
    "list": [
      {
        "name": "海南项目",
        "introduction": "",
        "uuid": "6155f624-17c5-4e3f-b03c-fe4cb64cacfc",
        "org_uuid": "676f28d2-3585-41af-918d-b59b4950b590",
        "project_work_center_point": {
          "latitude": 19.85376891504428,
          "longitude": 110.38023592536878
        },
        "created_at": 1745214300,
        "updated_at": 1745214300
      },
      {
        "name": "昆嵛山",
        "introduction": "",
        "uuid": "a433adf9-35b8-4dc2-9d44-d30fc24c17c1",
        "org_uuid": "676f28d2-3585-41af-918d-b59b4950b590",
        "project_work_center_point": {
          "latitude": 37.565270885116625,
          "longitude": 121.17672555296284
        },
        "created_at": 1745196116,
        "updated_at": 1745196116
      },
      {
        "name": "0419保障",
        "introduction": "",
        "uuid": "0aee7d07-24ba-4d85-a588-b740a9b68f9a",
        "org_uuid": "676f28d2-3585-41af-918d-b59b4950b590",
        "project_work_center_point": {
          "latitude": 37.60870650498788,
          "longitude": 121.12953478005348
        },
        "created_at": 1744008679,
        "updated_at": 1745218387
      },
      {
        "name": "新疆项目",
        "introduction": "",
        "uuid": "37a9d3ef-7d75-4706-a015-f760f0c39814",
        "org_uuid": "676f28d2-3585-41af-918d-b59b4950b590",
        "project_work_center_point": {
          "latitude": 44.27926853843641,
          "longitude": 87.73868027592721
        },
        "created_at": 1741143033,
        "updated_at": 1745227962
      }
    ]
  }
}
"""


def get_project():

    payload = ""
    headers = {"X-Request-Id": "", "X-Language": "zh", "X-User-Token": token}
    conn.request("GET", "/openapi/v0.1/project", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))


"""获取项目下的设备
成功响应：


"""


def get_project_device():
    payload = ""
    headers = {
        "X-Request-Id": "",
        "X-Language": "zh",
        "X-Project-Uuid": project_uuid,
        "X-User-Token": token,
    }
    conn.request("GET", "/openapi/v0.1/project/device", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))


"""
获取物模型
成功响应：


"""


def get_model(device_sn):

    payload = ""
    headers = {
        "X-Request-Id": "",
        "X-Language": "zh",
        "X-Project-Uuid": project_uuid,
        "X-User-Token": token,
    }
    conn.request("GET", f"/openapi/v0.1/device/{device_sn}/state", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))


"""开启直播
成功响应：
示例1：
{
    "code": 0,
    "message": "",
    "data": {
        "expire_ts": 1745375258,
        "url": "app_id=668f8a70f1f998012921dc72&expire_time=1745375258&room_id=1581F6Q8X252U00G05EA_176-0-0&token=001668f8a70f1f998012921dc72XAAB%2F1cAukYIaBpQCGgcADE1ODFGNlE4WDI1MlUwMEcwNUVBXzE3Ni0wLTAoAHdpbmRvd18xNzcwMDA4NzY3Mjc1MDEyMDk2XzE3NDUzNzI4NTczMzMBAAQAGlAIaCAAKSOG71HyqJuyhSUP5flrXzb8zF0QwojimRnH5LZGIIE%3D&user_id=window_1770008767275012096_1745372857333",
        "url_type": "volc"
    }
}

示例2：

"""


def start_live():

    # 设备名称：M3TD-2 ； 设备型号：M3TD
    # 81-0-0
    # 176-0-0
    payload = json.dumps(
        {
            "sn": "1581F6Q8X252U00G05EA",
            "camera_index": "176-0-0",
            "video_expire": 7200,
            "video_quality": "adaptive",
        }
    )
    headers = {
        "X-Request-Id": "",
        "X-Language": "zh",
        "X-Project-Uuid": project_uuid,
        "Content-Type": "application/json",
        "X-User-Token": token,
    }
    conn.request("POST", "/openapi/v0.1/live-stream/start", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))


"""
司空2 OpenApi 接口调用示例：
接口文档：https://apifox.com/apidoc/shared/6b4ca90b-233f-48ac-818c-d694acb0663a/api-229642876

"""
if __name__ == "__main__":
    get_system_status()
    # get_project()
    # get_device()
    # get_project_device()
    # 无人机 ： M3TD
    # get_model("1581F6Q8X252U00G05FH")

    # start_live()
