# _*_ coding : UTF-8 _*_
# 开发团队 : 柴俊峰
# 开发人员 ：柴俊峰
# 开发时间 ：2020/12/1 23:02
# 文件名称 : 爬虫-有道翻译.py
# 开发工具 ：PyCharm


def fanyi(keywords):
    '''
    1、此功能为有道翻译
    '''

    '''
    Request URL: http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule
    Request Method: POST
    '''
    import requests
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    data = {
        'i': keywords,
        'doctype': 'json'
    }
    try:
        res = requests.post(url, data=data)
        if res.status_code == 200:
            resdata = res.json()
            # print(resdata)
            print("翻译结果为：", resdata['translateResult'][0][0]['tgt'])
    except:
        print("翻译出错了，请重试！")


vas = """
***********************
*** 欢迎使用py翻译    ***
*** 输入字母q退出     ***
***********************
"""
print(vas)

while True:
    keywords = input("请输入你想要翻译的内容：")
    if keywords == "q":
        break
    else:
        fanyi(keywords)
        print("\n")