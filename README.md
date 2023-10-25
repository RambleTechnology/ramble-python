# ramble-python
漫步python。收集一些工作中编写的python脚本；作为学习python过程中实践代码的存储仓库。



# pandas_excel

此文件夹存放使用 pandas 工具包操作excel相关案例

## 读取excel

~~~python

def read():
    file_path = r'./python_pandas_excel.xlsx'
    df = pd.read_excel(file_path, sheet_name="Sheet1")
    print(df)
    print("----------")
    print(df.head())
    print("----------")
    print(df.columns)
    print("----------")
    print(df.index)
    print("----------")
    print(df["name"])
    print("----------")
    print(df.describe())

~~~

## 写excel


~~~python

def write():
    data = {'name': ['zs', 'ls', 'ww'], 'age': [
        11, 12, 13], 'gender': ['man', 'man', 'woman']}
    df = DataFrame(data)
    df.to_excel('pandas_write_excel.xlsx')

~~~


## 新增列

~~~python


def edit():
    file_path = r'./TagBaseInfo信息整理.xlsx'
    df = pd.read_excel(file_path)
    name_column = df['水源名称']
    # print("水源名称列的值为：")
    print(*name_column, sep=",")

    # 遍历方式一，按行遍历，带索引
    # for r in df.iterrows():
    #   print(r)

    # 遍历方式二，一行为一个元组
    # 新列的值放到一个列表中
    new_column_value = []
    for row in df.itertuples():
        # print(row)
        name = getattr(row, "水源名称", "")
        station = getattr(row, "消防站简称", "")
        link = getattr(row, "联系方式", "")
        new_value = "水源名称:"+name+",消防站简称:"+station+",联系方式:"+str(link)
        new_column_value.append(new_value)
    # print(new_column_value)

    old_columns = df.columns.tolist()
    old_columns.append("新增一列的名称")
    new_columns = old_columns
    df.reindex(columns=new_columns)
    df["新增一列的名称"] = new_column_value
    df.to_excel("用已有列计算得到新的列.xlsx")

~~~