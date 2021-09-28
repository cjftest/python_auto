# _*_ coding : UTF-8 _*_
# 开发团队 : 柴俊峰
# 开发人员 ：柴俊峰
# 开发时间 ：2020/11/26 22:46
# 文件名称 : demo1.py
# 开发工具 ：PyCharm

import requests
from lxml import html

url = "http://www.qzwb.com/gb/node/node_538.htm"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
}
response = requests.get(url,headers=headers).content.decode('utf8')
lxml_code = html.etree
lxml_data = lxml_code.HTML(lxml_code)
print(lxml_data)
# with open('data.html','wb') as f:
#     f.write(response)
#     f.close()
# print(response)