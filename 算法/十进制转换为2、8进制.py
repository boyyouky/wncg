def turn(x,n):
	list=[]
	while True:
		r=x%n
		list.append(str(r))
		x=(x-r)//n
		if x<n:
			list.append(str(x))
			break
	list.reverse() ##反向排序list
	
	s="".join(list)##把list中元素拼起来
	print(eval(s))##把字符去''输出