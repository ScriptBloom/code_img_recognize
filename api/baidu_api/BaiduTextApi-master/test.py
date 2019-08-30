#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bin.AccessToken import AccessToken  # 测试获取AccessToken
from bin.WebImage import WebImage  # 网络图片文字识别
from bin.HandwRiTing import HandwRiTing  # 手写文字识别
from bin.Numbers import Numbers  # 数字识别
import json
import sys
sys.path.append('/media/dzou/Windows/py/scrapy_code/api')
from save_img import save_img

def handwriting(img):
    # 测试手写文字识别
    testHandTing = HandwRiTing(img)
    s = testHandTing.postHandwRiTing()
    print('手写文字识别: ', s)
    s1 = json.loads(s)
    p = s1["words_result"][0]
    print(p["words"])
    return p["words"]

def number(img):
    # 数字识别
    testNumbers = Numbers(img)
    n = testNumbers.postNumbers()
    print('数字识别：', n)
    n1 = json.loads(n)
    o = n1["words_result"][0]
    print(o['words'])
    return o["words"]

def onLineImage():
    # 网络图片文字识别
    testWebImage = WebImage()
    m = testWebImage.postWebImage()
    print('网络图片文字识别: ', m)
    m1 = json.loads(m)
    i = m1["words_result"][0]
    print(i['words'])
    return i["words"]

if __name__ == '__main__':
    # image = '025.jpg'  # 普通图片
    # NUMBERS = '027.jpg'  # 数字
    # im = '028.jpg'  # 数字


    # 路径在config中配置 这里这是文件名
    img = '1.png'

    # 测试获取AccessToken
    testAccessToken = AccessToken()
    # print('Access_token:', testAccessToken.getToken())

    # 该方法是调用 selenium 自动化截图保存验证码 不需要可注释
    # save_img()

    # print(onLineImage())
    print(number(img))
    print(handwriting(img))

    



    
