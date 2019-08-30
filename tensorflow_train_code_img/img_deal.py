#!/usr/bin/python3.5  
# -*- coding: utf-8 -*- 

# 切割图片为6张数字图片

from PIL import Image
import os
import time

path = 'D:\\py\\code_img'
origin_path = path + "\\no_disLine\\"
new_path = path + '\\dealed_jpg\\'   #用来存放处理好的图片

#从100张图片中提取出字符样本
for image in os.listdir(origin_path)[:2000]: 
    im = Image.open(origin_path+image)    
    width, height = im.size
    cut = [44,76,107,141,174,207,237]
    count = [0,1,2,3,4,5]
    for i in count:
        img = im.crop((cut[i],0,cut[i+1],70))
        # img.show()
        img.save(new_path + str(i)+'-'+ image.replace('png','png'))  
    print('成功处理图片{}'.format(image))    


    