import json
import csv
from datetime import datetime

# 文件路径，替换成你的文件路径
file_path = "log_to_json.json"
csv_filename = "output.csv"

# 存储所有提取的数据
rows = []

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

                # 获取所需字段
                send_time = event_data.get("sendTime", "N/A")
                if "gpsCollection" in event_data:
                    for gps_data in event_data["gpsCollection"]:
                        uav_status = gps_data.get("UAVStatus", {})
                        gs_status = gps_data.get("GSStatus", {})

                        relative_height = uav_status.get("RelativeHeight", "N/A")
                        if relative_height is not None:
                            relative_height = relative_height * 1000
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

                        # 将提取的数据存储在 rows 列表中
                        rows.append(
                            {
                                "DATE_year": date_year,
                                "DATE_month": date_month,
                                "DATE_day": date_day,
                                "DATE_hour": date_hour,
                                "DATE_minute": date_minute,
                                "DATE_second": date_second,
                                "GPS_alt": relative_height,
                                "APEN_z": "55555",  # 留空
                                "GIMS_roll":"",
                                "GIMS_pitch": gimbal_pitch_angle,  # 留空
                                "GIM1_ym": gimbal_yaw,  # 留空
                                "APEG_gla": latitude,
                                "APEG_glo": longitude,
                            }
                        )

        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
        except KeyError as e:
            print(f"Missing key: {e}")

# 按时间对数据进行排序
rows.sort(
    key=lambda x: datetime(
        x["DATE_year"],
        x["DATE_month"],
        x["DATE_day"],
        x["DATE_hour"],
        x["DATE_minute"],
        x["DATE_second"],
    )
)

# 创建 CSV 文件并写入数据
with open(csv_filename, mode="w", newline="", encoding="utf-8") as csvfile:
    # 定义 CSV 文件的列名
    fieldnames = [
        "DATE_year",
        "DATE_month",
        "DATE_day",
        "DATE_hour",
        "DATE_minute",
        "DATE_second",
        "GPS_alt",
        "APEN_z",
        "GIMS_roll",
        "GIMS_pitch",
        "GIM1_ym",
        "APEG_gla",
        "APEG_glo",
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # 写入列名
    writer.writeheader()

    # 写入所有排序后的数据
    writer.writerows(rows)

print(f"数据已按时间正序写入到 {csv_filename}")
