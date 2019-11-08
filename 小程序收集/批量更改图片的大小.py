找出文件夹内尺寸大于iPhone X的图片
按比例进行缩放并创建新文件
输出修改的图片名称及总个数
from PIL import Image
import os
def change_size(path):
	w=2436
	d=1125
	for picname in os.listdir(path):
		picpath=path+'/'+picname
		img=Image.open(picpath)
		new_img=img.resize((800,600),Image.ANTIALIAS)
		newpath=path+'/finish_'+picname
	    new_img.save(newpath)
			
		
 

