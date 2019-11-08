import pymysql as sql
connect = sql.connect(host ="127.0.0.1",user = "root",password = "123456",database = "test",charset = "utf8")
cur = connect.cursor()
create_database = 'create database test1'
create_table = 'create table news2(title text,source text,time text,intraduce text,url text);'
filepath = 'E:\\百度新闻.csv' #文件路径
cur.execute( "load data infile 'E:\\new.csv'
into table baidu              
fields terminated by ',' 
optionally enclosed by '"' 
lines terminated by '\r\n' 
ignore 1 lines;")



a= ((1, '乔布斯', '18012345678', Decimal('0.00'), Decimal('0.00'), Decimal('0.00')), (2, '雷军', '13512345678', Decimal('8888.00'), Decimal('0.00'), Decimal('0.00')))
	
	