#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import logging
from retrying import retry


URL = 'http://gk.vecc.org.cn/ergs/o3/open/protect';
SAVE_CODE_PATH = "/home/dzou/Documents/1.png"
chromedriver_path = "/home/dzou/Documents/chromedriver" #改成你的chromedriver的完整路径地址,版本和chrome浏览器一致


# #定义一个infos类
class infos:

    #对象初始化
    def __init__(self):
        # webdriver初始化
        logging.basicConfig(level=logging.INFO,#控制台打印的日志级别
                    filename='info.log',
                    filemode='a',##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    #a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    #日志格式
                    )
        self.url = URL
        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 1}) # 加载图片
        options.add_experimental_option('excludeSwitches', ['enable-automation']) # 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
        self.browser = webdriver.Chrome(executable_path=chromedriver_path, options=options)
        self.wait = WebDriverWait(self.browser, 100) #超时时长为100s


    def retry_if_result_none(result):
        print("retry_if_result_none")
        return result is None

    #获取验证码
    # 需要重试把下面一行取消注解
    # @retry(retry_on_result=retry_if_result_none)
    def save(self):

        # 打开网页
        self.browser.get(self.url)

        self.browser.implicitly_wait(30) #智能等待，直到网页加载完毕，最长等待时间为30s
        # 等待页面body加载完毕
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'body')))
        sleep(0.5)
        # 获取验证码元素进行截图
        # code = self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="kaptcha"]/img')))
        code = self.browser.find_element_by_xpath('//*[@id="kaptcha"]/img')
        code.screenshot(SAVE_CODE_PATH)


        #如果验证码输入错误或请求失败则重试，直到成功为止(成功标志：出现table栏显示查询信息)
        #不了解可以查询retry模块
        # check = self.browser.find_element_by_xpath('/html/body/div[2]/div[2]/table')
        # if(check!=None):
        #     return 1
        # sleep(1)
        # return None 

def save_img():
    a = infos()
    a.save()




