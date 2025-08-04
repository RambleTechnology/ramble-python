# mysql 相关脚本和功能集合

## query_to_insert.py

将查询结果转换为insert语句，需要提供查询的sql语句，明确定义需要查询的列，转换后的insert语句会打印到控制台，同时保存到文件中，文件命名规则：insert_表名_时间戳.sql