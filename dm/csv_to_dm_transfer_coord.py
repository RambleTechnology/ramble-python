#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CSV 数据治理脚本 - 导入到达梦数据库
支持幂等操作，多次导入不产生重复数据
坐标系：CSV 中为 WGS84，写入数据库前自动转换为 BD09
"""

import csv
import math
import sys
import logging
from datetime import datetime
from pathlib import Path

# ============================================================
# 依赖安装说明：
#   pip install dmPython
# 达梦官方驱动下载：https://eco.dameng.com/download/
# 若使用 JDBC 风格可改用 jaydebeapi：
#   pip install jaydebeapi JPype1
# ============================================================

# ---------- 日志配置 ----------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)


# ============================================================
# 数据库连接配置
# ============================================================
DB_CONFIG = {
    "host": "127.0.0.1",
    "port": 5236,
    "user": "SYSDBA",
    "password": "xxx",
    "database": "xxx",
}

TABLE_NAME = '"xxx".xxx'

# 固定默认值
DEFAULT_HAS_DEL = 0
DEFAULT_TYPE    = 0
DEFAULT_ORG_ID  = "xxx"



# ============================================================
# CSV 字段 → 数据库字段 映射
# ============================================================
FIELD_MAP = {
    "videoId":           "camera_index_code",   # VARCHAR / 唯一约束
    "isDeleted":         "hasDel",              # INT
    "c_device_name":     "name",                # VARCHAR
    "c_amap_longitude":  "longitude",           # DOUBLE（BD09，转换后写入）
    "c_amap_latitude":   "latitude",            # DOUBLE（BD09，转换后写入）
}


# ============================================================
# 坐标转换：WGS84 → GCJ02 → BD09
# ============================================================

_PI    = math.pi
_A     = 6378245.0          # 克拉索夫斯基椭球长半轴
_EE    = 0.00669342162296594323  # 第一偏心率平方
_BD_PI = _PI * 3000.0 / 180.0   # 百度坐标系专用 π


def _out_of_china(lon: float, lat: float) -> bool:
    """判断坐标是否在中国大陆范围之外（在范围外则无需偏移）。"""
    return not (72.004 <= lon <= 137.8347 and 0.8293 <= lat <= 55.8271)


def _transform_lat(lon: float, lat: float) -> float:
    ret = (-100.0 + 2.0 * lon + 3.0 * lat + 0.2 * lat * lat
           + 0.1 * lon * lat + 0.2 * math.sqrt(abs(lon)))
    ret += (20.0 * math.sin(6.0 * lon * _PI)
            + 20.0 * math.sin(2.0 * lon * _PI)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lat * _PI)
            + 40.0 * math.sin(lat / 3.0 * _PI)) * 2.0 / 3.0
    ret += (160.0 * math.sin(lat / 12.0 * _PI)
            + 320.0 * math.sin(lat * _PI / 30.0)) * 2.0 / 3.0
    return ret


def _transform_lon(lon: float, lat: float) -> float:
    ret = (300.0 + lon + 2.0 * lat + 0.1 * lon * lon
           + 0.1 * lon * lat + 0.1 * math.sqrt(abs(lon)))
    ret += (20.0 * math.sin(6.0 * lon * _PI)
            + 20.0 * math.sin(2.0 * lon * _PI)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lon * _PI)
            + 40.0 * math.sin(lon / 3.0 * _PI)) * 2.0 / 3.0
    ret += (150.0 * math.sin(lon / 12.0 * _PI)
            + 300.0 * math.sin(lon / 30.0 * _PI)) * 2.0 / 3.0
    return ret


def wgs84_to_gcj02(lon: float, lat: float):
    """WGS84 → GCJ02（火星坐标系）。"""
    if _out_of_china(lon, lat):
        return lon, lat

    d_lat = _transform_lat(lon - 105.0, lat - 35.0)
    d_lon = _transform_lon(lon - 105.0, lat - 35.0)

    rad_lat   = lat / 180.0 * _PI
    magic     = math.sin(rad_lat)
    magic     = 1 - _EE * magic * magic
    sqrt_magic = math.sqrt(magic)

    d_lat = (d_lat * 180.0) / ((_A * (1 - _EE)) / (magic * sqrt_magic) * _PI)
    d_lon = (d_lon * 180.0) / (_A / sqrt_magic * math.cos(rad_lat) * _PI)

    return lon + d_lon, lat + d_lat


def gcj02_to_bd09(lon: float, lat: float):
    """GCJ02（火星坐标系）→ BD09（百度坐标系）。"""
    z     = math.sqrt(lon * lon + lat * lat) + 0.00002 * math.sin(lat * _BD_PI)
    theta = math.atan2(lat, lon) + 0.000003 * math.cos(lon * _BD_PI)
    bd_lon = z * math.cos(theta) + 0.0065
    bd_lat = z * math.sin(theta) + 0.006
    return bd_lon, bd_lat


def wgs84_to_bd09(lon: float, lat: float):
    """WGS84 → BD09（两步转换，含边界判断）。"""
    if lon is None or lat is None:
        return lon, lat
    gcj_lon, gcj_lat = wgs84_to_gcj02(lon, lat)
    return gcj02_to_bd09(gcj_lon, gcj_lat)


# ============================================================
# 工具函数
# ============================================================


def parse_row(row: dict, current_time: str) -> dict:
    """将 CSV 行解析为目标字段字典，并进行类型转换 + GBK 清洗。
    坐标从 WGS84 转换为 BD09 后再写入。
    current_time 由调用方统一传入，保证同批次时间一致。
    """
    wgs_lon = _to_float(row.get("c_amap_longitude"))
    wgs_lat = _to_float(row.get("c_amap_latitude"))

    # WGS84 → BD09
    bd_lon, bd_lat = wgs84_to_bd09(wgs_lon, wgs_lat)

    record = {
        "camera_index_code": row.get("videoId", "").strip(),
        "name":              row.get("c_device_name", "").strip(),
        "longitude":         bd_lon,   # BD09 经度
        "latitude":          bd_lat,   # BD09 纬度
        "hasDel":            _to_int(row.get("isDeleted"), DEFAULT_HAS_DEL),
        "type":              DEFAULT_TYPE,
        "org_id":            DEFAULT_ORG_ID,
        "create_time":       current_time,  # 插入时写入，更新时不覆盖
        "update_time":       current_time,  # 插入和更新都写入
    }
    # 清洗无法 GBK 编码的字符（\ufffd 等）
    return sanitize_record(record)


# ============================================================
# 字符清洗：去除无法编码为 GBK 的字符
# ============================================================

def sanitize_for_gbk(value: str) -> str:
    """
    将字符串中无法用 GBK 编码的字符替换为空字符串。
    达梦在 GBK 字符集环境下写入时会报 codec 错误，需提前清洗。
    \ufffd 是 Unicode 替换字符，通常是原文件本身存在损坏字节导致的。
    """
    if not isinstance(value, str):
        return value
    return value.encode("gbk", errors="ignore").decode("gbk")


def sanitize_record(record: dict) -> dict:
    """对记录中所有字符串字段执行 GBK 清洗。"""
    return {
        k: sanitize_for_gbk(v) if isinstance(v, str) else v
        for k, v in record.items()
    }


def _to_float(value, default=None):
    try:
        return float(value) if value not in (None, "") else default
    except (ValueError, TypeError):
        return default


def _to_int(value, default=0):
    try:
        return int(value) if value not in (None, "") else default
    except (ValueError, TypeError):
        return default


def now_str() -> str:
    """返回当前时间字符串，格式：2026-05-14 02:00:07"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def detect_encoding(filepath: str) -> str:
    """
    自动检测文件编码。
    依次尝试常见编码，返回第一个可成功读取全文的编码。
    """
    for enc in ("utf-8-sig", "utf-8", "gbk", "gb2312", "latin-1"):
        try:
            with open(filepath, encoding=enc) as f:
                f.read()
            logger.info(f"文件编码检测为：{enc}")
            return enc
        except (UnicodeDecodeError, LookupError):
            continue
    return "latin-1"  # 最终兜底，不会再报 decode 错误


