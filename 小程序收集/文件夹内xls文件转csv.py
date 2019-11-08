import pandas as pd
import numpy as np
import os
filename = os.listdir(r"D:\wncgdata\xlsx")
filepath =[]
newfilepath = []

for i in range(len(filename)):
    path= r"D:\wncgdata\xlsx" + '\\'+filename[i]
    filepath.append(path)
for i in range(len(filepath)):
    df= pd.read_excel(filepath[i])
    newpath = r"D:\wncgdata\csv" +'\\' +filename[i]
    df.to_csv(newpath,header=0,index=False,encoding='utf-8-sig')
    print(filename[i]+'已经完成')
