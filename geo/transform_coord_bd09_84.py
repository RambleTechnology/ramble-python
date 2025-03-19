import math

# BD-09 to GCJ-02
def bd09_to_gcj02(bd_lon, bd_lat):
    x = bd_lon - 0.0065
    y = bd_lat - 0.006
    z = math.sqrt(x * x + y * y) - 0.00002 * math.sin(y * math.pi)
    theta = math.atan2(y, x) - 0.000003 * math.cos(x * math.pi)
    gcj_lon = z * math.cos(theta)
    gcj_lat = z * math.sin(theta)
    return gcj_lon, gcj_lat

# GCJ-02 to WGS-84
def gcj02_to_wgs84(gcj_lon, gcj_lat):
    # Using a differential method
    def delta(lon, lat):
        a = 6378245.0  # WGS84 semi-major axis
        ee = 0.006693421622965943  # WGS84 eccentricity squared
        dlat = transform_lat(lon - 105.0, lat - 35.0)
        dlon = transform_lon(lon - 105.0, lat - 35.0)
        radlat = lat / 180.0 * math.pi
        magic = math.sin(radlat)
        magic = 1 - ee * magic * magic
        sqrtmagic = math.sqrt(magic)
        dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * math.pi)
        dlon = (dlon * 180.0) / (a / sqrtmagic * math.cos(radlat) * math.pi)
        return dlon, dlat

    def transform_lat(lon, lat):
        return 300.0 + lon * 2 + lat * 3 + lon * lat * 0.2 + lat * lat * 0.1 + lon * lon * 0.2

    def transform_lon(lon, lat):
        return 500.0 + lon * 2 + lat * 3 + lon * lat * 0.2 + lon * lon * 0.1 + lat * lat * 0.3
    
    if not out_of_china(gcj_lon, gcj_lat):
        dlon, dlat = delta(gcj_lon, gcj_lat)
        wgs_lon = gcj_lon - dlon
        wgs_lat = gcj_lat - dlat
        return wgs_lon, wgs_lat
    else:
        return gcj_lon, gcj_lat

# Check if the point is out of China
def out_of_china(lon, lat):
    if lon < 72.004 or lon > 137.8347:
        return True
    if lat < 0.8293 or lat > 55.8271:
        return True
    return False

# BD-09 to WGS-84
def bd09_to_wgs84(bd_lon, bd_lat):
    gcj_lon, gcj_lat = bd09_to_gcj02(bd_lon, bd_lat)
    wgs_lon, wgs_lat = gcj02_to_wgs84(gcj_lon, gcj_lat)
    return wgs_lon, wgs_lat

# Main function to demonstrate conversion
def main():
    # 示例输入：BD-09 坐标
    bd_lon = float("116.462454")
    bd_lat = float("39.91")

    # 调用函数转换为WGS-84
    wgs_lon, wgs_lat = bd09_to_wgs84(bd_lon, bd_lat)
    
    # 输出转换后的WGS-84坐标
    print(f"转换后的WGS-84坐标: 经度: {wgs_lon}, 纬度: {wgs_lat}")

# 程序入口
if __name__ == "__main__":
    main()