def read_csv(filepath: str) -> list:
    """读取 CSV 文件，返回解析后的字典列表（坐标已转换为 BD09）。"""
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"CSV 文件不存在：{filepath}")

    encoding = detect_encoding(filepath)

    records = []
    current_time = now_str()  # 同批次所有行使用同一时间戳
    # errors="replace"：将无法解码的字节替换为 \ufffd，后续 sanitize_for_gbk 再移除
    with open(path, newline="", encoding=encoding, errors="replace") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
              records.append(parse_row(row, current_time))
            except Exception as e:
                logger.error(f"解析CSV行失败，行数据：{row}，错误信息：{str(e)}")

    logger.info(f"读取到 {len(records)} 条记录（坐标已转换 WGS84→BD09），文件：{filepath}")
    return records


# ============================================================
# 达梦数据库操作（使用 dmPython）
# ============================================================

def get_connection():
    """创建达梦数据库连接（dmPython）。"""
    try:
        import dmPython  # noqa: F401  达梦官方 Python 驱动
    except ImportError:
        raise ImportError(
            "未找到 dmPython 模块。\n"
            "请从达梦官网下载驱动并安装：https://eco.dameng.com/download/\n"
            "或执行：pip install dmPython"
        )

    conn = dmPython.connect(
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        server=DB_CONFIG["host"],
        port=DB_CONFIG["port"],
    )
    logger.info("数据库连接成功")
    return conn


