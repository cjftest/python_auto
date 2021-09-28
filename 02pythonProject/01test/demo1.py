# _*_ coding : UTF-8 _*_
# 开发团队 : 柴俊峰
# 开发人员 ：柴俊峰
# 开发时间 ：2020/10/26 23:24
# 文件名称 : demo1.py
# 开发工具 ：PyCharm


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time

# wd = webdriver.Chrome()
# wd.get('https://www.baidu.com')
# wd.implicitly_wait(10)
# element = wd.find_element_by_id('kw')
# element.send_keys('白月黑羽')
# time.sleep(1.5)
# element = wd.find_element_by_id('su')
# element.click()
# time.sleep(2)
# wd.close()

# wb = webdriver.Chrome()
# wb.implicitly_wait(5)
# wb.get('https://www.baidu.com')
# element = wb.find_element_by_id('kw')
# element.send_keys('白月黑羽')
# element = wb.find_element_by_id('su').click()
# element = wb.find_element_by_id('1').get_attribute('srcid')
# print(element)
# wb.quit()

# wb = webdriver.Chrome()
# wb.get("http://cdn1.python3.vip/files/selenium/sample1.html")
# elements = wb.find_elements_by_class_name("animal")
# for element in elements:
#     print(element.text)
#
# print("\n")
# elements = wb.find_elements_by_tag_name("span")
# for element in elements:
#     print(element.text)
#
# wb.quit()

# wb = webdriver.Chrome()
# wb.implicitly_wait(5)
# wb.get("https://www.baidu.com")
# element = wb.find_element_by_id('kw').send_keys("白夜黑羽\n")
# # element.send_keys("白夜黑羽\n")
# element = wb.find_element_by_id('su').click()
# # time.sleep(2)
# element = wb.find_element_by_id('1')
# print(element.text)
# wb.quit()

# wb = webdriver.Chrome()
# wb.implicitly_wait(5)
# wb.get("http://cdn1.python3.vip/files/selenium/sample1.html")
# element = wb.find_element_by_css_selector(".plant")
# print(element.text)
# print("........")
# element = wb.find_elements_by_css_selector("#container span")
# for elemen in element:
#     print(".....")
#     print(elemen)
# wb.quit()


# wb = webdriver.Chrome()
# wb.implicitly_wait(5)
# wb.get("http://cdn1.python3.vip/files/selenium/sample1b.html")
# element = wb.find_element_by_css_selector("span:nth-child(2)")
# print(element)
# wb.quit()


# wd = webdriver.Chrome()
# wd.implicitly_wait(5)
# wd.get("http://cdn1.python3.vip/files/selenium/sample2.html")
# # wd.switch_to.frame("frame1")
# wd.switch_to.frame(wd.find_element_by_css_selector('iframe[src="sample1.html"]'))
# # wd.switch_to.frame('iframe[src="sample1.html"]')  #此方法无效
# elements = wd.find_elements_by_css_selector(".plant")
# for element in elements:
#     print("......")
#     print(element.get_attribute('outerHTML'))
# # print(element.get_attribute('innerHTML'))  #此方法有效
#
# wd.switch_to.default_content()
# wd.find_element_by_id("outerbutton").click()
# # wd.quit()



# wd = webdriver.Chrome()
# wd.get("http://cdn1.python3.vip/files/selenium/sample3.html")
# wd.implicitly_wait(5)
# mainhandle = wd.current_window_handle
# link = wd.find_element_by_tag_name("a")
# time.sleep(2)
# link.click()
# print(wd.title)
# for handle in wd.window_handles:
#     wd.switch_to.window(handle)
#     if "Bing" in wd.title:
#         break
# print(wd.title)
# wd.find_element_by_id("sb_form_q").send_keys("白月黑羽")
# wd.find_element_by_id("sb_form_go").click()
# time.sleep(2)
# wd.switch_to.window(mainhandle)
# wd.find_element_by_id("outerbutton").click()
# wd.find_element_by_id("outerbutton").click()
# time.sleep(2)
# wd.quit()


# wd = webdriver.Chrome()
# wd.get("http://cdn1.python3.vip/files/selenium/test2.html")
# wd.implicitly_wait(5)
# element = wd.find_element_by_css_selector("#s_radio input[checked='checked']")
# print("当前选择的老师是",element.get_attribute("value"))
#
# element = wd.find_element_by_css_selector("#s_radio input[value='小雷老师']")
# print("当前选择的老师是",element.get_attribute("value"))
# element.click()
#
# wd.quit()


wd = webdriver.Chrome()
wd.get("http://cdn1.python3.vip/files/selenium/test2.html")
wd.implicitly_wait(5)
elements = wd.find_elements_by_css_selector("#s_checkbox input[checked='checked']")
for element in elements:
    element.click()

wd.find_element_by_css_selector("#s_checkbox input[value='小江老师']").click()
time.sleep(2)
wd.quit()