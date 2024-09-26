from sqlalchemy import create_engine, MetaData, Table, select
from sqlalchemy.orm import sessionmaker
import psycopg2
import json



# PostgreSQL 连接信息
pg_username = 'db_suriver_services'
pg_password = 'admin@123!'
pg_host = '192.168.1.224'
pg_db = 'ngh_test'



# 创建 PostgreSQL 连接
pg_engine = create_engine(
    f"postgresql+psycopg2://{pg_username}:{pg_password}@{pg_host}/{pg_db}")







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
