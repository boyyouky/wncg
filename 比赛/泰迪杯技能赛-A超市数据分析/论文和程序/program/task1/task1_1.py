import pandas as pd
data = pd.read_csv(r"C:\Users\顾伟强\AppData\Local\Temp\HZ$D.022.4649\HZ$D.022.4650\附件.csv",encoding='gb2312')
df = pd.DataFrame(data)
df.isnull().any()
nan_lines = data.isnull().any(1)
data[nan_lines]
df.dropna(axis = 0)
df[(df['销售数量'] >= -0.1) & (df['销售数量']<=0.1)]
count_1 = df.loc[df["销售数量"]>0.1]
count_2 = df.loc[df["销售数量"]<-0.1]
data_new = pd.concat([count_1,count_2])
data_new.to_csv("task1_1.csv",encoding="gb2312")