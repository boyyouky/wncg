import time
from selenium import webdriver
from lxml import etree
user='QQ号码'      
pw='QQ密码'
friend='朋友QQ'
driver=webdriver.Firefox()
driver.maximize_window()
driver.get("http://i.qq.com")
driver.switch_to.default_content()
driver.get("http://user.qzone.qq.com/" +friend+ "/311")
next_num=0
while True:
	for i in range(1,6):
		height=20000*i
		strWord = "window.scrollBy(0,"+str(height)+")"
		driver.execute_script(strWord)
		time.sleep(4)
	driver.switch_to.frame("app_canvas_frame")
	selector = etree.HTML(driver.page_source)
	divs = selector.xpath('//*[@id="msgList"]/div[3]')
	with open('qq_word.txt','a') as f:
		for div in divs:
			qq_name = div.xpath('./div[2]/a/text()')
			qq_content = div.xpath('./div[2]/pre/text()')
			qq_time = div.xpath('./div[4]/div[1]/span/a/text()')
			qq_name = qq_name[0] if len(qq_name)>0 else ''
			qq_content = qq_content[0] if len(qq_content)>0 else ''
			qq_time = qq_time[0] if len(qq_time)>0 else ''
			print(qq_name,qq_time,qq_content)
			f.write(qq_content+"\n")
	if driver.page_source.find('pager_next_' + str(next_num)) == -1:
		break
	driver.find_element_by_id('pager_next_' + str(next_num)).click()
	next_num += 1
	driver.switch_to.parent_frame()