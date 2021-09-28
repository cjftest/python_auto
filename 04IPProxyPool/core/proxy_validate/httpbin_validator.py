# _*_ coding : UTF-8 _*_
# 开发团队 : 柴俊峰
# 开发人员 ：柴俊峰
# 开发时间 ：2021/1/12 23:32
# 文件名称 : httpbin_validator.py
# 开发工具 ：PyCharm



'''
实现代理池的校验模块
目标：检查代理IP速度，
步骤：匿名程度以及支持的协议类型
检查代理IP速度和匿名程度：
    1、代理IP速度：就是从发送请求到获取响应的时间间隔
    2、匿名程度检查：
        1、对 http://httpbin.org/get 或 https://httpbin.org/get 发送请求
        2、如果响应的origin中有 ','分割的两个IP就是透明代理IP
        3、如果响应的headers中包含 Proxy-Connection 说明是匿名代理IP
        4、否则就是高匿代理IP
检查代理IP协议类型：
    如果 http://httpbin.org/get 发送请求可以成功，说明支持http协议
    如果 https://httpbin.org/get 发送请求可以成功，说明支持https协议
'''
import json
import time
import requests


from utils.http import get_request_headers
from settings import TEST_TIMEOUT
from utils.log import logger
from domain import Proxy

def check_proxy(proxy):
    """
    用于检查指定 代理 IP 响应速度，匿名程度，支持协议类型
    :param proxy:代理IP模型对象
    :return:检查后的代理ip模型对象
    """
    # 准备代理ip字典
    proxies = {
        'http':'http://{}:{}'.format(proxy.ip,proxy.port),
        'https':'https://{}:{}'.format(proxy.ip,proxy.port)
    }
    # 测试该代理ip
    http,http_nick_type,http_speed = _check_http_proxies(proxies)
    https,https_nick_type,https_sspeed = _check_http_proxies(proxies,False)
    # protocol 代理ip支持的协议类型，http是0，https是1，http和https都支持是2
    if http and https:
        proxy.protocol =2
        proxy.nick_type = http_nick_type
        proxy.speed = http_speed
    elif https:
        proxy.protocol = 1
        proxy.nick_type = https_nick_type
        proxy.speed = https_sspeed
    elif http:
        proxy.protocol = 0
        proxy.nick_type = http_nick_type
        proxy.speed = http_speed
    else:
        proxy.protocol = -1
        proxy.nick_type = -1
        proxy.speed = -1
    return proxy


def _check_http_proxies(proxies,is_http=True):
    # 匿名类型：高匿：0，匿名：1，透明：2，
    nick_type = -1
    # 响应速度，单位：s
    speed = -1
    if is_http:
        test_url = 'http://httpbin.org/get'
    else:
        test_url = 'https://httpbin.org/get'
    # 获取开始时间
    start = time.time()
    try:
        # 发送请求，获取响应数据
        response = requests.get(test_url,headers=get_request_headers(),proxies=proxies,timeout=TEST_TIMEOUT)
        if response.ok:
            # 计算响应速度
            speed = round(time.time()-start,2)
            # 匿名程度
            # 把响应的json字符串转换为字典
            dic = json.loads(response.text)
            # 获取响应ip：origin
            origin = dic['origin']
            proxy_connection = dic['headers'].get('Proxy-Connection',None)
            # 1、如果响应的origin中有 ','分割的两个IP就是透明代理IP
            if ',' in origin:
                nick_type = 2
            # 2、如果响应的headers中包含 Proxy-Connection 说明是匿名代理IP
            elif proxy_connection:
                nick_type = 1
            # 3、否则就是高匿代理IP
            else:
                nick_type = 0
            return True,nick_type,speed
        return False,nick_type,speed
    except Exception as ex:
        #logger.exception(ex)
        return False,nick_type,speed


if __name__ == '__main__':
    proxy = Proxy('49.81.246.192',port='8888')
    print(check_proxy(proxy))



