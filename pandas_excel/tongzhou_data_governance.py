import time
import pandas as pd
from pandas import DataFrame


def data_governance():
    print("====================开始治理====================")
    file_path = r'./通州/通州区人民调解委员会_result.xlsx'
    df = pd.read_excel(file_path)

    new_row = []
    for row in df.itertuples():
        name = getattr(row, "名称", "")
        # 经度
        long = getattr(row, "经度_bd", "")
        # 纬度
        lat = getattr(row, "纬度_bd")
        # 标签地址
        lat = getattr(row, "地址")
        # 标签来源
        source = "手工整理"
        # 标签类型
        type = ""
        # 坐标系
        coor = "bd"

    data = {'name': ['zs', 'ls', 'ww'], 'age': [
        11, 12, 13], 'gender': ['man', 'man', 'woman']}
    data1={'A': 'new_row', 'B': 'row2', 'C': 'row3'}
    new_df = DataFrame
    new_df.insert(1, pd.Series({'A': 'new_row', 'B': 'row2', 'C': 'row3'}))
    new_df.to_excel('治理完的数据.xlsx')
    # new_df = DataFrame
    # new_df.columns = ["标签名称", "标签来源", "经度", "纬度",
    #                   "标签地址", "标签类型", "坐标系", "基本信息", "外来标签ID"]
    # t = time.time()
    # path = str(t)+"治理完的数据.xlsx"
    # excel_writer = pd.ExcelWriter('your_file.xlsx')
    # new_df.to_excel(excel_writer,"Sheet1")
    print("====================结束治理====================")


def create_excel():
    # df=pd.read_excel(r'./通州/template.xlsx')
    # df.insert(2, '标签名称',["dd"])
    df=DataFrame()
    df.columns=['col1']
    df.insert(0,"col1","value")
    df.to_excel('result.xlsx')

if __name__ == "__main__":
    # data_governance()
    create_excel()
