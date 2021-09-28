# _*_ coding : UTF-8 _*_
# 开发团队 : 柴俊峰
# 开发人员 ：柴俊峰
# 开发时间 ：2020/12/7 23:49
# 文件名称 : 爬虫-快代理ip.py
# 开发工具 ：PyCharm

import requests
import time
from fake_useragent import UserAgent
import json
# from lxml import etree
from lxml import etree


class SpiderKuaidaili(object):
    def __init__(self):
        ua = UserAgent()
        self.base_url = "https://www.kuaidaili.com/free/inha/{}"
        self.headers = {
            'User-Agent': ua.random
        }

    #获取url列表
    def get_url_list(self,n):
        print("获取url列表")
        url_list = []
        for i in range(1,n):
            url = self.base_url.format(i)
            url_list.append(url)
        return url_list

    #请求数据
    def getPage(self,url):
        print("请求数据")
        try:
            responses = requests.get(url,headers=self.headers,timeout=5)
            if responses.status_code == 200:
                responses = responses.content.decode('utf8')
                return responses
        except:
            return False

    #解析数据
    def parseHTML(self,responses):
        print("解析数据")
        response= etree.HTML(responses)
        resips = response.xpath('//table[@class="table table-bordered table-striped"]//tr/td[1]/text()')
        resports = response.xpath('//table[@class="table table-bordered table-striped"]//tr/td[2]/text()')
        resip = list(zip(resips,resports))
        resip = [{i[0]:i[1]} for i in resip]
        print(resip)
        return resip


        # resips = []
        # resports = []
        # for resdata in resdatas:
        #     resip = resdata.xpath('./td[1]/text()')
        #     resips.append(resip)
        #     resport = resdata.xpath('./td[2]/text()')
        #     resports.append(resport)
        # # okip = list(zip(resip,resport))
        # # return okip
        # print(resips[1:])
        # print(resports[1:])
        # resip = list(zip(resips[1:],resports[1:]))
        # print(resip)

    #验证数据

    #保存数据
    def save_data(self,data):
        print("保存数据")
        with open('ip文件.json','a+') as f:
            for i in data:
                # print(json.dumps(i))
                f.write(json.dumps(i))
                f.write("\n")
        f.close()

    #统筹数据
    def run(self):
        n = int(input("请输入你想要爬取的页数："))
        url_list = self.get_url_list(n)
        for url in url_list:
            # print(f"正在爬取第{i}页")
            time.sleep(2)
            responses = self.getPage(url)
            okip = self.parseHTML(responses)
            self.save_data(okip)


if __name__ == '__main__':
    SpiderKuaidaili().run()