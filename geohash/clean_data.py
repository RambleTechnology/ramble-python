import psycopg2
import json
import geohash
from shapely.geometry import Polygon

from coord_utils import bd09_to_wgs84


db_config = {
        "host": "192.168.1.132",
        "port": 5432,
        "database": "ngh_cprh",
        "user": "postgres",
        "password": "J48Y5zVo1rpo7o25",
    }
# 初始化数据库连接对象
def init_db():
    conn = psycopg2.connect(
        host=db_config["host"],
        port=db_config["port"],
        database=db_config["database"],
        user=db_config["user"],
        password=db_config["password"],
    )
    cursor = conn.cursor()
    return conn, cursor

# 查询数据
def find_region():
    sql = """
    SELECT region_id, electronic_fence
    FROM "ngh-smart-bams".bams_region
    WHERE electronic_fence IS NOT NULL and region_id = '001012004' and  is_leaf = 1
    """
    conn, cursor = init_db()
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def geohash_cell_size_dynamic(lat, precision):
    """返回 geohash 精度对应的经纬度步长"""
    h = geohash.encode(lat, 0, precision)
    bbox = geohash.bbox(h)
    width = bbox["e"] - bbox["w"]
    height = bbox["n"] - bbox["s"]
    return width, height


def geohash_cover_polygon(polygon, precision=7):
    minx, miny, maxx, maxy = polygon.bounds
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
def main():
    precision = 7
    rows = find_region()

    if not rows:
        print("没有查询到需要处理的数据。")
        return

    conn, cursor = init_db()

    insert_sql = """
    INSERT INTO region_geohash (region_id, geohash, geohash_length, creatad_at)
    VALUES (%s, %s, %s, NOW())
    """

    total_inserted = 0
    for row in rows:
        region_id = row[0]
        fence_json = json.loads(row[1])
        region_geohash_set = set()

        for polygon_points in fence_json:
            points = []
            for p in polygon_points:
                wgs_lng, wgs_lat = bd09_to_wgs84(p["lng"], p["lat"])
                points.append((wgs_lng, wgs_lat))
            polygon = Polygon(points)
            hashes = geohash_cover_polygon(polygon, precision)
            region_geohash_set.update(hashes)

        if region_geohash_set:
            records = [
                (region_id, h, len(h))
                for h in region_geohash_set
            ]
            cursor.executemany(insert_sql, records)
            total_inserted += len(records)

    conn.commit()
    cursor.close()
    conn.close()

    print(f"处理完成，写入 geohash 数量：{total_inserted}")


if __name__ == "__main__":
    main()
