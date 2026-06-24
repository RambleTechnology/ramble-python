"""
车辆检测 Demo — 基于 YOLOv8
用法：
    python detect.py --source 0          # 摄像头实时检测
    python detect.py --source video.mp4  # 视频文件
    python detect.py --source image.jpg  # 单张图片
"""

import argparse
import time
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict

import cv2
from ultralytics import YOLO


# ── 配置区 ─────────────────────────────────────────────
MODEL_PATH   = "yolov8n.pt"   # 首次运行会自动下载（约6MB）
CONF_THRESH  = 0.45           # 置信度阈值，低于此值的检测结果忽略
IOU_THRESH   = 0.5            # NMS的IOU阈值，越小框越少
IMG_SIZE     = 640            # 推理分辨率

# COCO数据集中车辆相关的类别ID（固定值，不要改）
VEHICLE_CLASSES = {
    2:  "car",
    3:  "motorcycle",
    5:  "bus",
    7:  "truck",
    1:  "bicycle",
}

# 每种车辆的颜色（BGR格式）
CLASS_COLORS = {
    2: (0,   200, 100),   # car     → 绿色
    3: (0,   150, 255),   # moto    → 橙色
    5: (255,  50,  50),   # bus     → 蓝色
    7: (180,   0, 255),   # truck   → 紫色
    1: (0,   220, 220),   # bicycle → 黄色
}
DEFAULT_COLOR = (180, 180, 180)
# ── 配置区结束 ──────────────────────────────────────────


def draw_box(frame, x1, y1, x2, y2, label, conf, color):
    """在帧上画检测框和标签"""
    # 框
    cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

    # 标签背景
    text = f"{label} {conf:.0%}"
    (tw, th), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.55, 1)
    tag_y = max(y1 - 4, th + 4)
    cv2.rectangle(frame, (x1, tag_y - th - 4), (x1 + tw + 6, tag_y + 2), color, -1)

    # 文字
    cv2.putText(frame, text, (x1 + 3, tag_y - 2),
                cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 1, cv2.LINE_AA)


def draw_stats(frame, counts, fps, total):
    """左上角绘制统计面板"""
    panel_h = 30 + len(counts) * 22 + 28
    overlay = frame.copy()
    cv2.rectangle(overlay, (8, 8), (220, 8 + panel_h), (20, 20, 20), -1)
    cv2.addWeighted(overlay, 0.6, frame, 0.4, 0, frame)

    cv2.putText(frame, f"FPS: {fps:.1f}  Total: {total}",
                (14, 28), cv2.FONT_HERSHEY_SIMPLEX, 0.52, (220, 220, 220), 1)

    y = 50
    for cls_id, cnt in sorted(counts.items(), key=lambda x: -x[1]):
        color = CLASS_COLORS.get(cls_id, DEFAULT_COLOR)
        name  = VEHICLE_CLASSES.get(cls_id, "vehicle")
        cv2.putText(frame, f"  {name:<12} {cnt}",
                    (14, y), cv2.FONT_HERSHEY_SIMPLEX, 0.48, color, 1)
        y += 22

    cv2.putText(frame, datetime.now().strftime("%H:%M:%S"),
                (14, y + 6), cv2.FONT_HERSHEY_SIMPLEX, 0.44, (140, 140, 140), 1)


def save_log(log_path, records):
    """把检测记录存成JSON，方便后续分析"""
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)
    print(f"\n检测日志已保存：{log_path}（共 {len(records)} 条记录）")


