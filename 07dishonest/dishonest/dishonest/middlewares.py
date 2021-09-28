# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
import requests
from dishonest.settings import USER_AGENT

"""
实现随机User-Agent下载器中间
    1、准备User-Agent列表
    2、实现RandomUserAgent类
    3、实现process_request方法，设置随机的User-Agent
"""


class RandomUserAgent:

    def process_request(self, request, spider):
        # 3、实现process_request方法，设置随机的User-Agent
        request.headers['User-Agent'] = random.choice(USER_AGENT)

        return None


"""
实现代理IP下载器中间
    1、定义ProxyMiddleware类
    2、实现process_request方法，设置代理IP
"""

class ProxyMiddleware:

    def process_request(self, request, spider):
        # 实现process_request方法，设置代理IP
        # 1、获取协议头
        protocol = request.url.split('://')[0]
        # 2、构建代理IP请求的URL
        proxy_url = "http://localhost:16888/random?protocol={}".format(protocol)
        # 3、发送请求，获取代理IP
        response = requests.get(proxy_url)
        # 4、把代理IP设置给request.meta['proxy']
        request.meta['proxy'] = response.content.decode()

        return None
