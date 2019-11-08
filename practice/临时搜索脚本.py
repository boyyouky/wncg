class MyDatabase():
	charset = "utf8"
	def __init__(host,user,password,database):
		self.host = host	
		self.user = user
		self.password = password
		self.database = database	
	def reset_charset(self,charset):
		charset =str(charset)
		
#有参数“XH（学号）、XY（学院）、ZYMC（专业名称）、DQSZJ（）、XZB（行政班）、YKKH（）、KCDM（课程代码）、KCMC（课程名称）、XF(学分）、ZSCJ（正式成绩）"
#支持功能：1.查询学号获取该学生所有信息 2.查询上面的参数，得到该参数有关的信息
		
	def search(self,arg,content):
		connect = connect pymysql.connect(host =host,user =user, password = password,database=database,charset=charset)
		cur = connect.cursor()
		arg =str(arg)
		content = str(content)
		cur.execute("select * from student where {} like '%{}%';".format(arg,content)
		data = cur.fetchall()
		cur.close()
		content.close()
		tex = ''''''
		for i in range(len(data)):
			row = ''.join(data[i])
			txt += row + '\n'
		return txt
		
		
		
		
		connect = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database,
                                  charset=self.charset)