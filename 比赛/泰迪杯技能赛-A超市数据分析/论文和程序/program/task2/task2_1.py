import pandas as pd
import numpy as np


def month_to_day(month):
    month = month - 20150000
    m = int(month / 100)
    if (m == 1):
        day = month % 100
    elif (m == 2):
        day = January + month % 100
    elif (m == 3):
        day = February + January + month % 100
    elif (m == 4):
        day = February + January + March + month % 100
    return day


def day_to_month(day):
    if (day >= 1 and day <= 30):
        month = 20150100 + day
    if (day >= 31 and day <= 59):
        month = 20150200 + day - January
    if (day >= 60 and day <= 89):
        month = 20150300 + day - January - February
    if (day >= 90 and day <= 120):
        month = 20150400 + day - January - February - March
    return month


df = pd.read_csv(r"C:\Users\ASUS\Desktop\技能赛\附件.csv",encoding='gbk')
df = df.dropna()
df.sort_values(by=['销售日期'])
name =[]
month =[]
money =[]
January =31
February = 28
March = 31
April =30
for i in range(len(df)):
    name.append(str(df.iloc[i,11]))
    money.append(float(df.iloc[i,14]))
    month.append(int(df.iloc[i,7]))
days_money =[[0,0,0] for i in range(120)]
for i in range(120):
    days_money[i][0]=i+1
days =month
for i in range(len(days)):
    days[i] = month_to_day(days[i])
print(name)
print(days)
print(money)


for i in range(len(name)):
    dayflag =days[i]-1
    if(days[i]==days_money[dayflag][0]):
        if(name[i] =='生鲜'):
            days_money[dayflag][1] += money[i]*100
        elif(name[i]=='一般商品'):
            days_money[dayflag][2] += money[i]*100
    dayflag =0
for i in range(len(days_money)):
    days_money[i][1] = float(days_money[i][1]/100)
    days_money[i][2] = float(days_money[i][2]/100)
arr = np.array(days_money)
df1 =pd.DataFrame(arr,columns=['天数','生鲜销售额','一般商品销售额'])
df1.to_csv(r"C:\Users\ASUS\Desktop\技能赛\task2_1.csv",encoding='gbk')


