# _*_ coding : UTF-8 _*_
# 开发团队 : 柴俊峰
# 开发人员 ：柴俊峰
# 开发时间 ：2021/1/12 23:34
# 文件名称 : proxy_spider.py
# 开发工具 ：PyCharm


from base_spider import BaseSpider
import time
import random
# import requests
# import js2py

"""
1、实现jiangxianli 代理ip的爬虫：https://ip.jiangxianli.com/?page=1
    定义一个类，继承通用爬虫类（BaseSpider)
    提供urls，group_xpath 和 detail_xpath
"""

class JiangxianliSpider(BaseSpider):

    # 准备url列表
    urls = ['https://ip.jiangxianli.com/?page={}'.format(i) for i in range(1,9)]
    # 分组的xpath，用于获取包含代理ip信息的标签列表
    group_xpath = '/html/body/div[1]/div[2]/div[1]/div[1]/table/tbody/tr'
    # 组内xpath，用于提取 ip，port，area
    detail_xpath = {
        'ip':'./td[1]/text()',
        'port':'./td[2]/text()',
        'area':'./td[5]/text()'
    }

"""
2、实现云代理 代理ip的爬虫：https://ip.jiangxianli.com/?page=1
    定义一个类，继承通用爬虫类（BaseSpider)
    提供urls，group_xpath 和 detail_xpath
"""
class Ip3366Spider(BaseSpider):

    # 准备url列表
    urls = ['http://www.ip3366.net/free/?stype={}&page={}'.format(i,j) for i in range(1,3) for j in range(1,8)]
    # 分组的xpath，用于获取包含代理ip信息的标签列表
    group_xpath = '//*[@id="list"]/table/tbody/tr'
    # 组内xpath，用于提取 ip，port，area
    detail_xpath = {
        'ip':'./td[1]/text()',
        'port':'./td[2]/text()',
        'area':'./td[6]/text()'
    }

"""
3、实现快代理 代理ip的爬虫：https://www.kuaidaili.com/free/inha/2/
    定义一个类，继承通用爬虫类（BaseSpider)
    提供urls，group_xpath 和 detail_xpath
"""
class KuaidailiSpider(BaseSpider):
    # 准备url列表
    urls = ['https://www.kuaidaili.com/free/inha/{}'.format(i) for i in range(1,9)]
    # 分组的xpath，用于获取包含代理ip信息的标签列表
    group_xpath = '//*[@id="list"]/table/tbody/tr'
    # 组内xpath，用于提取 ip，port，area
    detail_xpath = {
        'ip':'./td[1]/text()',
        'port':'./td[2]/text()',
        'area':'./td[5]/text()'
    }
    # 当我们访问两个页面时间间隔太短，就报错了，这是一种反扒手段
    def get_page_from_url(self,url):
        # 随机等待1-3s
        time.sleep(random.uniform(1,3))
        # 调用父类方法，发送请求，获取响应数据
        return super().get_page_from_url(url)


"""
4、实现proxylistplus 代理ip的爬虫：https://list.proxylistplus.com/Fresh-HTTP-Proxy-List-2
    定义一个类，继承通用爬虫类（BaseSpider)
    提供urls，group_xpath 和 detail_xpath
"""
class ProxylistplusSpider(BaseSpider):

    # 准备url列表
    urls = ['https://list.proxylistplus.com/Fresh-HTTP-Proxy-List-{}'.format(i) for i in range(1,6)]
    # 分组的xpath，用于获取包含代理ip信息的标签列表
    group_xpath = '//*[@id="page"]/table[2]/tr[position()>2]'
    # 组内xpath，用于提取 ip，port，area
    detail_xpath = {
        'ip':'./td[2]/text()',
        'port':'./td[3]/text()',
        'area':'./td[5]/text()'
    }

"""
5、实现66ip 代理ip的爬虫：http://www.66ip.cn/2.html
    定义一个类，继承通用爬虫类（BaseSpider)
    提供urls，group_xpath 和 detail_xpath
"""
class Ip66Spider(BaseSpider):

    # 准备url列表
    urls = ['http://www.66ip.cn/{}.html'.format(i) for i in range(1,11)]
    # 分组的xpath，用于获取包含代理ip信息的标签列表
    group_xpath = '//*[@id="main"]/div[1]/div[2]/div[1]/table/tr[position()>1]'
    # 组内xpath，用于提取 ip，port，area
    detail_xpath = {
        'ip':'./td[1]/text()',
        'port':'./td[2]/text()',
        'area':'./td[3]/text()'
    }

if __name__ == '__main__':
    # spider = JiangxianliSpider()
    spider = Ip3366Spider()
    # spider = KuaidailiSpider()
    # spider = ProxylistplusSpider()
    # spider = Ip66Spider()
    for proxy in spider.get_proxies():
        print(proxy)

    # 测试66ip代理： http://www.66ip.cn/1.html
    # url = 'http://www.66ip.cn/3.html'
    # response = requests.get(url=url)
    # print(response.status_code)
    # print(response.content.decode('gbk'))
    # context = js2py.EvalJs()