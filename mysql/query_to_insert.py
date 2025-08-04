import pymysql
from pymysql.cursors import DictCursor
from datetime import datetime


def get_table_name_from_sql(sql):
    """从SQL语句中提取表名"""
    # 简单处理，适用于基本的SELECT语句
    sql_lower = sql.lower()
    if "from" in sql_lower:
        parts = sql_lower.split("from")[1].strip()
        # 去除可能的WHERE子句
        if "where" in parts:
            parts = parts.split("where")[0].strip()
        # 去除可能的反引号
        return parts.replace("`", "").split()[0]
    return "unknown_table"


def query_to_insert(host, port, user, password, database, query_sql):
    """执行查询并将结果转换为INSERT语句"""
    connection = None
    try:
        # 连接数据库
        connection = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            charset="utf8mb4",
            cursorclass=DictCursor,
        )

        with connection.cursor() as cursor:
            # 执行查询
            cursor.execute(query_sql)
            # 获取查询结果
            results = cursor.fetchall()

            if not results:
                print("查询结果为空")
                return []

            # 获取表名和列名
            table_name = get_table_name_from_sql(query_sql)
            columns = results[0].keys()

            # 生成INSERT语句
            insert_statements = []
            columns_str = ", ".join([f"`{col}`" for col in columns])

            for row in results:
                values = []
                for col in columns:
                    value = row[col]
                    if value is None:
                        values.append("NULL")
                    elif isinstance(value, (int, float)):
                        values.append(str(value))
                    else:
                        # 处理字符串中的单引号
                        escaped_value = str(value).replace("'", "''")
                        values.append(f"'{escaped_value}'")

                values_str = ", ".join(values)
                insert_sql = (
                    f"INSERT INTO `{table_name}` ({columns_str}) VALUES ({values_str});"
                )
                insert_statements.append(insert_sql)

            return insert_statements

    except Exception as e:
        print(f"发生错误: {str(e)}")
        return []
    finally:
        if connection:
            connection.close()


if __name__ == "__main__":
    # 数据库连接信息
    db_config = {
        "host": "192.168.1.126",  # 数据库主机地址
        "port": 3306,  # 数据库端口
        "user": "root",  # 数据库用户名
        "password": "J48Y5zVo1rpo7o25",  # 数据库密码
        "database": "ngh-smart-bams",  # 数据库名
    }

    # 要执行的查询SQL
    # query_sql = """
    # SELECT `GROUP_ID`, `API_ID`, `API_NAME`, `IS_AUTH`, `DESCRIPTION`,
    #        `START_VERSION`, `END_VERSION`, `IS_USE`, `REVISION`,
    #        `CREATE_BY`, `CREATE_TIME`, `UPDATE_BY`, `UPDATE_TIME`
    # from op_api
    # where GROUP_ID = '341d0a9e55d65ea4621c004dfae5c588'
    # """

    query_sql = """
    SELECT `api_id`, `status_code`, `error_code`, `illustrate`, `create_by`, `create_time`, `update_by`, `update_time`, `del_flag`, `version`
    from op_api_error_code_setting
    where api_id in (SELECT `API_ID` from op_api where GROUP_ID = '341d0a9e55d65ea4621c004dfae5c588')
    ;
    """

    # 执行转换
    insert_statements = query_to_insert(**db_config, query_sql=query_sql)

    # 打印结果
    for stmt in insert_statements:
        print(stmt)

    # 可选：将结果保存到文件

    # 生成带时间戳的文件名
    if insert_statements:
        # 时间格式：年-月-日_时-分-秒
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        # 从SQL中提取表名用于文件名
        table_name = get_table_name_from_sql(query_sql)
        filename = f"insert_{table_name}_{timestamp}.sql"

        # 保存到文件
        with open(filename, "w", encoding="utf-8") as f:
            for stmt in insert_statements:
                f.write(stmt + "\n")
        print(f"\nINSERT语句已保存到文件: {filename}")
