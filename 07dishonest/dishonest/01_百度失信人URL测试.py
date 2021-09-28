

import requests

url = 'https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=6899&query=失信人&pn=0&rn=10&from_mid=1&ie=utf-8&oe=utf-8'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'Referer':'https://www.baidu.com/s?ie=UTF-8&wd=%E5%A4%B1%E4%BF%A1%E4%BA%BA'
}

response = requests.get(url,headers=headers)

print(response.content.decode('utf8'))