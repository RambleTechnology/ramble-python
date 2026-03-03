from openpyxl import Workbook
import random
import string

# ===== 基本配置 =====
ROW_COUNT = 300_000      # 行数，约 80~95MB，可自行调大/调小
OUT_FILE = "导入性能测试数据2.xlsx"

# ===== Workbook（写入模式，省内存）=====
wb = Workbook(write_only=True)
ws = wb.create_sheet("资源数据")

# 表头（与模板一致）
ws.append([
    "资源名称", "资源地址", "经度", "纬度", "坐标系",
    "资源类型", "标签类型", "是否多层空间",
    "楼层", "基本信息", "外来标识"
])

# 浦东新区常见道路
ROADS = [
    "世纪大道", "张江高科路", "陆家嘴环路", "金科路",
    "浦东南路", "杨高南路", "龙阳路", "芳甸路"
]

def gen_cml_id():
    return "cml" + "".join(
        random.choices(string.ascii_lowercase + string.digits, k=12)
    )

# ===== 生成数据 =====
for i in range(ROW_COUNT):
    ws.append([
        f"浦东资源{i}",
        f"上海市浦东新区{random.choice(ROADS)}{random.randint(1, 9999)}号",
        round(random.uniform(121.3, 121.8), 6),  # 经度
        round(random.uniform(31.0, 31.4), 6),   # 纬度
        "bd",                                   # 坐标系
        "001901001001",                         # 资源类型（写死）
        "",
        "",
        "",
        "",
        gen_cml_id()                            # 外来标识
    ])

# ===== 保存 =====
wb.save(OUT_FILE)
