from sqlalchemy import create_engine, MetaData, Table, select
from sqlalchemy.orm import sessionmaker
import psycopg2
import json

# MySQL 连接信息
mysql_username = 'root'
mysql_password = 'J48Y5zVo1rpo7o25'
mysql_host = '192.168.1.115'
mysql_db = 'ngh-smart-ar'

# PostgreSQL 连接信息
pg_username = 'db_suriver_services'
pg_password = 'admin@123!'
pg_host = '192.168.1.224'
pg_db = 'ngh_test'

# 创建 MySQL 连接
mysql_engine = create_engine(
    f"mysql://{mysql_username}:{mysql_password}@{mysql_host}/{mysql_db}")

# 创建 PostgreSQL 连接
pg_engine = create_engine(
    f"postgresql+psycopg2://{pg_username}:{pg_password}@{pg_host}/{pg_db}")

# 创建MySQL元数据
mysql_meta = MetaData()
mysql_meta.reflect(bind=mysql_engine)

# 获取 MySQL 中的表
mysql_table = mysql_meta.tables['poi_info']




# 创建 PostgreSQL 元数据
# pg_meta = MetaData(bind=pg_engine)
# pg_meta = MetaData()
# pg_meta.bind = pg_engine
# pg_table=pg_meta.tables['poi_info']

# 创建 PostgreSQL 元数据
pg_meta = MetaData()

# 反射 PostgreSQL 数据库中的表结构
pg_meta.reflect(bind=pg_engine)

# 获取反射后的表对象
pg_tables = pg_meta.tables

# 打印反射后的表名
print(pg_tables.keys())

# 将 MySQL 表结构应用到 PostgreSQL 数据库
# mysql_table.create(bind=pg_engine, checkfirst=True)

# 创建Session
Session = sessionmaker(bind=mysql_engine)
session = Session()

# 从 MySQL 中查询数据
# mysql_data = session.execute(select([mysql_table])).fetchall()
mysql_data = session.execute(mysql_table.select().limit(10)).fetchall()


# 创建Session
Session_pg = sessionmaker(bind=pg_engine)
session_pg = Session_pg()

# 插入数据到 PostgreSQL
for row in mysql_data:
    session_pg.execute(pg_table.insert().values(row))

# 提交并关闭会话
session_pg.commit()
session_pg.close()
session.close()

print("Data synchronization complete!")
