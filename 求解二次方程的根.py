import math
def quadratic(a,b,c):
	if b*b-4*a*c<0:
		print("无解")
	elif b*b-4*a*c==0 :
		x1=x2=(-b+math.sqrt(b*b-4*a*c))/2*a
		print(x1)
	else:
		x1=(-b+math.sqrt(b*b-4*a*c))/2*a
		x2=(-b-math.sqrt(b*b-4*a*c))/2*a
		print(x1,x2)



