import test
import myaes
import pandas as pd
import numpy as np
import os

path = r"C:\Users\ASUS\Desktop\数据\new"
newpath = r"C:\Users\ASUS\Desktop\数据\test"
def get_filepath(path):
    filename = os.listdir(path)
    for i in range(len(os.listdir(path))):
        filename[i] = path + '\\' + filename[i]
    filepath = filename
    return filepath
def get_newfilepath(newpath, path):
    filename = os.listdir(path)
    for i in range(len(os.listdir(path))):
        filename[i] = newpath + '\\' + filename[i]
    newfilepath = filename
    return newfilepath

def decrypt_excel_encrypt_aes_csv(filepath,newfilepath):
	df = pd.read_excel(filepath)
	for i in range(0,len(df)):
		crypto = df.iloc[i,1]
		message =test.decrypt(crypto)
		df.iloc[i,1] = myaes.encrypt(message)
	df.to_csv(newfilepath[:-4]+'csv',index=0,header=None,encoding='utf-8-sig')

filepath = get_filepath(path)
newfilepath = get_newfilepath(newpath, path)

for i in range(len(filepath)):
    decrypt_excel_encrypt_aes_csv(filepath[i],newfilepath[i])
    print('完成文件:'+filepath[i])
