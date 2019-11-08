import pandas as pd
import numpy as np
df = pd.read_csv(r"C:\Users\ASUS\Desktop\技能赛\附件.csv",encoding='gbk')
df = df.dropna()
df=df.sort_values(by=['顾客编号'])
customers =[]
for i in range(len(df)):
    message = []
    message.append(int(df.iloc[i,0]))
    message.append(int(df.iloc[i,7]))
    message.append(int(df.iloc[i,8]))
    message.append(float(df.iloc[i,14]))
    customers.append(message)
customers_number = customers[i][0]
month_number = 4
customer =[[] for n in range(customers_number)]
for i in range(customers_number):
    for x in range(len(customers)):
        if(customers[x][0]==i):
            customer[i].append(customers[x])
customer_month =[[0 for i in range(9)] for i in range(customers_number)]
for n in range(customers_number):
    for i in range(len(customer[n])):
        if (customer[n][i][2] == 201501):
            customer_month[n][1] += 1
            customer_month[n][2] += customer[n][i][3]*100
        elif (customer[n][i][2] == 201502):
            customer_month[n][3] += 1
            customer_month[n][4] += customer[n][i][3]*100
        elif (customer[n][i][2] == 201503):
            customer_month[n][5] += 1
            customer_month[n][6] += customer[n][i][3]*100
        elif (customer[n][i][2] == 201504):
            customer_month[n][7] += 1
            customer_month[n][8] += customer[n][i][3]*100
for i in range(len(customer_month)):
    customer_month[i][2] =float(customer_month[i][2]/100)
    customer_month[i][4] = float(customer_month[i][4] / 100)
    customer_month[i][6] = float(customer_month[i][6] / 100)
    customer_month[i][8] = float(customer_month[i][8] / 100)
arr = np.array(customer_month)
df_arr = pd.DataFrame(arr,columns=['顾客编号','一月消费天数','一月消费额','二月消费天数','二月消费额','三月消费天数','三月消费额','四月消费天数','四月消费额'])
df_arr.to_csv(r"C:\Users\ASUS\Desktop\技能赛\task1_5.csv",encoding='gbk')







