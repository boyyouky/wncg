import os
import json
import xlwt
filepath='文件路径'
os.chdir(filepath)
with open('city.txt') as f:
	content=f.read()
	d=json.loads(content)
	file = xlwt.Workbook()
	table = file.add_sheet('test')
    for row, i in enumerate(list(d)):
        table.write(row, 0, i)
        table.write(row, 1, d[i])
    file.save('city.xls')
