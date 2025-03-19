import pymysql

# 数据库连接配置
db_config = {
    'host': '192.168.1.92',         # 替换为你的数据库地址
    'user': 'root',         # 替换为你的数据库用户名
    'password': 'J48Y5zVo1rpo7o25', # 替换为你的数据库密码
    'database': 'cml'  # 替换为你的数据库名称
}

# 连接数据库
connection = pymysql.connect(**db_config)
cursor = connection.cursor()

try:
    # 查询 bams_dept 表中 dept_name 为 '万州区' 的数据
    cursor.execute("SELECT dept_name FROM bams_dept WHERE parent_logic_id = '0001'")
    dept_data = cursor.fetchall()

    # 如果查询到数据
    if dept_data:
        for dept in dept_data:
            dept_name = dept[0]  # 获取 dept_name
            
            # 根据 dept_name 查询 bams_region 表中的 region_id
            cursor.execute("SELECT region_id FROM bams_region WHERE region_name = %s", (dept_name,))
            region_data = cursor.fetchone()

            # 如果找到对应的 region_id
            if region_data:
                region_id = region_data[0]

                # 更新 bams_dept 表中的 region_id
                update_query = "UPDATE bams_dept SET region_id = %s WHERE dept_name = %s"
                cursor.execute(update_query, (region_id, dept_name))

                # 提交更新
                connection.commit()
                print(f"Updated region_id for dept_name: {dept_name} to {region_id}")
            else:
                print(f"No matching region found for dept_name: {dept_name}")
    else:
        print("No departments found with parent_logic_id = '0001'.")

except pymysql.MySQLError as e:
    print(f"Error occurred: {e}")
    connection.rollback()

finally:
    cursor.close()
    connection.close()
