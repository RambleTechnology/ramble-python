import socket

target = "47.111.139.33"
ports = [80, 443, 22, 21, 3389, 8080,8848,3306,6379]  # 常见端口示例

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port}: OPEN")
    s.close()