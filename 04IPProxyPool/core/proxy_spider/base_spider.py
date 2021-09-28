# _*_ coding : UTF-8 _*_
# 开发团队 : 柴俊峰
# 开发人员 ：柴俊峰
# 开发时间 ：2021/1/12 23:34
# 文件名称 : base_spider.py
# 开发工具 ：PyCharm

import requests
from utils.http import get_request_headers
from lxml import etree
from domain import Proxy

"""
    目标：实现可以指定不同URL列表，分组的xpath和详情的xpath，从不同页面上提取代理的ip，端口号和区域的通用爬虫
    步骤：
    1、在base_spider.py文件中，定义一个BaseSpider类，继承Object
    2、提供三个类成员变量
        urls:代理ip网址的URL列表
        group_xpath:分组xpath，获取包含代理ip信息标签列表的xpath
        detail_xpath:组内xpath，获取代理ip详情的信息xpath，格式为：{'ip':'xx','port':'xx','area':'xx'}
    3、提供初始方法，传入爬虫URL列表，分组xpath，详情（组内）xpath
    4、对外提供一个获取代理ip的方法
        4、1 遍历URL列表，获取URL
        4、2 根据发送请求，获取页面数据
        4、3 解析页面，提取数据，封装为Proxy对象
        4、4 返回Proxy对象列表
"""

# 1、在base_spider.py文件中，定义一个BaseSpider类，继承Object
class BaseSpider(object):
    # 2、提供三个类成员变量
    # urls:代理ip网址的URL列表
    urls = []
    # group_xpath:分组xpath，获取包含代理ip信息标签列表的xpath
    group_xpath = ''
    # detail_xpath:组内xpath，获取代理ip详情的信息xpath，格式为：{'ip':'xx','port':'xx','area':'xx'}
    detail_xpath = {}

    # 3、提供初始方法，传入爬虫URL列表，分组xpath，详情（组内）xpath
    def __init__(self,urls =[],group_xpath='',detail_xpath ={}):
        if urls:
            self.urls = urls
        if group_xpath:
            self.group_xpath = group_xpath
        if detail_xpath:
            self.detail_xpath = detail_xpath

    def get_page_from_url(self,url):
        """ 根据url发送请求，获取页面数据 """
        response = requests.get(url,headers=get_request_headers())
        return response.content

    def get_first_from_list(self,lis):
        # 如果列表中有元素就返回第一个，否则返回空字符串
        return lis[0] if len(lis) !=0 else ''

    def get_proxies_from_page(self,page):
        """ 解析页面，提取数据，封装为Proxy对象 """
        element = etree.HTML(page)
        # 获取包含代理IP信息的标签列表
        trs = element.xpath(self.group_xpath)
        #  遍历trs，获取代理ip相关信息
        for tr in trs:
            ip = self.get_first_from_list(tr.xpath(self.detail_xpath['ip']))
            port = self.get_first_from_list(tr.xpath(self.detail_xpath['port']))
            area = self.get_first_from_list(tr.xpath(self.detail_xpath['area']))
            proxy = Proxy(ip=ip, port=port, area=area)
            # 使用yield返回提取到的数据
            yield proxy

    def get_proxies(self):
        # 4、对外提供一个获取代理ip的方法
        # 4、1 遍历URL列表，获取URL
        for url in self.urls:
            # 4、2 根据发送请求，获取页面数据
            page = self.get_page_from_url(url)
            # 4、3 解析页面，提取数据，封装为Proxy对象
            proxies = self.get_proxies_from_page(page)
            # 4、4 返回Proxy对象列表
            yield from proxies

if __name__ == '__main__':
    config = {
        'urls':['https://ip.jiangxianli.com/?page={}'.format(i) for i in range(1,4)],
        'group_xpath':'/html/body/div[1]/div[2]/div[1]/div[1]/table/tbody/tr',
        'detail_xpath':{
            'ip':'./td[1]/text()',
            'port':'./td[2]/text()',
            'area':'./td[5]/text()'
        }
    }

    spider = BaseSpider(**config)
    for proxy in spider.get_proxies():
        print(proxy)

