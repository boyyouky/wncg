import pymysql as sql
connect = sql.connect(host ="127.0.0.1",user = "root",password = "123456",database = "test",charset = "utf8")
cur = connect.cursor()
print('请输入关键词：')
keyword = str(input())
cur.execute("select title,url from baidu where title like '%{}%';".format(keyword))
data = cur.fetchall()
cur.close()
connect.close()
for i in range(len(data)):
    print(data[i])