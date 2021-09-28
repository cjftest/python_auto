# _*_ coding : UTF-8 _*_
# 开发团队 : 柴俊峰
# 开发人员 ：柴俊峰
# 开发时间 ：2020/12/2 22:39
# 文件名称 : 爬虫-代理IP.py
# 开发工具 ：PyCharm


from fake_useragent import UserAgent
import requests

ua = UserAgent()
url = 'http://httpbin.org/get'
headers = {
    'User-Agent': ua.random
}
# print(headers)
proxies = {
    'http':'110.44.117.26:43922',
    'http':'197.248.7.229:8080',
    'https':'123.163.117.170:9999'
}
try:
    response = requests.get(url, headers=headers,proxies=proxies,timeout=10)
    if response.status_code == 200:
        res = response.json()
        print("本地ip为：",res['origin'])
except:
    print("请求失败")
