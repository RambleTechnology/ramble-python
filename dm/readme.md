## 将csv内容导入到dm

### 备份表

mkdir /home/dm_backup

cd  /home/dmdba/dmdbms/bin

./dexp USERID=SYSDBA/xxx@localhost:5236 DIRECTORY=/home/dm_backup FILE=camera_backup260514.dmp  TABLES=xxx.xxx


### 恢复表

如果表已存在，先删除再导入（注意数据丢失风险！）
./dimp USERID=SYSDBA/xxx@localhost:5236 DIRECTORY=/home/dm_backup FILE=camera_backup260514.dmp TABLES=xxx.xxx TABLE_EXISTS_ACTION=REPLACE

### 服务器安装dmPython依赖

DM安装程序已经包含了dmPython依赖，我们只需要安装一下就可以

添加环境变量

```
1. 编辑配置文件
vi ~/.bashrc

2. 在文件末尾添加这两行
export DM_HOME=/home/dmdba/dmdbms
export LD_LIBRARY_PATH=$DM_HOME/bin:$LD_LIBRARY_PATH

3. 保存后，使配置立即生效
source ~/.bashrc
```

执行安装

```
cd /home/dmdba/dmdbms/drivers/python/dmPython

python3.7 setup.py install
```

检查 dmPython 安装是否成功

```
python3.7 -c "import dmPython" 2>/dev/null && echo "✓ dmPython 已安装" || echo "✗ dmPython 未安装"
```

### 执行py脚本治理数据

将py脚本和csv传到服务器下

```

mkdir /home/csv_to_dm

python3.7 .\csv_to_dm_transfer_coord.py .\t_video.csv  
```


### 验证

```
cd  /home/dmdba/dmdbms/bin

./disql  SYSDBA/xxx

SELECT * from "xxx"."xxx" order by id desc LIMIT 100 ;


```
有新数据，说明导入成功



