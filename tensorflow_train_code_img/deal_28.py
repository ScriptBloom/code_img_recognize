#!/usr/bin/python3.5  
# -*- coding: utf-8 -*-    

# 把图片批量装换为mnist所需的28*28像素
from PIL import Image
import os.path
import glob


def convertjpg(jpgfile,outdir,width=28,height=28):
    img=Image.open(jpgfile)
    try:
        new_img=img.resize((width,height),Image.BILINEAR)   
        new_img.save(os.path.join(outdir,os.path.basename(jpgfile)))
    except Exception as e:
        print(e)
        
for jpgfile in glob.glob("D:\\py\\code_img\\dealed_jpg\\*.png"):
    convertjpg(jpgfile,"D:\\py\\code_img\\28")