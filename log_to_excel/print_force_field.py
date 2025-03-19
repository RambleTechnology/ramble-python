import json
import csv
from datetime import datetime

# 文件路径，替换成你的文件路径
file_path = "log_to_json.json"

# 打开并读取文件
with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        try:
            # 解析每一行的 JSON 字符串
            data = json.loads(line.strip())

            # 获取 params 字段中的嵌套 JSON 字符串
            params = json.loads(data["params"])

            # 提取 events 列表中的数据
            for event in params.get("events", []):
                # 获取 data 字段
                event_data = event.get("data", {})

                # 获取并打印所需的字段
                send_time = event_data.get("sendTime", "N/A")
                if "gpsCollection" in event_data:
                    for gps_data in event_data["gpsCollection"]:
                        uav_status = gps_data.get("UAVStatus", {})
                        gs_status = gps_data.get("GSStatus", {})

                        relative_height = uav_status.get("RelativeHeight", "N/A")
                        longitude = uav_status.get("Longitude", "N/A")
                        latitude = uav_status.get("Latitude", "N/A")
                        gimbal_yaw = gs_status.get("GimbalYaw", "N/A")
                        gimbal_pitch_angle = gs_status.get("GimbalPitchAngle", "N/A")
                        # 如果 gimbal_pitch_angle 和 gimbal_yaw 有值，则除以100
                        if gimbal_pitch_angle is not None:
                            gimbal_pitch_angle /= 100

                        if gimbal_yaw is not None:
                            gimbal_yaw /= 100

                        # 解析 sendTime，将其拆分为 年月日 时分秒
                        dt = datetime.fromisoformat(send_time)
                        date_year = dt.year
                        date_month = dt.month
                        date_day = dt.day
                        date_hour = dt.hour
                        date_minute = dt.minute
                        date_second = dt.second
                        # 打印提取到的字段
                        print(f"sendTime: {send_time}")
                        print(
                            f"{date_year}年{date_month}月{date_day}日{date_hour}时{date_minute}分{date_second}秒"
                        )
                        print(f"RelativeHeight: {relative_height}")
                        print(f"Longitude: {longitude}")
                        print(f"Latitude: {latitude}")
                        print(f"GimbalYaw: {gimbal_yaw}")
                        print(f"GimbalPitchAngle: {gimbal_pitch_angle}")
                        print("-" * 40)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
        except KeyError as e:
            print(f"Missing key: {e}")
