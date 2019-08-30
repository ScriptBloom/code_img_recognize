#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

#
ACCESS_TOKEN = ''
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

### 在这配置你的百度API信息
### 注册后在 https://console.bce.baidu.com/ai 中获取
# ID,KEY的配置信息
INFO_CONFIG = {
    'ID': 'xxxxxxxx',
    'API_KEY': 'xxxxxxxx',
    'SECRET_KEY': 'xxxxxxxx'
}

# 本地路径配置
LOCALHOST_PATH = {
    'PATH': os.path.join(BASE_DIR, '/home/dzou/Documents/')
}

# URL配置
URL_LIST_URL = {
    # ACCESS_TOKEN_URL用于获取ACCESS_TOKEN, POST请求,
    #  grant_type必须参数,固定为client_credentials,client_id必须参数,应用的API Key,client_secre 必须参数,应用的Secret Key.
    'ACCESS_TOKEN_URL': 'https://aip.baidubce.com/oauth/2.0/token?' + 'grant_type=client_credentials&client_id={API_KEYS}&client_secret={SECRET_KEYS}&'.format(
        API_KEYS=INFO_CONFIG['API_KEY'], SECRET_KEYS=INFO_CONFIG['SECRET_KEY']),
    # 网络图片文字识别
    # URL参数：
    ## access_token	调用AccessToken模块获取
    # Headers参数
    ## 参数：Content-Type	，值：application/x-www-form-urlencoded
    # Body请求参数：
    ## 参数：image，	                    是否必选：和url二选一，	        类型：string，  	可选值范围：null	                                                            说明：图像数据，base64编码后进行urlencode，要求base64编码和urlencode后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式，当image字段存在时url字段失效
    ## 参数：url，	                    是否必选：和image二选一，	    类型：string，  	可选值范围：null	                                                            说明：图片完整URL，URL长度不超过1024字节，URL对应的图片base64编码后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式，当image字段存在时url字段失效，不支持https的图片链接
    ## 参数：detect_direction	，  是否必选：false，        类型：string，  可选值范围：[true、false]，                                       说明：是否检测图像朝向，默认不检测，即：false。朝向是指输入图像是正常方向、逆时针旋转90/180/270度。可选值包括: - true：检测朝向； - false：不检测朝向。
    ## 参数：detect_language，    是否可选：false，        类型：string，  可选值范围：[true、false]，                                       说明：是否检测语言，默认不检测。当前支持（中文、英语、日语、韩语）
    # ---------------------------------------------------------------------------------------
    # 返回说明
    ## 字段：direction，	                是否必选：否	    类型：int32，	            说明：图像方向，当detect_direction=true时存在。 - -1:未定义， - 0:正向， - 1: 逆时针90度， - 2:逆时针180度， - 3:逆时针270度
    ## 字段：log_id，	                    是否必选：是	    类型：uint64，	        说明：唯一的log id，用于问题定位
    ## 字段：words_result，	            是否必选：是	    类型：array()，	        说明：识别结果数组
    ## 字段：words_result_num，	        是否必选：是	    类型：uint32，	        说明：识别结果数，表示words_result的元素个数
    ## 字段：+words，	                    是否必选：否	    类型：string，	        说明：识别结果字符串
    ## 字段：probability，	            是否必选：否	    类型：object，	        说明：识别结果中每一行的置信度值，包含average：行置信度平均值，variance：行置信度方差，min：行置信度最小值
    'WEB_IMAGE': 'https://aip.baidubce.com/rest/2.0/ocr/v1/webimage',
    # 手写文字识别
    # URL参数：
    ## access_token	调用AccessToken模块获取
    # Headers参数
    ## 参数：Content-Type	，值：application/x-www-form-urlencoded
    # Body请求参数：
    ## 参数：image，                   是否必选：是	，           类型：string，    可选值范围：NULL，                  说明：图像数据，base64编码后进行urlencode，要求base64编码和urlencode后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式
    ## 参数：recognize_granularity，   是否必选：false，        类型：string，    可选值范围：[big、small]，           说明：是否定位单字符位置，big：不定位单字符位置，默认值；small：定位单字符位置
    ## 参数：words_type，              是否必选：false，        类型：string，    可选值范围：[默认/number]，          说明：words_type=number:手写数字识别；无此参数或传其它值 默认手写通用识别（目前支持汉字和英文）
    # ---------------------------------------------------------------------------------------
    # 返回说明:
    ## 字段：log_id，	                是否必选：是	    类型：uint64，	            说明：唯一的log id，用于问题定位
    ## 字段：words_result_num，	    是否必选：是	    类型：uint32，	            说明：识别结果数，表示words_result的元素个数
    ## 字段：words_result，	        是否必选：是	    类型：array()	，	            说明：定位和识别结果数组
    ## 字段：location，	            是否必选：是	    类型：object，	            说明：位置数组（坐标0点为左上角）
    ## 字段：left，	                是否必选：是	    类型：uint32	，	            说明：表示定位位置的长方形左上顶点的水平坐标
    ## 字段：top，	                是否必选：是	    类型：uint32，	            说明：表示定位位置的长方形左上顶点的垂直坐标
    ## 字段：width，	                是否必选：是	    类型：uint32，	            说明：表示定位位置的长方形的宽度
    ## 字段：height，	                是否必选：是	    类型：uint32，	            说明：表示定位位置的长方形的高度
    ## 字段：words，	                是否必选：是	    类型：string，	            说明：识别结果字符串
    ## 字段：chars，	                是否必选：否	    类型：array()，	            说明：单字符结果，recognize_granularity=small时存在
    ## 字段：location，	            是否必选：是	    类型：array()	，	            说明：位置数组（坐标0点为左上角）
    ## 字段：left，	                是否必选：是	    类型：uint32，	            说明：表示定位位置的长方形左上顶点的水平坐标
    ## 字段：top，	                是否必选：是	    类型：uint32，	            说明：表示定位位置的长方形左上顶点的垂直坐标
    ## 字段：width，	                是否必选：是	    类型：uint32，	            说明：表示定位定位位置的长方形的宽度
    ## 字段：height，	                是否必选：是	    类型：uint32，	            说明：表示位置的长方形的高度
    ## 字段：char，	                是否必选：是	    类型：string，	            说明：单字符识别结果
    ## 字段：probability，	        是否必选：否	    类型：object，	            说明：识别结果中每一行的置信度值，包含average：行置信度平均值，variance：行置信度方差，min：行置信度最小值
    'HANDWRITING': 'https://aip.baidubce.com/rest/2.0/ocr/v1/handwriting',
    # 数字识别
    # URL参数：
    ## access_token	调用AccessToken模块获取
    # Headers参数
    ## 参数：Content-Type	，值：application/x-www-form-urlencoded
    # Body请求参数：
    ## 参数：image，                         是否必选：TRUE，           类型：string，    可选值范围：null，                     说明：图像数据，base64编码后进行urlencode，要求base64编码和urlencode后大小不超过4M，最短边至少15px，最长边最大4096px,支持jpg/png/bmp格式
    ## 参数：recognize_granularity	       是否必选：false	        类型：string      可选值范围：	big、small	             说明：是否定位单字符位置，big：不定位单字符位置，默认值；small：定位单字符位置
    ## 参数：detect_direction		           是否必选：FALSE             类型：string	 可选值范围：true、false	             说明：是否检测图像朝向，默认不检测，即：false。可选值包括true - 检测朝向；false - 不检测朝向。朝向是指输入图像是正常方向、逆时针旋转90/180/270度。
    # ---------------------------------------------------------------------------------------
    # 返回说明:
    # log_id	是	uint64	唯一的log id，用于问题定位
    # words_result_num	是	uint32	识别结果数，表示words_result的元素个数
    # words_result	是	array()	定位和识别结果数组
    # location	是	object	位置数组（坐标0点为左上角）
    # left	是	uint32	表示定位位置的长方形左上顶点的水平坐标
    # top	是	uint32	表示定位位置的长方形左上顶点的垂直坐标
    # width	是	uint32	表示定位位置的长方形的宽度
    # height	是	uint32	表示定位位置的长方形的高度
    # words	是	string	识别结果字符串
    # chars	否	array()	单字符结果，recognize_granularity=small时存在
    # location	是	array()	位置数组（坐标0点为左上角）
    # left	是	uint32	表示定位位置的长方形左上顶点的水平坐标
    # top	是	uint32	表示定位位置的长方形左上顶点的垂直坐标
    # width	是	uint32	表示定位定位位置的长方形的宽度
    # height	是	uint32	表示位置的长方形的高度
    # char	是	string	单字符识别结果
    'NUMBERS': 'https://aip.baidubce.com/rest/2.0/ocr/v1/numbers'
}
