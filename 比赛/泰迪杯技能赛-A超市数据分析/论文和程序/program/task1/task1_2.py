import pandas as pd
import numpy as np
df = pd.read_csv(r"C:\Users\ASUS\Desktop\技能赛\附件.csv",encoding='gbk')
df = df.dropna()
name = []
money =[]
for i in range(len(df)):
    name.append(str(df.iloc[i,2]))
    money.append(float(df.iloc[i,14]))
arr = np.array(name)
arr = np.unique(arr)
total = [0 for i in range(len(arr))]
for i in range(len(arr)):
    for x in range(len(name)):
        if(name[x]==arr[i]):
           total[i]+=money[x]*100
for i in range(len(total)):
    total[i]=float(total[i]/100)
list1 =[]
list1.append(arr)
list1.append(total)
arr1 = np.array(list1)
df1 =pd.DataFrame(arr1,index=None,columns=None)
df1.to_csv(r"C:\Users\ASUS\Desktop\技能赛\task1_2.csv",encoding='gbk')