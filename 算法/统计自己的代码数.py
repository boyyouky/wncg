import os
import string  
def count(path):
	total=0
	countblank=0
	countpound=0
	for file in os.listdir(path):
		filepath=path + file
		myfile=open(filepath)
		for li in myfile.readlines(): 
			total=total+1
			if not li.split(): 
				countBlank=countblank+1
			if li.startswith('#'):             
				countPound=countpound+1
	print("空行:%d" % countblank)
	print("注释行:%d" % countpound)
    print("总行数:%d" % total)
			

