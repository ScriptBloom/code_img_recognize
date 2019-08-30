#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## 手写文字识别
import os
import base64
import requests
from .AccessToken import AccessToken
from .config import LOCALHOST_PATH, URL_LIST_URL

ACCESS_TOKEN = AccessToken().getToken()['access_token']

HANDW_RI_TING_URL = URL_LIST_URL['HANDWRITING'] + '?access_token={}'.format(ACCESS_TOKEN)


class HandwRiTingSuper(object):
    pass


class HandwRiTing(HandwRiTingSuper):
    def __init__(self, image=None, recognize_granularity='small', words_type=''):
        self.HEADER = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        self.IMAGE_CONFIG = {
            'recognize_granularity': recognize_granularity,
            'words_type': words_type
        }

        if image is not None:
            imagepath = os.path.exists(LOCALHOST_PATH['PATH'] + image)
            if imagepath == True:
                images = LOCALHOST_PATH['PATH'] + image
                with open(images, 'rb') as images:
                    self.IMAGE_CONFIG['image'] = base64.b64encode(images.read())

    def postHandwRiTing(self):
        if self.IMAGE_CONFIG.get('image', None) == None:
            return 'image参数不能为空！'
        handwriTing = requests.post(url=HANDW_RI_TING_URL, headers=self.HEADER, data=self.IMAGE_CONFIG)
        return handwriTing.text
