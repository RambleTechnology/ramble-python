import pymysql
import pandas as pd


def connect_to_mysql(host, port, user, password, database):
    connection = pymysql.connect(
        host=host, port=port, user=user, password=password, database=database
    )
    return connection


def get_database_schema(connection):
    schema_info = {}
    with connection.cursor() as cursor:
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        for table in tables:
            table_name = table[0]
            cursor.execute(f"DESCRIBE {table_name}")
            columns = cursor.fetchall()
            schema_info[table_name] = columns
    return schema_info


def format_schema_info(schema_info):
    formatted_data = []
    for table_name, columns in schema_info.items():
        for column in columns:
            formatted_data.append(
                {
                    "Table Name": table_name,
                    "Column Name": column[0],
                    "Data Type": column[1],
                    "Nullable": column[2],
                    "Key": column[3],
                    "Default": column[4],
                    "Extra": column[5],
                }
            )
    return pd.DataFrame(formatted_data)


def export_to_excel(df, filename):
    df.to_excel(filename, index=False)


def main():
    host = "192.168.1.58"
    port = 3306
    user = "root"
    password = "J48Y5zVo1rpo7o25"
    database = "ngh-smart-ar"

    connection = connect_to_mysql(host, port, user, password, database)
    schema_info = get_database_schema(connection)
    df = format_schema_info(schema_info)
    export_to_excel(df, "database_schema.xlsx")
    print("Database schema exported successfully!")


if __name__ == "__main__":
    main()
