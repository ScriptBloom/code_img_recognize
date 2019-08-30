# -*- coding:utf-8 -*-
import sys
import os
#QQ超人打码支持类库
import ctypes
from os.path import join, dirname, abspath, exists
dll = ctypes.windll.LoadLibrary(join(dirname(__file__),'dc64.dll'))
dll.GetUserInfo.restype = ctypes.c_uint64
dll.RecYZM_A.restype = ctypes.c_uint64
dll.RecByte_A.restype = ctypes.c_uint64

class dcVerCode:
    #user QQ超人打码账号
    #pwd QQ超人打码密码
    #softId 软件ID 缺省为0,作者务必提交softId,已保证分成
    def __init__(self,user,pwd,softId="0"):
        self.user = user.encode(encoding="utf-8")
        self.pwd = pwd.encode(encoding="utf-8")
        self.softId = softId.encode(encoding="utf-8")

    #获取账号剩余点数
    #成功返回剩余点数
    #返回"-1"----网络错误
    #返回"-5"----账户密码错误

    def getUserInfo(self):
        p = dll.GetUserInfo(self.user,self.pwd)
        if p:
                return ctypes.string_at(p,-1).decode()
        return ''

    #解析返回结果,成功返回(验证码,验证码ID),失败返回错误信息
    #点数不足:Error:No Money!
    #账户密码错误:Error:No Reg!
    #上传失败，参数错误或者网络错误:Error:Put Fail!
    #识别超时:Error:TimeOut!
    #上传无效验证码:Error:empty picture!
    #账户或IP被冻结:Error:Account or Software Bind!
    #软件被冻结:Error:Software Frozen!
    def parseResult(self,result):
        list = result.split('|')
        if len(list)==3:
            return (list[0],list[2])
        return (result,'')

    #recByte 根据图片二进制数据识别验证码,返回验证码,验证码ID
    #buffer 图片二进制数据

    def recByte(self,buffer):
        p = dll.RecByte_A(buffer,len(buffer),self.user,self.pwd,self.softId)
        if p:
            str = ctypes.string_at(p,-1).decode()
            return self.parseResult(str)
        return ''

    #recYZM 根据验证码路径识别,返回验证码,验证码ID
    #path 图片路径
    def recYZM(self,path):
        p = dll.RecYZM_A(path.encode(encoding="utf-8"),self.user,self.pwd,self.softId)
        if p:
            str = ctypes.string_at(p,-1).decode()
            return self.parseResult(str)
        return ''

    #reportErr 提交识别错误验证码
    #imageId 验证码ID
    def reportErr(self,imageId):
        dll.ReportError(self.user,imageId)
        
if __name__ == '__main__':
    client = dcVerCode("#","#","#"); #超人打码帐号,超人打码密码,软件ID
    path = "E:\\Code\\Python\\captcha\\captchaImg\\"
    counter = 1
    prefix = ".jpg"
    

    #查询帐号余额
    print ('帐号余额:' + client.getUserInfo())
    for i in range(743,991):
        yzm,imageId = client.recYZM("captchaImg\\"+str(i)+".jpg")
        if os.path.exists(path+yzm+prefix):
           os.remove(path+yzm+prefix)
        else:
            os.rename(os.path.join(path,str(i)+prefix),os.path.join(path,yzm+prefix))
            print(str(i)+":"+yzm)
        
    #client.reportErr(imageId.encode(encoding="utf-8")) #只有在验证码识别错误时才运行这个方法,恶意提交将会受到惩罚