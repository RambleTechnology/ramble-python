"""
日志分析脚本 — analyze.py
把 detect.py 生成的 JSON 日志可视化，输出统计报告和折线图

用法：
    python analyze.py detections_20240101_120000.json
"""

import json
import sys
import argparse
from collections import Counter
from pathlib import Path


def load_log(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def print_summary(records):
    total_frames_with_vehicles = len(records)
    all_detections = []

    for rec in records:
        for d in rec["detections"]:
            all_detections.append(d["class"])

    counter = Counter(all_detections)

    print("=" * 45)
    print("  车辆检测统计报告")
    print("=" * 45)
    print(f"  有车辆的帧数：{total_frames_with_vehicles}")
    print(f"  累计检测次数：{len(all_detections)}")
    print()
    print("  各类型车辆分布：")
    for name, cnt in counter.most_common():
        bar = "█" * (cnt * 30 // max(counter.values()))
        pct = cnt / len(all_detections) * 100
        print(f"    {name:<12} {cnt:>4}次  {pct:>5.1f}%  {bar}")
    print("=" * 45)

    # 找到车辆最密集的帧
    if records:
        peak = max(records, key=lambda r: r["total"])
        print(f"\n  高峰帧：第 {peak['frame']} 帧  时间：{peak['time']}")
        print(f"  当时车辆数：{peak['total']}")
        for cls, cnt in peak["counts"].items():
            print(f"    - {cls}: {cnt}")


def plot_timeline(records):
    """用 matplotlib 画车辆数量时间折线图（如果没装就跳过）"""
    try:
        import matplotlib.pyplot as plt
        import matplotlib
        matplotlib.use("Agg")  # 无头模式

        frames = [r["frame"] for r in records]
        totals = [r["total"] for r in records]

        # 各类型单独一条线
        class_names = set()
        for r in records:
            class_names.update(r["counts"].keys())

        fig, ax = plt.subplots(figsize=(12, 5))
        ax.plot(frames, totals, color="#2196F3", linewidth=2, label="总计", zorder=5)

        colors = ["#4CAF50", "#FF9800", "#E91E63", "#9C27B0", "#00BCD4"]
        for i, cls in enumerate(sorted(class_names)):
            vals = [r["counts"].get(cls, 0) for r in records]
            ax.fill_between(frames, vals, alpha=0.25, color=colors[i % len(colors)])
            ax.plot(frames, vals, linewidth=1, label=cls,
                    color=colors[i % len(colors)])

        ax.set_xlabel("帧编号")
        ax.set_ylabel("检测到的车辆数")
        ax.set_title("车辆数量时间分布")
        ax.legend(loc="upper right")
        ax.grid(True, alpha=0.3)
        fig.tight_layout()

        out = "vehicle_timeline.png"
        fig.savefig(out, dpi=150)
        print(f"\n  时间折线图已保存：{out}")

    except ImportError:
        print("\n  （安装 matplotlib 后可生成折线图：pip install matplotlib）")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("log", help="detect.py 输出的 JSON 日志路径")
    parser.add_argument("--no-plot", action="store_true")
    args = parser.parse_args()

    records = load_log(args.log)
    print_summary(records)
    if not args.no_plot:
        plot_timeline(records)
