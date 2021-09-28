# _*_ coding : UTF-8 _*_
# 开发团队 : 柴俊峰
# 开发人员 ：柴俊峰
# 开发时间 ：2020/11/12 22:53
# 文件名称 : demo2.py
# 开发工具 ：PyCharm

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait

# wd = webdriver.Chrome()
# wd.implicitly_wait(5)
# wd.get("http://www.baidu.com")
# wd.find_element_by_id("kw").send_keys("白夜黑羽")
# wd.find_element_by_id("su").click()
# wd.quit()

# wd = webdriver.Chrome()
# wd.get("http://cdn1.python3.vip/files/selenium/sample1.html")
# try:
#     elements = wd.find_element_by_class_name("animal12")
#     print(elements.text)
# except NoSuchElementException:
#     print("发生异常")
# finally:
#     print("退出")
#     wd.quit()


# wd = webdriver.Chrome()
# wd.implicitly_wait(5)
# wd.get("http://cdn1.python3.vip/files/selenium/sample1.html")
# try:
#     elements = wd.find_element_by_class_name("animal11")
#     print(elements.text)
# except NoSuchElementException:
#     print("没有找到animal属性")
#     # for element in elements:
#     #     print(element.text)
# finally:
#     wd.quit()


wd = webdriver.Chrome()
wd.implicitly_wait(5)
wd.get("http://cdn1.python3.vip/files/selenium/sample1.html")
# elements = wd.find_elements_by_css_selector("#container > div")
# for element in elements:
#     print("-----------")
#     print(element.text)
element = wd.find_element_by_css_selector(".footer2 [href='http://www.miitbeian.gov.cn']")
print(element.text)
wd.quit()