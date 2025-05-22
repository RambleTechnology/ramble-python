import os
from ftplib import FTP

# FTP 连接信息
ftp_host = "47.122.123.149"
ftp_port = 21
ftp_user = "cmll"
ftp_pass = "123456"

# 本地 images 文件夹路径（Windows路径）
local_directory = r"C:\Users\cml\Pictures"  # 使用原始字符串避免路径转义问题

# 连接到 FTP 服务器
ftp = FTP()
ftp.connect(ftp_host, ftp_port)
ftp.login(ftp_user, ftp_pass)

# 切换到服务器上的目标文件夹，如果没有文件夹可以创建它
# ftp.cwd('path_on_ftp')  # 如果需要切换到特定的文件夹

def upload_files(local_dir, remote_dir):
    """递归上传文件夹中的文件"""
    # 如果目标目录不存在，创建该目录
    try:
        ftp.cwd(remote_dir)  # 切换到目标目录
    except Exception:
        ftp.mkd(remote_dir)  # 创建目录
        ftp.cwd(remote_dir)  # 进入目录

    # 遍历目录中的所有内容
    for item in os.listdir(local_dir):
        local_path = os.path.join(local_dir, item)
        
        if os.path.isdir(local_path):  # 如果是文件夹，递归调用
            upload_files(local_path, item)
        elif os.path.isfile(local_path):  # 如果是文件，上传文件
            with open(local_path, "rb") as file:
                # 使用 FTP 上传文件
                ftp.storbinary(f"STOR {item}", file)

# 调用函数上传本地的 pictures 文件夹到 FTP
upload_files(local_directory, "Pictures")  # 假设要上传到 FTP 上的 "Pictures" 目录

# 关闭 FTP 连接
ftp.quit()

print("文件上传完成")
