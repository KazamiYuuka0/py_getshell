from gmssl.sm4 import CryptSM4, SM4_ENCRYPT, SM4_DECRYPT
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
def SM4_decrypt(ciphertext,secret_key=secret_key,crypt_sm4=crypt_sm4):
    #解密
    crypt_sm4.set_key(secret_key, SM4_DECRYPT)
    decrypted_text = crypt_sm4.crypt_ecb(ciphertext)
    #decode
    #decrypted_text=decrypted_text.decode()
    #返回
    return decrypted_text
#######################################
def encrypt_file(path):
    file=open(path,'rb')
    data=file.read()
    file.close()
    data_enc=SM4_encrypt(data)
    file2=open('fileout_enc','wb')
    file2.write(data_enc)
    file2.close()
def decrypt_file(path):
    file=open(path,'rb')
    data=file.read()
    file.close()
    data_enc=SM4_decrypt(data)
    file2=open('fileout_dec','wb')
    file2.write(data_enc)
    file2.close()
#######################################
def encode_file(path):
    file=open(path,'rb')
    data=file.read()
    file.close()
    data_enc=data
    file2=open('fileout_enc','wb')
    file2.write(data_enc)
    file2.close()
