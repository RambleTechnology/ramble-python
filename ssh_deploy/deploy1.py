import paramiko

# 设置SSH连接参数
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.1.128', username='root', password='Ngh@123456#')

# 设置源文件路径和目标路径
source_file = 'D:/Code/ngh-smart-bams/ngh-mcdp-bams/target/ngh-mcdp-bams-3.0.1.jar'
target_folder = '/opt/ngh-smart/public/server/ngh-smart-bams/ngh-mcdp-bams-3.0.1.jar'

# 使用SFTP传输文件
sftp = ssh.open_sftp()
sftp.put(source_file, target_folder)  
sftp.close()

# 关闭SSH连接
ssh.close()
