import scrapy
import json
from jsonpath import jsonpath
from datetime import datetime
import pymysql



from dishonest.items import DishonestItem


"""
完善爬虫
步骤：
    1、起始URL
    2、生成所有页面的请求
    3、解析页面，提取需要的数据
"""

"""
创建数据库
create datebase dishonest;
创建表
CREATE TABLE dishonest(
dishonest_id INT NOT NULL AUTO_INCREMENT, -- ID 主键
age INT NOT NULL,  -- 年龄，自然人年龄都是>0的，企业的年龄等于0
name VARCHAR(200) NOT NULL,		-- 失信人名称
card_num VARCHAR(50),		-- 失信人号码
area VARCHAR(50) NOT NULL,		-- 区域
content VARCHAR(2000) NOT NULL,		-- 失信内容
business_entity VARCHAR(20),		-- 企业法人
publish_unit VARCHAR(200),		-- 发布单位
publish_date VARCHAR(20),		-- 公布日期
create_date DATETIME,		-- 创建日期
update_date DATETIME,		-- 更新日期
PRIMARY KEY (dishonest_id)
);
"""

class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=6899&query=失信人&pn=0&rn=10&from_mid=1&ie=utf-8&oe=utf-8']

    def parse(self, response):
        # 构建所有页面请求
        # 把响应内容的json字符串，转换为字典
        results = json.loads(response.text)
        # 取出总数据条数
        disp_num = jsonpath(results,'$..dispNum')[0]
        # print(disp_num)
        # URL模板
        url_pattern = 'https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=6899&query=失信人&pn={}&rn=10&from_mid=1&ie=utf-8&oe=utf-8'
        # 每隔10条创建一个请求
        for pn in range(0,disp_num,10):
            # 构建URL
            url = url_pattern.format(pn)
            # 创建请求，交给引擎
            yield scrapy.Request(url,callback=self.parse_data)

    def parse_data(self,response):
        # 解析数据
        # 响应数据
        datas = json.loads(response.text)
        results = jsonpath(datas,'$..disp_data')[0]
        # print(len(results))
        for result in results:
            item = DishonestItem()
            # 失信人名称
            item['name'] = result['iname']
            # 失信人号码
            item['card_num'] = result['cardNum']
            # 失信人年龄
            item['age'] = int(result['age'])
            # 区域
            item['area'] = result['areaName']
            # 法人（企业）
            item['business_entity'] = result['businessEntity']
            # 失信内容
            item['content'] = result['duty']
            # 公布日期
            item['publish_date'] = result['publishDate']
            # 公布 / 执行单位
            item['publish_unit'] = result['courtName']
            # 创建日期
            item['create_date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # 更新日期
            item['update_date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # print(item)
            # 把数据交给引擎
            yield item




