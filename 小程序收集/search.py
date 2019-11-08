import pymysql as sql
class MyDatabase:
    charset = "utf-8"
    def __init__(self,host,user,password,database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database


    def search(citiao):
        connect = sql.connect(host=self.host, user=self.user, password=self.password, database=self.database, charset=charset)
        cur = connect.cursor()
        citiao = str(citiao)
        cur.execute("select title,url from baidu where title like '%{}%';".format(citiao))
        data = cur.fetchall()
        cur.close()
        connect.close()
        txt = ''''''
        for i in range(len(data)):
            row = ''.join(data[i])
            txt += row + '\n'
        return txt

d= MyDatabase("127.0.0.1","root","123456","test")


