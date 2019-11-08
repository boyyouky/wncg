from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
data = pd.read_csv('task1_1.csv', encoding='gb2312')
data_2_2_1 = data.loc[data['销售月份'] == 201502]
data_2_2_1 = data_2_2_1.drop(['销售月份'],axis=1)
data_01 = data_2_2_1['销售金额'].groupby(data_2_2_1['大类名称'])
data_01 = data_01.sum()
sampler= np.random.permutation(14)
data_01 = data_01.take(sampler)
plt.figure(figsize=(10,10))
data_01.plot.pie(labeldistance = 1.05,startangle=225)
