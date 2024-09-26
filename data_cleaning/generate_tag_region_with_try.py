from sqlalchemy import create_engine, text
import pandas as pd
import random
import time

# 创建数据库连接
engine = create_engine(
    "mysql://root:@192.168.1.82:9030/test", pool_size=100, max_overflow=200
)  # 例如：'postgresql://user:password@localhost:5432/mydatabase'

def fetch_page(page_number, page_size):
    # 计算偏移量
    offset = (page_number - 1) * page_size

    # 定义SQL查询语句
    sql_query = text(
        f"""
        SELECT auth_field_1, id
        FROM tag_copy2
        WHERE auth_field_1 NOT LIKE '001033001022___'
        LIMIT :page_size OFFSET :offset
        """
    )

    # 执行查询
    with engine.connect() as connection:
        result = connection.execute(
            sql_query, {"page_size": page_size, "offset": offset}
        )
        # 将结果加载到DataFrame中
        df = pd.DataFrame(result.fetchall(), columns=result.keys())

    return df

page_size = 800
target_region = [
    "001033001022002",
    "001033001022003",
    "001033001022004",
    "001033001022005",
    "001033001022101",
    "001033001022102",
    "001033001022109",
    "001033001022110",
    "001033001022112",
    "001033001022113",
    "001033001022201",
    "001033001022202",
    "001033001022204",
    "001033001022210",
]

while True:
    page_number = 1  # 从第一页开始
    try:
        while True:
            df = fetch_page(page_number, page_size)
            if df.empty:
                break  # 如果没有更多数据，则退出循环

            # 处理当前页的数据
            print(f"Processing page {page_number}")
            # 确保 'auth_field_1' 列的数据类型是字符串
            df["auth_field_1"] = df["auth_field_1"].astype(str)
            for index, row in df.iterrows():
                id = row["id"]
                region = '' + row["auth_field_1"]
                if region not in target_region:
                    new_region = random.choice(target_region)
                    # 更新 auth_field_1 字段的值
                    update_sql = (
                        f"UPDATE tag_copy2 SET auth_field_1 = '{new_region}' WHERE id = {id}"
                    )
                    with engine.connect() as connection:
                        connection.execute(text(update_sql))
                    print(f"id={id}, region={region}, new_region={new_region}")

            page_number += 1
            #time.sleep(0.2)  # 稍作休息

    except Exception as e:
        print(f"An error occurred: {e}")
        print("Waiting for 1 minute before retrying...")
        time.sleep(30)  # 等待 1 分钟后重新开始