MERGE_SQL = f"""
MERGE INTO {TABLE_NAME} AS target
USING (
    SELECT
        :xxx AS xxx,
        :name              AS name,
        :longitude         AS longitude,
        :latitude          AS latitude,
        :hasDel            AS hasDel,
        :type              AS type,
        :org_id            AS org_id,
        :create_time       AS create_time,
        :update_time       AS update_time
    FROM DUAL
) AS source
ON (target.xxx = source.xxx)
WHEN MATCHED THEN
    UPDATE SET
        target.name        = source.name,
        target.longitude   = source.longitude,
        target.latitude    = source.latitude,
        target.hasDel      = source.hasDel,
        target.type        = source.type,
        target.org_id      = source.org_id,
        target.update_time = source.update_time,
        target.source_type = 55,
        target.protocol    ='iframe'    
        -- create_time 更新时不覆盖，保留首次插入值
WHEN NOT MATCHED THEN
    INSERT (
        xxx,
        name,
        longitude,
        latitude,
        hasDel,
        type,
        org_id,
        create_time,
        update_time,
        source_type,
        protocol
    ) VALUES (
        source.xxx,
        source.name,
        source.longitude,
        source.latitude,
        source.hasDel,
        source.type,
        source.org_id,
        source.create_time,
        source.update_time,
        55,
        'iframe'
    )
"""


def print_progress(current: int, total: int, success: int, failed: int):
    """
    在同一行打印进度条，格式示例：
    进度: [====================] 100.0%  200/200  ✓成功:198  ✗失败:2
    """
    bar_width = 30
    ratio     = current / total if total else 1
    filled    = int(bar_width * ratio)
    bar       = "=" * filled + "-" * (bar_width - filled)
    percent   = ratio * 100

    line = (
        f"\r进度: [{bar}] {percent:5.1f}%  "
        f"{current}/{total}  "
        f"✓成功:{success}  ✗失败:{failed}"
    )
    sys.stdout.write(line)
    sys.stdout.flush()

    if current == total:
        sys.stdout.write("\n")
        sys.stdout.flush()


def upsert_records(conn, records: list):
    """幂等写入：MERGE INTO，camera_index_code 为唯一匹配键。"""
    if not records:
        logger.warning("没有可写入的记录")
        return

    cursor      = conn.cursor()
    total       = len(records)
    success     = 0
    failed      = 0
    failed_list = []

    logger.info(f"开始写入，共 {total} 条记录...")

    try:
        for idx, record in enumerate(records, start=1):
            try:
                cursor.execute(MERGE_SQL, record)
                success += 1
            except Exception as e:
                failed += 1
                cam_id = record.get("xxx", "UNKNOWN")
                # 先换行，避免进度条与错误日志混在一行
                sys.stdout.write("\n")
                logger.error(f"写入失败 xxx={cam_id}，原因：{e}")
                failed_list.append((cam_id, str(e)))

            # 每条都刷新进度（数据量大时可改为每 N 条刷新一次）
            print_progress(idx, total, success, failed)

        conn.commit()
        logger.info(f"写入完成：成功 {success} 条，失败 {failed} 条")

        if failed_list:
            logger.warning("=== 失败记录汇总 ===")
            for cam_id, reason in failed_list:
                logger.warning(f"  {cam_id}: {reason}")
    finally:
        cursor.close()


# ============================================================
# 备用方案：使用 jaydebeapi（JDBC 驱动）
# ============================================================

def get_connection_jdbc():
    """
    备用：通过 JDBC 连接达梦数据库（需要 jaydebeapi + JPype1 + DmJdbcDriver18.jar）。
    pip install jaydebeapi JPype1
    """
    try:
        import jaydebeapi
    except ImportError:
        raise ImportError("请执行：pip install jaydebeapi JPype1")

    jdbc_url = (
        "jdbc:dm://127.0.0.1:5236/xxx"
        "?useUnicode=true&allowMultiQueries=true"
        "&characterEncoding=utf8"
        "&zeroDateTimeBehavior=convertToNull"
        "&useSSL=true&serverTimezone=GMT%2B8"
        "&autoReconnect=true"
        "&rewriteBatchedStatements=true"
        "&nullCatalogMeansCurrent=true"
    )

    conn = jaydebeapi.connect(
        "dm.jdbc.driver.DmDriver",
        jdbc_url,
        [DB_CONFIG["user"], DB_CONFIG["password"]],
        "/path/to/DmJdbcDriver18.jar",   # ← 修改为实际 jar 路径
    )
    logger.info("数据库连接成功（JDBC）")
    return conn


# ============================================================
# 主入口
# ============================================================

def main(csv_filepath: str, use_jdbc: bool = False):
    # 1. 读取 CSV（含坐标转换）
    records = read_csv(csv_filepath)

    # 2. 建立数据库连接
    if use_jdbc:
        conn = get_connection_jdbc()
    else:
        conn = get_connection()

    try:
        # 3. 幂等写入
        upsert_records(conn, records)
    finally:
        conn.close()
        logger.info("数据库连接已关闭")


if __name__ == "__main__":
    # 用法：
    #   python import_to_dm.py data.csv
    #   python import_to_dm.py data.csv --jdbc   # 使用 JDBC 驱动
    if len(sys.argv) < 2:
        print("用法：python import_to_dm.py <csv文件路径> [--jdbc]")
        sys.exit(1)

    csv_file = sys.argv[1]
    use_jdbc = "--jdbc" in sys.argv

    main(csv_file, use_jdbc=use_jdbc)