def run(source, save_video=False, save_log_file=True):
    # ── 加载模型 ──────────────────────────────────────────
    print(f"加载模型 {MODEL_PATH} ...")
    model = YOLO(MODEL_PATH)
    print("模型加载完成\n")

    # ── 打开视频源 ────────────────────────────────────────
    is_camera = str(source) == "0"
    cap_src   = 0 if is_camera else str(source)
    cap = cv2.VideoCapture(cap_src)

    if not cap.isOpened():
        raise RuntimeError(f"无法打开视频源：{source}")

    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps_src = cap.get(cv2.CAP_PROP_FPS) or 30.0
    print(f"视频源：{source}  分辨率：{width}x{height}  FPS：{fps_src:.1f}\n")

    # ── 可选：保存输出视频 ────────────────────────────────
    writer = None
    if save_video:
        out_path = f"output_{datetime.now():%Y%m%d_%H%M%S}.mp4"
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        writer = cv2.VideoWriter(out_path, fourcc, fps_src, (width, height))
        print(f"输出视频：{out_path}")

    # ── 主循环 ────────────────────────────────────────────
    records     = []           # 日志记录
    frame_idx   = 0
    prev_time   = time.time()
    fps_display = 0.0

    print("开始检测，按 Q 退出 / 按 S 截图\n")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("视频读取完毕")
            break

        frame_idx += 1
        ts = datetime.now().isoformat(timespec="milliseconds")

        # ── 推理 ──────────────────────────────────────────
        results = model(
            frame,
            conf=CONF_THRESH,
            iou=IOU_THRESH,
            imgsz=IMG_SIZE,
            verbose=False,
            classes=list(VEHICLE_CLASSES.keys()),  # 只检测车辆类别
        )[0]

        # ── 解析结果 ──────────────────────────────────────
        counts      = defaultdict(int)
        frame_recs  = []

        for box in results.boxes:
            cls_id = int(box.cls[0])
            if cls_id not in VEHICLE_CLASSES:
                continue

            conf  = float(box.conf[0])
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            name  = VEHICLE_CLASSES[cls_id]
            color = CLASS_COLORS.get(cls_id, DEFAULT_COLOR)

            counts[cls_id] += 1
            draw_box(frame, x1, y1, x2, y2, name, conf, color)

            frame_recs.append({
                "class": name,
                "conf": round(conf, 3),
                "box": [x1, y1, x2, y2],
            })

        # 把本帧有检测结果时记录日志
        if frame_recs and save_log_file:
            records.append({
                "frame": frame_idx,
                "time":  ts,
                "total": sum(counts.values()),
                "counts": {VEHICLE_CLASSES[k]: v for k, v in counts.items()},
                "detections": frame_recs,
            })

        # ── 计算FPS ──────────────────────────────────────
        now = time.time()
        fps_display = 0.9 * fps_display + 0.1 * (1.0 / (now - prev_time + 1e-6))
        prev_time = now

        # ── 绘制统计面板 ──────────────────────────────────
        draw_stats(frame, counts, fps_display, sum(counts.values()))

        # ── 显示 / 写入 ───────────────────────────────────
        cv2.imshow("Vehicle Detection — press Q to quit", frame)
        if writer:
            writer.write(frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            print("用户退出")
            break
        elif key == ord("s"):
            shot = f"screenshot_{datetime.now():%H%M%S}.jpg"
            cv2.imwrite(shot, frame)
            print(f"截图已保存：{shot}")

    # ── 清理 ──────────────────────────────────────────────
    cap.release()
    if writer:
        writer.release()
    cv2.destroyAllWindows()

    if save_log_file and records:
        log_path = f"detections_{datetime.now():%Y%m%d_%H%M%S}.json"
        save_log(log_path, records)

    # 打印汇总
    total_vehicles = sum(r["total"] for r in records)
    print(f"\n共处理 {frame_idx} 帧，检测到车辆 {total_vehicles} 次")


# ── 入口 ─────────────────────────────────────────────────
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YOLOv8 车辆检测 Demo")
    parser.add_argument("--source",     default="0",        help="视频源：0=摄像头 / 视频路径 / 图片路径")
    parser.add_argument("--save-video", action="store_true", help="保存检测后的视频")
    parser.add_argument("--no-log",     action="store_true", help="不保存JSON日志")
    args = parser.parse_args()

    run(
        source=args.source,
        save_video=args.save_video,
        save_log_file=not args.no_log,
    )
