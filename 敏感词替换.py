
#敏感词汇库
a=['北京'，'程序员'，'公务员'，'领导'，'牛逼'，'你娘'，'你妈'，'love'，'sex']
words=input("please enter words:")
for x in a:
	
	words=words.replace(x,'**')
print(words)