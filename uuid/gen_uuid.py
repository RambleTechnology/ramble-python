import uuid
import pandas as pd

# 生成8000个不包含横杠的UUID
uuids = [str(uuid.uuid4()).replace('-', '') for _ in range(9000)]

# 将UUID列表转换为DataFrame
df = pd.DataFrame(uuids, columns=['UUID'])

# 将DataFrame写入Excel文件
excel_file_path = 'uuids_no_hyphens.xlsx'
df.to_excel(excel_file_path, index=False)

print(f"8000个不包含横杠的UUID已写入Excel文件: {excel_file_path}")