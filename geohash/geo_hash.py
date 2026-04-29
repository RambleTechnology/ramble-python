import psycopg2
import json
import geohash
from shapely.geometry import Polygon

from coord_utils import bd09_to_wgs84, wgs84_to_bd09


def geohash_cell_size_dynamic(lat, precision):
    """返回 geohash 精度对应的经纬度步长"""
    # 用中心点生成 geohash，然后计算 bbox 宽高
    h = geohash.encode(lat, 0, precision)
    bbox = geohash.bbox(h)
    width = bbox["e"] - bbox["w"]
    height = bbox["n"] - bbox["s"]
    return width, height


# ---------------- 多边形生成 Geohash ----------------
def geohash_cover_polygon(polygon, precision=7):
    minx, miny, maxx, maxy = polygon.bounds
    # 初始步长用中心纬度动态计算
    center_lat = (miny + maxy) / 2
    step_lng, step_lat = geohash_cell_size_dynamic(center_lat, precision)
    hashes = set()

    lat = miny
    while lat <= maxy:
        lng = minx
        while lng <= maxx:
            h = geohash.encode(lat, lng, precision)
            bbox = geohash.bbox(h)
            cell = Polygon(
                [
                    (bbox["w"], bbox["s"]),
                    (bbox["e"], bbox["s"]),
                    (bbox["e"], bbox["n"]),
                    (bbox["w"], bbox["n"]),
                ]
            )
            if polygon.intersects(cell):
                hashes.add(h)
            lng += step_lng
        lat += step_lat
    return hashes


# ---------------- 主处理函数 ----------------
def process_region_fences(db_config, precision=7):
    """
    处理 bams_region 表 electronic_fence 字段
    返回字典： {region_id: set(geohash)}
    """
    conn = psycopg2.connect(
        host=db_config["host"],
        port=db_config["port"],
        database=db_config["database"],
        user=db_config["user"],
        password=db_config["password"],
    )
    cursor = conn.cursor()

    # 005001 = cml测试区划
    # 001012004 = 和平区
    sql = """
    SELECT id, electronic_fence
    FROM "ngh-smart-bams".bams_region
    WHERE electronic_fence IS NOT NULL and region_id = '001012004' and  is_leaf = 1
    """
    cursor.execute(sql)
    rows = cursor.fetchall()

    result = {}
    for row in rows:
        region_id = row[0]
        fence_json = json.loads(row[1])
        region_geohash_set = set()

        # 多围栏处理
        for polygon_points in fence_json:
            points = []
            for p in polygon_points:
                wgs_lng, wgs_lat = bd09_to_wgs84(p["lng"], p["lat"])
                points.append((wgs_lng, wgs_lat))
            polygon = Polygon(points)
            hashes = geohash_cover_polygon(polygon, precision)
            region_geohash_set.update(hashes)

        result[region_id] = region_geohash_set

    cursor.close()
    conn.close()
    return result


# ---------------- Geohash 反解析为 BD09 多边形 ----------------
def geohash_to_bd09_polygon(h):
    bbox = geohash.bbox(h)
    points_wgs84 = [
        (bbox["w"], bbox["s"]),
        (bbox["e"], bbox["s"]),
        (bbox["e"], bbox["n"]),
        (bbox["w"], bbox["n"]),
        (bbox["w"], bbox["s"]),  # 封闭多边形
    ]
    # 转回 BD09
    points_bd09 = [wgs84_to_bd09(lng, lat) for lng, lat in points_wgs84]
    return points_bd09


# ---------------- main 方法 ----------------
def main():
    db_config = {
        "host": "192.168.1.132",
        "port": 5432,
        "database": "ngh_cprh",
        "user": "postgres",
        "password": "J48Y5zVo1rpo7o25",
    }

    precision = 7  # geohash 精度
    region_geohash_map = process_region_fences(db_config, precision)

    # 输出结果
    for region_id, geohashes in region_geohash_map.items():
        print(f"region_id: {region_id}, total geohash: {len(geohashes)}")
        print(geohashes)
        print("-------------------------------------------------")

        # 反解析成 BD09 多边形
        bd09_polygons = []
        for h in geohashes:
            bd_polygon = geohash_to_bd09_polygon(h)
            bd09_polygons.append(bd_polygon)

        # 1.直接打印
        # print(f"region_id: {region_id}, total BD09 polygons: {len(bd09_polygons)}")
        # # 打印前 5 个 polygon 示例
        # for i, poly in enumerate(bd09_polygons):
        #     print(poly)

        # 2.保存到文件
        # 将每个 polygon 转成 [[lng, lat], ...] 格式（如果本身是 (lng, lat) 元组）
        formatted_polygons = []
        for poly in bd09_polygons:
            formatted_poly = [[lng, lat] for lng, lat in poly]
            formatted_polygons.append(formatted_poly)

        # 保存到文件，例如 bd09_polygons.json
        with open(f"region_{region_id}_bd09_polygons.json", "w", encoding="utf-8") as f:
            json.dump(formatted_polygons, f, ensure_ascii=False, indent=4)

        print(
            f"保存完成，共 {len(formatted_polygons)} 个多边形到 region_{region_id}_bd09_polygons.json"
        )


# ---------------- 脚本入口 ----------------
if __name__ == "__main__":
    main()
