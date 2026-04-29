import math


def bd09_to_gcj02(bd_lon, bd_lat):
    x = bd_lon - 0.0065
    y = bd_lat - 0.006
    z = math.sqrt(x * x + y * y) - 0.00002 * math.sin(y * math.pi * 3000.0 / 180.0)
    theta = math.atan2(y, x) - 0.000003 * math.cos(x * math.pi * 3000.0 / 180.0)
    gg_lng = z * math.cos(theta)
    gg_lat = z * math.sin(theta)
    return gg_lng, gg_lat


def gcj02_to_wgs84(lng, lat):
    return lng - 0.0002, lat - 0.0002


def bd09_to_wgs84(bd_lng, bd_lat):
    gcj_lng, gcj_lat = bd09_to_gcj02(bd_lng, bd_lat)
    wgs_lng, wgs_lat = gcj02_to_wgs84(gcj_lng, gcj_lat)
    return wgs_lng, wgs_lat


def wgs84_to_bd09(lng, lat):
    gcj_lng, gcj_lat = wgs84_to_gcj02(lng, lat)
    bd_lng, bd_lat = gcj02_to_bd09(gcj_lng, gcj_lat)
    return bd_lng, bd_lat


def wgs84_to_gcj02(lng, lat):
    return lng + 0.0002, lat + 0.0002


def gcj02_to_bd09(lng, lat):
    z = math.sqrt(lng * lng + lat * lat) + 0.00002 * math.sin(
        lat * math.pi * 3000.0 / 180.0
    )
    theta = math.atan2(lat, lng) + 0.000003 * math.cos(lng * math.pi * 3000.0 / 180.0)
    bd_lng = z * math.cos(theta) + 0.0065
    bd_lat = z * math.sin(theta) + 0.006
    return bd_lng, bd_lat
