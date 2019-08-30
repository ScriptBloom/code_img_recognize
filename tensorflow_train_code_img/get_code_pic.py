#!/usr/bin/python3.5  
# -*- coding: utf-8 -*- 

# 获取训练样本

import random
from urllib.request import urlretrieve
import os
import time
#下载300张验证码图片
url = 'http://gk.vecc.org.cn/kaptcha/kaptcha.jpg'
path = '/home/dzou/Documents/code_jpg/' #将下载的图片保存到当前目录下的origin_imgs文件夹中
m = 1697
for i in range(1531878604000,1531878606000):
    urlretrieve(url, path + str(m) + '.jpg')
    print('成功下载 {} 张图片'.format(str(m)))
    m = m+1
    if (m%50 == 0):
        time.sleep(0.5)