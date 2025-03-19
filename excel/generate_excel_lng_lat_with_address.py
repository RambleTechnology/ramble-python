import pandas as pd
import requests
import time  # 导入 time 模块

# 定义接口地址
API_URL = "http://localhost:7084/baidu/84/"

# 定义函数来调用 API 获取经纬度
def get_coordinates(full_address):
    try:
        # 发送请求
        response = requests.get(f"{API_URL}{full_address}")
        print(f"Requesting {full_address}, Response status: {response.status_code}")  # Debugging
        if response.status_code == 200:
            data = response.json()
            print(f"Response JSON: {data}")  # Debugging to see the full response
            lng = data.get("lng")
            lat = data.get("lat")
            return lng, lat
        else:
            print(f"Error: Unable to fetch coordinates for {full_address}, Status Code: {response.status_code}")
            return None, None
    except Exception as e:
        print(f"Error occurred while fetching coordinates for {full_address}: {e}")
        return None, None

# 定义函数来处理数据并更新经纬度
def update_coordinates_in_excel(input_file, output_file):
    # 读取 Excel 文件
    df = pd.read_excel(input_file)

    # 创建 df 的副本
    df_copy = df.copy()

    # 检查数据
    print(f"Loaded data from {input_file}. First few rows:")
    print(df_copy.head())

    # 遍历 DataFrame 并更新经纬度
    for index, row in df_copy.iterrows():
        # 获取 full_address 和 longitude 列的数据
        full_address = row["full_address"]
        longitude = row["longitude"]

        # 如果 longitude 为空或为 0，则调用接口更新经纬度
        if pd.isna(longitude) or longitude == 0:
            print(f"Fetching coordinates for address: {full_address}")
            lng, lat = get_coordinates(full_address)

            if lng and lat:
                # 更新 longitude 和 latitude 列
                df_copy.at[index, "longitude"] = lng
                df_copy.at[index, "latitude"] = lat
                print(f"Updated coordinates: {lng}, {lat}")
            else:
                print(f"Failed to fetch coordinates for address: {full_address}")

            # 让线程休息 1 秒
            time.sleep(1)

    # 将修改后的副本 DataFrame 保存为新的 Excel 文件
    df_copy.to_excel(output_file, index=False)
    print(f"Updated Excel file has been saved as {output_file}")

# 主函数
def main():
    input_file = "fulladdress_region-lngAndlat.xlsx"  # 输入文件
    output_file = "updated_fulladdress_region-lngAndlat.xlsx"  # 输出文件
    update_coordinates_in_excel(input_file, output_file)

# 如果是直接运行该脚本，则调用 main 函数
if __name__ == "__main__":
    main()
