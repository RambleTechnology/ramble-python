# 车辆检测 Demo — YOLOv8

基于 YOLOv8 的实时车辆检测，支持摄像头/视频文件/图片，
自动识别 car / truck / bus / motorcycle / bicycle，
生成 JSON 日志供后续统计分析。

---

## 快速开始

### 1. 安装依赖

```bash
pip install ultralytics opencv-python
```

> 首次运行会自动下载 YOLOv8n 模型权重（约 6MB），需要联网。

### 2. 运行检测

```bash
# 摄像头实时检测
python detect.py --source 0

# 视频文件
python detect.py --source road.mp4

# 同时保存检测后的视频
python detect.py --source road.mp4 --save-video
```

**运行时快捷键：**
- `Q` — 退出
- `S` — 保存当前帧截图

### 3. 分析检测日志

检测结束后会自动生成 JSON 日志，用 analyze.py 查看统计：

```bash
python analyze.py detections_20240101_120000.json
```

输出示例：
```
=============================================
  车辆检测统计报告
=============================================
  有车辆的帧数：1842
  累计检测次数：6731

  各类型车辆分布：
    car          4102次   61.0%  ████████████████████
    truck         987次   14.7%  ██████
    bus           723次   10.7%  ████
    motorcycle    612次    9.1%  ███
    bicycle       307次    4.6%  █
=============================================
```

---

## 文件说明

```
vehicle_detection/
├── detect.py       # 主检测脚本
├── analyze.py      # 日志分析脚本
└── README.md       # 本文件
```

检测运行后生成：
```
├── detections_YYYYMMDD_HHMMSS.json   # 每帧的检测详情
├── output_YYYYMMDD_HHMMSS.mp4        # 带标注框的视频（--save-video 时）
└── screenshot_HHMMSS.jpg             # 按 S 时的截图
```

---

## 调参说明

打开 `detect.py` 顶部的配置区：

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `MODEL_PATH` | `yolov8n.pt` | 模型大小：n < s < m < l < x，越大越准但越慢 |
| `CONF_THRESH` | `0.45` | 置信度阈值，调高减少误报，调低减少漏检 |
| `IOU_THRESH` | `0.5` | NMS 阈值，调低可减少重叠框 |
| `IMG_SIZE` | `640` | 推理分辨率，越大越准但越慢 |

**性能参考（CPU）：**
- yolov8n：~15 FPS，适合实时
- yolov8s：~8 FPS，精度更好
- yolov8m：~4 FPS，项目演示推荐

---

## JSON 日志格式

```json
[
  {
    "frame": 42,
    "time": "2024-01-01T12:00:01.500",
    "total": 3,
    "counts": { "car": 2, "truck": 1 },
    "detections": [
      { "class": "car",   "conf": 0.923, "box": [120, 200, 380, 420] },
      { "class": "car",   "conf": 0.871, "box": [450, 180, 680, 390] },
      { "class": "truck", "conf": 0.756, "box": [10,  150, 110, 350] }
    ]
  }
]
```

`box` 格式为 `[x1, y1, x2, y2]`，左上角和右下角坐标。

---

## 下一步扩展方向

1. **加追踪（Tracking）** — 让同一辆车保持同一个 ID，统计实际过车数量而非帧检测数
   ```python
   results = model.track(frame, persist=True, classes=list(VEHICLE_CLASSES.keys()))
   ```

2. **加越线告警** — 定义一条虚拟线，判断车辆中心点是否穿越

3. **接入 SAM** — 对检测到的车辆做精细轮廓分割，用于车牌区域提取

4. **接摄像头 RTSP 流** — 把 `--source 0` 换成 `rtsp://camera_ip/stream`
