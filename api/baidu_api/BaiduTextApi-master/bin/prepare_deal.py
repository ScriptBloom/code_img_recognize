#!/usr/bin/python
#coding: utf-8

# 二值化、去噪、去除干扰线
import timeit,random,time,requests,os
from PIL import Image,ImageDraw
from PIL import  ImageEnhance 
from PIL import  ImageFilter 
# import pytesseract



Get_path = "D:\\py\\code_img\\code_jpg\\001.jpg"    #需要处理的验证码图片路径
Get_url = ""
Get_number = 10             #下载图片数量
Edit_path = 'D:\\py\\code_img\\gray_jpg\\1.jpg'       #灰度图目录
Edit_name = ''              #保存灰度图名称
Modif = 'D:\\py\\code_img\\dis_line\\1.png'          #去掉干扰线、预处理后验证码保存路径
ico = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

class IMG(object):

    def HandleVerify(self): 
        info_len = 0
        han_img_start = time.time()
        print('开始处理图片')
        threshold = 140
        table = [] 
        for i in range(256): 
            if i < threshold: 
                table.append(0) 
            else: 
                table.append(1) 


        print("正在处理验证码")
        ini_time = int(time.time())
        edit_img_name = random.randint(0,ini_time)  
        im = Image.open(Get_path)
        imgry = im.convert('L')
        out = imgry.point(table,'1') 
        Edit_name = Edit_path   
        out.save(Edit_name) 
        self.resize_img(Edit_name)
        han_img_end = time.time()
        print ("图片转换完成，耗时 %f m"%(han_img_end-han_img_start))



    def ModifyImg(self,img_name):

        img = Image.open(img_name)
        img = img.filter(ImageFilter.MedianFilter())
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(2)
        img = img.convert('1')

        width, height = img.size
        data = []
        for i in range(height):
            tmp=[]
            for j in range(width):
                if(img.getpixel((j,i)) == 255 ):
                    tmp.append(1)
                else:
                    tmp.append(0)
            data.append(tmp)
              
        img2 = Image.new("P",img.size, 255)
        for y in range(height):
            for a in range(len(data[y])):
                
                o = y+1
                t = y+2
                #s = y+3
                z = a+1
                x = a+2
                try:
                    if data[o][a] == 0 and data[t][a] == 0 and data[y][z] == 0  and data[y][x] == 0:#and data[s][a] == 0 
                        img2.putpixel((a,y),1)
                        img2.save(Modif)
                        
                        
                except:
                    pass
        img2_path = Modif

        image = Image.open(img2_path)  
        image = image.convert("L")  
        self.clearNoise(image,53,4,8)  
        image.save(img2_path)  
        # image.show()
   
    def resize_img(self,img_path):
        img= Image.open(img_path)
        width,height = img.size
        new_width = 280
        new_height = int(height * new_width / width)
        out = img.resize((new_width,new_height),Image.ANTIALIAS)
        # ext = os.path.splitext(img_path)[1]
        out.save(img_path,quality=95)    
        self.ModifyImg(img_path)


    def getPixel(self,image,x,y,G,N):  
        L = image.getpixel((x,y))  
        if L > G:  
            L = True  
        else:  
            L = False  
      
        nearDots = 0  
        if L == (image.getpixel((x - 1,y - 1)) > G):  
            nearDots += 1  
        if L == (image.getpixel((x - 1,y)) > G):  
            nearDots += 1  
        if L == (image.getpixel((x - 1,y + 1)) > G):  
            nearDots += 1  
        if L == (image.getpixel((x,y - 1)) > G):  
            nearDots += 1  
        if L == (image.getpixel((x,y + 1)) > G):  
            nearDots += 1  
        if L == (image.getpixel((x + 1,y - 1)) > G):  
            nearDots += 1  
        if L == (image.getpixel((x + 1,y)) > G):  
            nearDots += 1  
        if L == (image.getpixel((x + 1,y + 1)) > G):  
            nearDots += 1  
      
        if nearDots < N:  
            return image.getpixel((x,y-1))  
        else:  
            return None  

    def clearNoise(self,image,G,N,Z):  
        draw = ImageDraw.Draw(image)  
      
        for i in range(0,Z):  
            for x in range(1,image.size[0] - 1):  
                for y in range(1,image.size[1] - 1):  
                    color = self.getPixel(image,x,y,G,N)  
                    if color != None:  
                        draw.point((x,y),color)         


if __name__ == '__main__':
    Img = IMG()
    Img.HandleVerify()


def deal_code_img():
    Img = IMG()
    Img.HandleVerify()
