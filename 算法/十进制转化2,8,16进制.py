def turn2(x,y):
	list1=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
	list2=[]
	while True :
		if x<y :
			list2.append(list1[x])
			break
		r=x%y
		list2.append(list1[r])
		x=(x-r)//y
	list2.reverse() 
    print(list2)