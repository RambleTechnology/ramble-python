import paramiko


def upload_file(local_path, remote_path, hostname, username, password):
    # 创建 SSH 客户端
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # 连接到远程服务器
        client.connect(hostname, username=username, password=password)

        # 使用 SFTP 协议创建一个传输通道
        with client.open_sftp() as sftp:
            # 上传本地文件到远程服务器
            sftp.put(local_path, remote_path)
            print(f"文件 {local_path} 已成功上传到 {remote_path}")
            print(f"==================   jar上传成功  ======================")

    except Exception as e:
        print(f"上传文件时发生错误: {e}")

    finally:
        # 关闭 SSH 连接
        client.close()


def start_service(hostname, username, password):
    client = paramiko.SSHClient()
    transport = paramiko.Transport((hostname))
    transport.connect(username=username, password=password)
    client._transport = transport
    # 执行命令
    command = " sh /opt/ngh-smart/public/server/ngh-smart-ar/start.sh "
    client.exec_command(command)

    print(f"================= 重启命令执行成功 ==================")

if __name__ == "__main__":
    # 本地文件路径
    local_file_path = "D:/Code/ngh-smart-ar/target/ngh-smart-ar-0.0.1.jar"

    # 远程服务器信息
    remote_server_hostname = "192.168.1.128"
    remote_server_username = "root"
    remote_server_password = "Ngh@123456#"

    # 远程文件路径
    remote_file_path = "/opt/ngh-smart/public/server/ngh-smart-ar/ngh-smart-ar-0.0.1.jar"

    # 调用函数进行文件上传
    upload_file(local_file_path, remote_file_path, remote_server_hostname,
            remote_server_username, remote_server_password)
    start_service(remote_server_hostname,
              remote_server_username, remote_server_password)