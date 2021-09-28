import requests

url = 'http://zxgk.court.gov.cn/shixin/searchSX.do'

# 准备数据

data = {
    'pName': '上海',
    'pCardNum':'',
    'pProvince': 0,
    'pCode': 'px4c',
    'captchaId': 'MeeT0MyleHCG2C01gjt9NW6WkLTv5sEH',
    'currentPage': 1,
}

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
}

response = requests.post(url=url,data=data)
print(response.content.decode())