# _*_ coding : UTF-8 _*_
# 开发团队 : 柴俊峰
# 开发人员 ：柴俊峰
# 开发时间 ：2020/12/3 23:33
# 文件名称 : 爬虫-代理ip.py
# 开发工具 ：PyCharm


import requests
from fake_useragent import UserAgent
from lxml import etree
import time


#爬取快代理ip
def kuaidaili():
    urls = "https://www.kuaidaili.com/free/inha/{}"
    ua = UserAgent()
    headers = {
        'User-Agent':ua.random
    }
    ips = []
    for i in range(1,5):
        time.sleep(1)
        url = urls.format(i)
        # print(f"正在爬取第{i}页")
        print("正在爬取第%d页" % (i))
        try:
            response = requests.get(url,headers=headers,timeout=5).content.decode('utf8')
            resdata = etree.HTML(response)
            resip = resdata.xpath('//table[@class="table table-bordered table-striped"]//tr/td[1]/text()')
            resport = resdata.xpath('//table[@class="table table-bordered table-striped"]//tr/td[2]/text()')
            data = list(zip(resip,resport))
            ips.append(data)
            # print(data)
            print(len(data))
        except:
            print("请求失败！")

    print(ips)


#爬取西拉代理
# urls = "http://www.xiladaili.com/gaoni/{}"
# ua = UserAgent()
# headers = {
#     'User-Agent':ua.random
# }
# for i in range(1,4):
#     # time.sleep(1)
#     url = urls.format(i)
#     print(url)
#     try:
#         # ip = []
#         response = requests.get(url, headers=headers).content.decode('utf8')
#         res = etree.HTML(response)
#         resips = res.xpath('//table[@class="fl-table"]//tr/td[1]/text()')
#         print(resips)
#         print(len(resips))
#         # for item in resips:
#         #     resip = item.xpath('./td[1]/text()')
#         #     ip.append(resip)
#         #
#         #     # resip = resip[1:]
#         #     # print(resip)
#     except:
#         print("请求失败")
#
# # print(ip[1:])



if __name__ == '__main__':
    kuaidaili()