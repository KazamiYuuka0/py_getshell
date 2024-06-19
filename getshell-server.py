import socket

# 创建一个IPv4 TCP Socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定IP地址和端口
server_address = ('45.77.35.154', 6667)  # 使用本地地址localhost，端口12345
server_socket.bind(server_address)

# 开始监听连接
server_socket.listen(1)  # 参数是允许排队的连接数量

print(f"服务器正在监听 {server_address[0]}:{server_address[1]} ...")

while True:
    # 等待连接
    try:
        client_socket, client_address = server_socket.accept()
        print(f"收到来自 {client_address[0]}:{client_address[1]} 的连接")
        while True:
            client_socket.sendall(input("[server]").encode())
            data = client_socket.recv(4096).decode()
            print(data)
    except:
        continue
