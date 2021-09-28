# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


import pymysql
from dishonest.settings import MYSQL_HOST,MYSQL_DB,MYSQL_PORT,MYSQL_USER,MYSQL_PASSWORD

"""
步骤：
1、在open_spider中，建立数据库连接，获取操作的数据的cursor
2、在close_spider中，关闭cursor，关闭数据库连接
3、在process_item中，如果数据不存在，保存数据
"""

class DishonestPipeline(object):

    def open_spider(self,spider):
        """
        1、在open_spider中，建立数据库连接，获取操作的数据的cursor
        """
        # 建立数据库连接
        self.connection = pymysql.connect(host=MYSQL_HOST,user=MYSQL_USER,port=MYSQL_PORT,
                                          password=MYSQL_PASSWORD,db=MYSQL_DB)
        # 获取操作的数据的cursor
        self.cursor = self.connection.cursor()

    def close_spider(self,spider):
        """
        2、在close_spider中，关闭cursor，关闭数据库连接
        """
        # 1、关闭cursor
        self.cursor.close()
        # 2、关闭数据库连接
        self.connection.close()

    def process_item(self, item, spider):
        """
        3、在process_item中，如果数据不存在，保存数据
        """
        # 如果是自然人，根据身份证号进行判断
        # 如果是企业/组织，根据 企业名称和区域进行判断
        # 如何判断是企业还是自然人， 如果年龄是0就是企业，否则就是自然人
        if item['age'] == 0:
            # 如果是企业，根据企业名称和区域进行判断是否重复
            select_count_sql = "SELECT COUNT(1) FROM dishonest WHERE name='{}' AND area='{}'"\
                .format(item['name'],item['area'])
        else:
            # 否则就是自然人
            select_count_sql = "SELECT COUNT(1) FROM dishonest WHERE card_num='{}'".format(item['card_num'])
        # 执行查询sql
        self.cursor.execute(select_count_sql)
        # 获取查询结果
        count = self.cursor.fetchone()[0]
        if count == 0:
            keys, values = zip(*dict(item).items())
            # 如果没有数据，就插入数据
            insert_sql = "INSERT INTO dishonest ({}) VALUES ({})".format(
                ','.join(keys),
                ','.join(['%s'] * len(keys))
            )
            # 执行sql
            self.cursor.execute(insert_sql,values)
            #  提交事务
            self.connection.commit()
            spider.logger.info('插入数据')
        else:
            #否则就重复了
            spider.logger.info('数据重复')

        return item
