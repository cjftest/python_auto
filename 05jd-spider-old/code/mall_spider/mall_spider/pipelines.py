# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


"""
实现保存分类的Pipeline类
    1、open_spider方法中，链接MongoDB数据库，获取要操作的集合
    2、process_item方法中，向MongoDB中插入类别数据
    3、close_spider方法中，关闭MongoDB的链接
"""

from pymongo import MongoClient
from mall_spider.settings import MONGODB_URL
from mall_spider.spiders.jd_category import JdCategorySpider


class CategoryPipeline(object):

    def open_spider(self,spider):
        """当爬虫启动的时候执行"""
        if isinstance(spider,JdCategorySpider):
            #  1、open_spider方法中，链接MongoDB数据库，获取要操作的集合
            self.client = MongoClient(MONGODB_URL)
            self.collection = self.client['jd']['category']


    def process_item(self, item, spider):
        # 2、process_item方法中，向MongoDB中插入类别数据
        if isinstance(spider,JdCategorySpider):
            self.collection.insert_one(dict(item))
        return item

    def close_spider(self,spider):
        # 3、close_spider方法中，关闭MongoDB的链接
        if isinstance(spider,JdCategorySpider):
            self.client.close()
