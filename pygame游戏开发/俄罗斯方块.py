import sys
import pymysql as sql
from PyQt5.QtWidgets import (QPushButton,QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout,QApplication)

class Example(QWidget):
    def __init__(self): # 初始化
        super().__init__()
        self.initUI()

    def introduction(self, citiao):
        connect = sql.connect(host="127.0.0.1", user="root", password="123456", database="test", charset="utf8")
        cur = connect.cursor()
        citiao = str(citiao)
        cur.execute("select title,url from new3 where title like '%{}%';".format(citiao))
        data = cur.fetchall()
        cur.close()
        connect.close()
        txt = ''''''
        for i in range(len(data)):
            row = ''.join(data[i])
            txt += row + '\n'
        return txt

    def intro_final(self,citiao): # 異常处理函數
        try:
            return self.introduction(citiao)
        except AttributeError:
            return "请再输入详细点，亲~~"

    def initUI(self):
        #GUI布局及控件放置
        search_label = QLabel("请输入搜索词条：")
        search_item = QLineEdit()
        btn1 = QPushButton("开始搜索", self)
        btn2 = QPushButton("清空", self)
        search_result = QTextEdit()
        grid = QGridLayout()
        grid.setSpacing(5)
        grid.addWidget(search_label, 1, 0)
        grid.addWidget(search_item,2, 0)
        grid.addWidget(btn1, 3, 0)
        grid.addWidget(btn2, 3, 1)
        grid.addWidget(search_result, 4, 0, 5, 0)
        self.setLayout(grid)

        #爲兩個按鈕關聯處理函數，當按下“開始搜索”按鈕開始開搜並輸出，當按下“清空”清空內容
        def searching():
            search_result.setText(self.intro_final(search_item.text()))
        btn1.clicked.connect(searching)

        def clear():
            search_result.setText("")
            search_item.setText("")
        btn2.clicked.connect(clear)

        #設置窗口
        self.setGeometry(400, 150, 600, 500)
        self.setWindowTitle("搜索引擎GUI")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
