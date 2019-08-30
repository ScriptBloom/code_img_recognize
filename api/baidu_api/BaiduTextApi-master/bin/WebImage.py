#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 网络图片文字识别
import os
import base64
import requests
from .config import LOCALHOST_PATH, URL_LIST_URL
from .AccessToken import AccessToken

ACCESS_TOKEN = AccessToken().getToken()['access_token']
WEB_IMAGE_URL = URL_LIST_URL['WEB_IMAGE'] + '?access_token={}'.format(ACCESS_TOKEN)


class WebImageSuper(object):
    pass


class WebImage(WebImageSuper):
    # 在这传入识别网络图片url
    def __init__(self, image=None,url='http://gk.vecc.org.cn/kaptcha/kaptcha.jpg', detect_direction=True, detect_language=True):
        self.HEADER = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        self.IMAGE_CONFIG = {
            'detect_direction': detect_direction,
            'detect_language': detect_language,
        }

        if image is None:
            if url is not None:
                self.IMAGE_CONFIG['url'] = url
        elif url is None:
            imagePath = os.path.exists(LOCALHOST_PATH['PATH'] + image)
            if imagePath == True:
                images = LOCALHOST_PATH['PATH'] + image
                with open(images, 'rb') as image1:
                    self.IMAGE_CONFIG['image'] = base64.b64encode(image1.read())
        elif url and image is not None:
            self.IMAGE_CONFIG['url'] = url

    def postWebImage(self):
        try:
            webImage = requests.post(url=WEB_IMAGE_URL, headers=self.HEADER, data=self.IMAGE_CONFIG)
        except AttributeError:
            return 'image和url参数任选其一！'
        return webImage.text
