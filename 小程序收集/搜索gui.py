import sys
import re
import bs4
import urllib.request
from bs4 import BeautifulSoup
import urllib.parse
from PyQt5.QtWidgets import (QPushButton,QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout,QApplication)

class Example(QWidget):
    def __init__(self): # 初始化
        super().__init__()
        self.initUI()

    def introduction(self,citiao): # 詞條的百度百科簡介部分函數
        url = 'https://baike.baidu.com/item/'+urllib.parse.quote(citiao)
        # 讀取網頁
        html = urllib.request.urlopen(url)
        content = html.read().decode('utf-8')
        html.close()
        #網頁解析
        soup = BeautifulSoup(content, "lxml")
        text = soup.find('div', class_="lemma-summary").children #簡介部分
        intro_text=''
        #文本處理，主要利用正則表達式
        for x in text:
            word = re.sub(re.compile(r"<(.+?)>"),'',str(x))
            words = re.sub(re.compile(r"\[(.+?)\]"),'',word)
            intro_text += words

        return intro_text # 返回文本(str格式)

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