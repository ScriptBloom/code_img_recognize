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
# 用来发送邮件的邮箱，可以注册一个163邮箱
email_username = 'xxxxx'
email_password = 'xxxxx'
# 用来接收验证码邮件的邮箱，可以用你的谷歌gmail或者qq邮箱
target_email = 'xxxxxx'

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
    def getcode(self):

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
        sleep(0.5)
        #发送邮件，等待输入
        self.send_email()
        #查看邮箱输入验证码
        s = input("请输入你邮箱收到的验证码以继续进行爬虫：")
        # 把你输入的验证码输入到input元素中，
        # 业务逻辑可自行更改
        self.browser.find_element_by_xpath('//*[@id="qry-form"]/div/div[2]/div[2]/div/input').send_keys(s)
        #todo 后面的操作你自行定义，验证码已经输入完毕
        #------------比如-------------
        #------------搜索-------------
        #self.browser.find_element_by_xpath('//*[@id="qry-form"]/div/div[2]/div[4]/div/input').click()


        #如果验证码输入错误或请求失败则重试，直到成功为止(成功标志：出现table栏显示查询信息)
        #不了解可以查询retry模块
        # check = self.browser.find_element_by_xpath('/html/body/div[2]/div[2]/table')
        # if(check!=None):
        #     return 1
        # sleep(1)
        # return None 

    # 发送邮件
    def send_email(self):
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from email.mime.image import MIMEImage
        from email.header import Header
        from email.utils import parseaddr, formataddr
        from email import encoders
        from email.mime.base import MIMEBase

        def _format_addr(s):
            name, addr = parseaddr(s)
            return formataddr((Header(name, 'utf-8').encode(), addr))

        sender = email_username
        receiver = target_email
        subject = 'happy day'
        smtpserver = 'smtp.163.com'
        username = email_username
        password = email_password
        boby = """
            <h3>email image</h3>
            <p>
            <br><img src="cid:image1"></br> 
            </p>
            <p>
        """

        msgRoot = MIMEMultipart('related')
        msgRoot['Subject'] = Header(subject,'utf-8')
        msgRoot['From'] = _format_addr('Me <%s>' % sender)
        msgRoot['To'] = _format_addr('SE <%s>' % receiver)

        msgText = MIMEText(
            '''happy birthday'''+boby, 'html', 'utf-8')
        msgRoot.attach(msgText)
        # 添加图片，以html形式显示
        fp = open(SAVE_CODE_PATH, 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()

        msgImage.add_header('Content-ID', '<image1>')
        msgRoot.attach(msgImage)

        # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
        with open(SAVE_CODE_PATH, 'rb') as f:
            # 设置附件的MIME和文件名，这里是png类型:
            mime = MIMEBase('image', 'png', filename='1.png')
            # 加上必要的头信息:
            mime.add_header('Content-Disposition', 'attachment', filename='1.png')
            mime.add_header('Content-ID', '<0>')
            mime.add_header('X-Attachment-Id', '0')
            # 把附件的内容读进来:
            mime.set_payload(f.read())
            # 用Base64编码:
            encoders.encode_base64(mime)
            # 添加到MIMEMultipart:
            msgRoot.attach(mime)

        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msgRoot.as_string())
        smtp.quit()

if __name__ == "__main__":
    chromedriver_path = "/home/dzou/Documents/chromedriver" #改成你的chromedriver的完整路径地址,版本和chrome浏览器一致
    a = infos()
    a.getcode()




