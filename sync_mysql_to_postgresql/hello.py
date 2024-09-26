from sqlalchemy import create_engine, MetaData, Table

# MySQL数据库连接信息
mysql_username = 'root'
mysql_password = 'J48Y5zVo1rpo7o25'
mysql_host = '192.168.1.115'
mysql_port = '3306'
mysql_db = 'ngh-smart-ar'

# PostgreSQL数据库连接信息
postgresql_username = 'vastbase'
postgresql_password = 'Admin@123'
postgresql_host = '192.168.1.224'
postgresql_port = '5432'
postgresql_db = 'ngh_test'

# 创建MySQL数据库连接引擎
mysql_engine = create_engine(f"mysql+pymysql://{mysql_username}:{mysql_password}@{mysql_host}:{mysql_port}/{mysql_db}")

# 创建PostgreSQL数据库连接引擎
postgresql_engine = create_engine(f"postgresql+psycopg2://{postgresql_username}:{postgresql_password}@{postgresql_host}:{postgresql_port}/{postgresql_db}")

# 从MySQL中读取表结构
metadata = MetaData()
mysql_table = Table('poi_info', metadata, autoload=True, autoload_with=mysql_engine)

# 将MySQL中的数据插入到PostgreSQL中
with postgresql_engine.connect() as conn:
    with conn.begin():
        # 复制数据
        conn.execute(f"INSERT INTO poi_info SELECT * FROM mysql.{mysql_table}")

print("数据同步完成！")