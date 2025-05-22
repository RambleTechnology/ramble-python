import paho.mqtt.client as mqtt
import time
from datetime import datetime
import uuid
import json
import random

# MQTT 连接设置
# BROKER = "111.33.143.195"
# PORT = 18083
BROKER = "112.230.197.170"
PORT = 1833
USER = "public"
PWD = "admin123456"


# 主题：thing/product/+/osd
osd_topic_prefix = "thing/product/"
osd_topic_suffix = "/osd"


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")


# 获取设备实时状态
def generate_json():
    # 生成 UUID 和当前时间戳
    tid = str(uuid.uuid4())
    bid = str(uuid.uuid4())
    timestamp = int(time.time() * 1000)  # 当前时间的毫秒级时间戳

    # 构建 JSON 对象
    json_object = {
        "tid": tid,
        "bid": bid,
        "timestamp": timestamp,
        "data": {
            "53-0-0": {
                "gimbal_pitch": 0,
                "gimbal_roll": 0,
                "gimbal_yaw": 107.7,
                "measure_target_altitude": 0,
                "measure_target_distance": 4.700000286102295,
                "measure_target_error_state": 3,
                "measure_target_latitude": 0,
                "measure_target_longitude": 0,
                "payload_index": "53-0-0",
                "thermal_current_palette_style": 0,
                "thermal_gain_mode": 2,
                "thermal_global_temperature_max": 26.598840713500977,
                "thermal_global_temperature_min": 8.69597816467285,
                "thermal_isotherm_lower_limit": -20,
                "thermal_isotherm_state": 0,
                "thermal_isotherm_upper_limit": 150,
            },
            "activation_time": 1669921424,
            "attitude_head": 107.7,
            "attitude_pitch": -4.2,
            "attitude_roll": -0.2,
            "battery": {
                "batteries": [
                    {
                        "capacity_percent": 81,
                        "firmware_version": "02.00.20.58",
                        "high_voltage_storage_days": 2,
                        "index": 0,
                        "loop_times": 22,
                        "sn": "4BUPK79DA120HG",
                        "sub_type": 0,
                        "temperature": 25.7,
                        "type": 0,
                        "voltage": 24250,
                    },
                    {
                        "capacity_percent": 80,
                        "firmware_version": "02.00.20.58",
                        "high_voltage_storage_days": 2,
                        "index": 1,
                        "loop_times": 22,
                        "sn": "4BUPK79DA120GC",
                        "sub_type": 0,
                        "temperature": 25.8,
                        "type": 0,
                        "voltage": 24234,
                    },
                ],
                "capacity_percent": 80,
                "landing_power": 0,
                "remain_flight_time": 0,
                "return_home_power": 0,
            },
            "cameras": [
                {
                    "camera_mode": 0,
                    "ir_metering_mode": 0,
                    "ir_metering_point": {"temperature": 0, "x": 0.5, "y": 0.5},
                    "ir_zoom_factor": 1,
                    "liveview_world_region": {
                        "bottom": 0.608518898487091,
                        "left": 0.3949633836746216,
                        "right": 0.5876559615135193,
                        "top": 0.41036492586135864,
                    },
                    "payload_index": "53-0-0",
                    "photo_state": 0,
                    "photo_storage_settings": ["current", "ir"],
                    "record_time": 0,
                    "recording_state": 0,
                    "remain_photo_num": 2175,
                    "remain_record_duration": 0,
                    "screen_split_enable": "false",
                    "wide_calibrate_farthest_focus_value": 0,
                    "wide_calibrate_nearest_focus_value": 0,
                    "wide_exposure_mode": 1,
                    "wide_exposure_value": 16,
                    "wide_focus_mode": 0,
                    "wide_focus_state": 0,
                    "wide_focus_value": 0,
                    "wide_iso": 6,
                    "wide_max_focus_value": 0,
                    "wide_min_focus_value": 0,
                    "wide_shutter_speed": 31,
                    "zoom_calibrate_farthest_focus_value": 200,
                    "zoom_calibrate_nearest_focus_value": 241,
                    "zoom_exposure_mode": 1,
                    "zoom_exposure_value": 16,
                    "zoom_factor": 1,
                    "zoom_focus_mode": 2,
                    "zoom_focus_state": 0,
                    "zoom_focus_value": 283,
                    "zoom_iso": 6,
                    "zoom_max_focus_value": 261,
                    "zoom_min_focus_value": 180,
                    "zoom_shutter_speed": 32,
                }
            ],
            "distance_limit_status": {
                "distance_limit": 0,
                "is_near_distance_limit": 0,
                "state": 0,
            },
            "elevation": 0,
            "exit_wayline_when_rc_lost": 1,
            "firmware_version": "10.01.0504",
            "gear": 1,
            "height": 1189.18359375,
            "height_limit": 0,
            "home_distance": 0,
            "horizontal_speed": 0,
            "is_near_height_limit": 0,
            "latitude": 0,
            "longitude": 0,
            "maintain_status": {
                "maintain_status_array": [
                    {
                        "last_maintain_flight_sorties": 0,
                        "last_maintain_flight_time": 0,
                        "last_maintain_time": 0,
                        "last_maintain_type": 1,
                        "state": 0,
                    },
                    {
                        "last_maintain_flight_sorties": 0,
                        "last_maintain_flight_time": 0,
                        "last_maintain_time": 0,
                        "last_maintain_type": 2,
                        "state": 0,
                    },
                    {
                        "last_maintain_flight_sorties": 0,
                        "last_maintain_flight_time": 0,
                        "last_maintain_time": 0,
                        "last_maintain_type": 3,
                        "state": 0,
                    },
                ]
            },
            "mode_code": 0,
            "night_lights_state": 0,
            "obstacle_avoidance": {"downside": 0, "horizon": 1, "upside": 0},
            "position_state": {
                "gps_number": 0,
                "is_fixed": 0,
                "quality": 0,
                "rtk_number": 0,
            },
            "rc_lost_action": 2,
            "rth_altitude": 260,
            "storage": {"total": 30131000, "used": 1000},
            "total_flight_distance": 246279.92617234506,
            "total_flight_sorties": 0,
            "total_flight_time": 0,
            "track_id": "",
            "vertical_speed": 0,
            "wind_direction": 0,
            "wind_speed": 0,
        },
        "gateway": "dock_sn",
    }

    return json.dumps(json_object, indent=4)


def publish_messages():
    # 创建 MQTT 客户端实例
    client = mqtt.Client()
    client.on_connect = on_connect
    client.username_pw_set(USER, PWD)

    # 连接到 MQTT 代理
    client.connect(BROKER, PORT, 60)

    # 启动网络循环
    client.loop_start()

    try:
        while True:
            # 发布消息到主题
            # sn = f"device{uuid.uuid1()}"
            sn = f"device{ random.randint(1, 9)}"
            device_sn = sn.replace("-", "")
            # timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # message = f"Hello from Program A! Timestamp: {timestamp}"
            topic = osd_topic_prefix + device_sn + osd_topic_suffix
            message = generate_json()
            client.publish(topic, message)
            print(f"Message '{message}' published to topic '{topic}'")
            # 等待 2 秒
            time.sleep(2)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        client.loop_stop()
        client.disconnect()


def main():
    publish_messages()


if __name__ == "__main__":
    main()
