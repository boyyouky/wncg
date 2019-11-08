import os
import pandas as pd
import glob
csv_list = glob.glob(r"D:\wncgdata\csv\*.csv")
print(csv_list)
for i in csv_list:
	fr = open(i,'rb').read()
	with open(r"D:\wncgdata\csv\result.csv",'ab') as f:
		f.write(fr)
print('合并完成')