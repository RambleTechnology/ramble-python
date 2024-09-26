from sqlalchemy import create_engine, text
import pandas as pd
import random
from concurrent.futures import ThreadPoolExecutor, as_completed

# 创建数据库连接
engine = create_engine(
    "mysql://root:@192.168.1.82:9030/test", pool_size=100, max_overflow=200
)


def fetch_page(page_number, page_size):
    offset = (page_number - 1) * page_size
    sql_query = text(
        f"""
        SELECT auth_field_1, id
        FROM tag_copy2
        WHERE auth_field_1 NOT LIKE '001033001022___'
        LIMIT :page_size OFFSET :offset
        """
    )
    with engine.connect() as connection:
        result = connection.execute(
            sql_query, {"page_size": page_size, "offset": offset}
        )
        df = pd.DataFrame(result.fetchall(), columns=result.keys())
    return df


def process_page(page_number, page_size, target_region):
    df = fetch_page(page_number, page_size)
    if df.empty:
        return

    df["auth_field_1"] = df["auth_field_1"].astype(str)
    for _, row in df.iterrows():
        id = row["id"]
        region = row["auth_field_1"]
        if region not in target_region:
            new_region = random.choice(target_region)
            update_sql = (
                f"UPDATE tag_copy2 SET auth_field_1 = '{new_region}' WHERE id = {id}"
            )
            with engine.connect() as connection:
                connection.execute(text(update_sql))
            print(f"Processed id={id}, region={region}, new_region={new_region}")


def main():
    page_size = 500
    max_pages = 5  # Number of pages to process
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

    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = [
            executor.submit(process_page, page_number, page_size, target_region)
            for page_number in range(1, max_pages + 1)
        ]
        for future in as_completed(futures):
            future.result()  # Optional: to catch any exceptions raised in the thread


if __name__ == "__main__":
    main()
