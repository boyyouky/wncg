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
def day_to_week(day):
    week= int(day/7)
    if(day%7>0):
        week+=1
    return week

df = pd.read_csv(r"C:\Users\ASUS\Desktop\技能赛\附件.csv",encoding='gbk')
df = df.dropna()
df.sort_values(by=['销售日期'])
ifsale =[]
month =[]
money =[]
January =31
February = 28
March = 31
April =30
for i in range(len(df)):
    ifsale.append(str(df.iloc[i,16]))
    money.append(float(df.iloc[i,14]))
    month.append(int(df.iloc[i,7]))
week_money =[[0,0,0] for i in range(18)]
for i in range(18):
    week_money[i][0]=i+1
days =month
for i in range(len(days)):
    days[i] = month_to_day(days[i])
weeks = []
for i in range(len(days)):
    weeks.append(day_to_week(days[i]))

for i in range(len(weeks)):
    weekflag = weeks[i]-1
    if (weeks[i]== week_money[weekflag][0]):
        if (ifsale[i] == '是'):
            week_money[weekflag][1] += money[i] * 100
        elif (ifsale[i] == '否'):
            week_money[weekflag][2] += money[i] * 100
for i in range(len(week_money)):
    week_money[i][1] = float(week_money[i][1]/100)
    week_money[i][2] = float(week_money[i][2]/100)
arr = np.array(week_money)
df1 =pd.DataFrame(arr,columns=['周数','促销商品销售额','非促销商品销售额'])
df1.to_csv(r"C:\Users\ASUS\Desktop\技能赛\task2_3.csv",encoding='gbk')

