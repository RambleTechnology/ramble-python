import os
import pandas as pd

def get_image_filenames_from_folder(folder_path):
    """获取指定文件夹中所有图片的文件名"""
    image_files = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):  # 支持常见图片格式
            image_files.append(filename)
    return image_files

def write_images_to_excel(img_folder_path, excel_filename):
    """遍历 img 文件夹，获取所有子文件夹中的图片名字并写入 Excel"""
    # 创建一个空的 DataFrame
    data = []

    # 遍历 img 文件夹中的所有子文件夹
    for subfolder in os.listdir(img_folder_path):
        subfolder_path = os.path.join(img_folder_path, subfolder)
        if os.path.isdir(subfolder_path):  # 确保是文件夹
            image_files = get_image_filenames_from_folder(subfolder_path)
            # 在每一行的第一个位置加入文件夹名字，然后跟上图片文件名
            data.append([subfolder] + image_files)

    # 将数据写入 Excel，设置 index=False 以防止将行索引写入 Excel 文件
    df = pd.DataFrame(data)

    # 将数据写入 Excel，不写入列名和索引
    df.to_excel(excel_filename, index=False, header=False)

    print(f"图片名字已写入 {excel_filename}")

# 调用函数，指定图片文件夹路径和目标 Excel 文件名
img_folder_path = 'img'  # 假设你的图片文件夹在当前目录下
excel_filename = 'image_filenames_with_folders.xlsx'

write_images_to_excel(img_folder_path, excel_filename)
