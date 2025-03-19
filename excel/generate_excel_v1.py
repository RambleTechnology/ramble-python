import pandas as pd
import uuid
from datetime import datetime


# 读取 data.xlsx 文件中的目标列数据
def read_address_names(data_file: str, column_name: str) -> list:
    """
    读取 data.xlsx 文件中的目标列数据，返回一个列表。
    """
    print(f"正在读取 {data_file} 文件中的 {column_name} 列...")
    data_df = pd.read_excel(data_file)

    if column_name not in data_df.columns:
        raise ValueError(f"{column_name} 列在 {data_file} 文件中不存在！")

    address_names = data_df[column_name].dropna().tolist()  # 去除空值
    print(f"成功读取到 {len(address_names)} 条地址数据。")
    return address_names


# 生成不带横杠的 UUID
def generate_address_codes(n: int) -> list:
    """
    生成 n 个不带横杠的 UUID 列表。
    """
    print(f"正在生成 {n} 个地址代码...")
    return [str(uuid.uuid4()).replace("-", "") for _ in range(n)]


# 从模板文件中获取列名
def get_template_columns(template_file: str) -> list:
    """
    读取模板文件并返回其列名列表。
    """
    print(f"正在读取模板文件 {template_file} 的列名...")
    template_df = pd.read_excel(template_file, nrows=0)  # 只读取列名
    columns = template_df.columns.tolist()
    print(f"模板文件的列名: {columns}")
    return columns


# 逐行填充模板文件
def fill_template_with_data(template_file: str, address_names: list) -> pd.DataFrame:
    """
    逐行读取模板文件并填充 id、address_code 和 address_name 列。
    返回填充后的 DataFrame。
    """
    print(f"正在读取模板文件 {template_file} 并填充数据...")

    # 获取模板的列名
    template_columns = get_template_columns(template_file)

    # 读取模板的空数据框（保持列名，但不读取行数据）
    template_df = pd.read_excel(template_file, usecols=template_columns)

    # 检查地址数据是否足够
    if len(address_names) == 0:
        raise ValueError("address_names 数据为空！")

    # 生成 id 和 address_code 并填充数据
    start_id = 600000
    filled_rows = []
    for i in range(len(address_names)):
        uid = generate_address_codes(1)[0]
        new_row = {
            "id": start_id + i,
            "address_library_code": "POI_OTHER",
            "address_code": uid,
            "address_name": address_names[i],
            "origin_address": address_names[i],
            "origin_address_code": uid,
            "concrete_address": address_names[i],
            "recognition_rate": 0,
            "govern_status": 0,
            "operator": "admin",
            "address_template": "village_building_campus_park",
            "isvalid": 1,
            "create_time": get_current_time(),
            "update_time": get_current_time(),
            "dict_update_time": get_current_time(),
        }

        # 填充剩余的列，假设这些列需要填充空值（可以根据实际需求修改）
        for column in template_columns:
            if column not in new_row:
                new_row[column] = None  # 填充空值，如果列不在新生成的行中

        filled_rows.append(new_row)

    # 创建填充后的 DataFrame
    filled_template_df = pd.DataFrame(filled_rows, columns=template_columns)

    print(f"成功填充 {len(filled_template_df)} 行数据。")
    return filled_template_df


# 保存处理后的数据到新的 Excel 文件
def save_to_excel(df: pd.DataFrame, output_file: str) -> None:
    """
    将 DataFrame 保存为 Excel 文件。
    """
    df.to_excel(output_file, index=False)
    print(f"数据处理完成，已保存到 {output_file}")


# 定义一个函数，获取当前时间并格式化 2024/11/13  10:00:00
def get_current_time():
    # 获取当前时间
    current_time = datetime.now()

    # 格式化当前时间为指定格式
    formatted_time = current_time.strftime("%Y/%m/%d %H:%M:%S")

    # 返回格式化后的时间字符串
    return formatted_time


# 主函数，协调各个步骤
def main():
    try:
        # 文件路径配置
        data_file = "data.xlsx"
        template_file = "template.xlsx"  # 此模板文件包含列名但没有数据
        output_file = "output.xlsx"  # 输出的填充后文件
        column_name = "target_need_deal"  # 目标列名

        # 步骤 1: 读取 address_names 数据
        address_names = read_address_names(data_file, column_name)

        # 步骤 2: 填充模板数据
        filled_template = fill_template_with_data(template_file, address_names)

        # 步骤 3: 保存处理后的文件
        save_to_excel(filled_template, output_file)

    except Exception as e:
        print(f"发生错误: {e}")


# 调用主函数
if __name__ == "__main__":
    main()
