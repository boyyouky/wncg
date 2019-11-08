#创建列车类
class CRH:
	starttime =0 
	endtime=0
#创建A车间类
class A:
	def __init__(self):    #定义车间的一些属性
		self.name = ' '
		self.state = 0
		self.maintenancetime =60
#创建B车间类
class B:
	def __init__(self):
			self.name =' '
			self.state = 0
			self.maintenancetime =120
#创建C车间类
class C:
	def __init__(self):
			self.name = ' '
			self.state = 0
			self.maintenancetime =90
CRHqueue =[] #创建列车等待队列
time = 0	#初始化时间序列
Aworkshop = Bworkshoop = Cworkshoop=[] #初始化车间状态队列

for i in range(48):   #创建48个列车实例
	locals()['CRH%d'%i] =CRH()
	CRHqueue.append(locals()['CRH%d'%i])

CRHqueue.reverse()	 #队列反置，使得第一辆车被队列弹出
for i in range(3):    #创建3个A车间实例
	locals()['A%d'%i] = A()
	locals()['A%d'%i].name = 'A%d'%i
for i in range(8):    #创建8个B车间实例
	locals()['B%d'%i] = B()
	locals()['B%d'%i].name = 'B%d'%i
for i in range(5):		#创建5个C车间实例
	locals()['C%d'%i] = C()
	locals()['C%d'%i].name = 'C%d'%i

CRHname = 0  	#列车名字序号
while True:
	if(len(Aworkshop))<3): #车间是否为空的判定
		Aworkshop.append(CRHqueue.pop())
		locals()['CRH%d'%CRHname].starttime+= time
		locals()['CRH%d'%CRHname].endtime+=locals()['CRH%d'%CRHname].starttime+60
		CRHname+=1
	time+=1
	index =[]
	for i in range(len(Aworkshop)):  #检验A车间内列车出车间条件
		if(Aworkshop[i].endtime == time):
			index.append(Aworkshop[i])
	for i in range(len(index)):
		Aworkshop.remove(index[i])   #移除A车间维修好的列车
			
	if(len(Aworkshop)==0 and len(CRHqueue)==0):  #A车间为空时结束循环
		break
	 
print('%d分钟后最后一辆列出开出A站'%CRH48.endtime)#打印最后一辆车出A车间时间