h,m=eval(input())
BMI=m/h*h
if BMI>32:
	print("严重肥胖")
elif 32>BMI>28:
	print("肥胖")
elif 28>BMI>25:
	print("过重")
elif 25>BMI>18.5:
	print("正常")
else:
	print("过轻")
	