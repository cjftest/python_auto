# _*_ coding : UTF-8 _*_
# 开发团队 : 柴俊峰
# 开发人员 ：柴俊峰
# 开发时间 ：2021/1/12 23:32
# 文件名称 : mongo_pool.py
# 开发工具 ：PyCharm

"""
7、实现代理池的数据库模块
作用：用于对proxies集合进行数据库的相关操作
目标：实现对数据库增删查改相关操作
步骤：
1、在init中，建立数据库连接，获取要操作的集合，在 del 方法中关闭数据库连接
2、提供基础的增删查改功能
    2.1 实现插入功能
    2.2 实现修改功能
    2.3 实现删除代理：根据代理的ip删除
    2.4 查询所有代理ip的功能
3、提供代理API模块使用的功能
    3.1、实现查询功能：根据条件进行查询，可以指定查询数量，先分数降序，速度升序排，保证优质的代理IP在上面
    3.2、实现根据协议类型 和 要访问网站的域名，获取代理IP列表
    3.3、实现根据协议类型 和 要访问网站的域名，随机获取一个代理IP
    3.4、实现把指定域名添加到指定IP的disable_domain列表中
"""

from pymongo import MongoClient
from settings import MONGO_URL
from utils.log import logger
from domain import Proxy
import pymongo
import random
from core.proxy_validate.httpbin_validator import check_proxy


class MongoPool(object):

    def __init__(self):
        # 1.1、在init中，建立数据库连接
        self.client = MongoClient(MONGO_URL)
        # 1.2 获取要操作的集合
        self.proxies = self.client['proxies_pool']['proxies']

    def __del__(self):
        # 1.3 关闭数据库连接
        self.client.close()

    def insert_one(self,proxy):
        """2.1 实现插入功能"""
        count = self.proxies.count_documents({'_id':proxy.ip})
        if count == 0:
            # 我们使用proxy.ip作为 MongoDB中数据的主键：_id
            dic = proxy.__dict__
            dic['_id'] = proxy.ip
            self.proxies.insert_one(dic)
            logger.info("插入新的代理：{}".format(proxy))
        else:
            logger.warning("已经存在的代理：{}".format(proxy))

    def update_one(self,proxy):
        """2.2 实现修改功能"""
        self.proxies.update_one({'_id':proxy.ip},{'$set':proxy.__dict__})
        logger.info("修改代理ip:{}".format(proxy))

    def delete_one(self,proxy):
        """2.3 实现删除代理：根据代理的ip删除"""
        self.proxies.delete_one({'_id':proxy.ip})
        logger.info("删除代理ip：{}".format(proxy))

    def find_all(self):
        """2.4 查询所有代理ip的功能"""
        cursor = self.proxies.find()
        for item in cursor:
            # 删除_id这个key
            # item.pop('_id')
            del item['_id']
            proxy = Proxy(**item)
            yield proxy

    def find(self,conditions={},count=0):
        """
        3.1、实现查询功能：根据条件进行查询，可以指定查询数量，先分数降序，速度升序排，保证优质的代理IP在上面
        :param conditions:查询条件字典
        :param count:限制最多取出多少个代理IP
        :return:返回满足要求代理IP（Proxy对象）列表
        """
        cursor = self.proxies.find(conditions,limit=count).sort(
            [('score',pymongo.DESCENDING),('speed',pymongo.ASCENDING)]
        )
        # 准备列表，用来存储查询处理代理IP
        proxy_list = []
        # 遍历 cursor
        for item in cursor:
            item.pop('_id')
            # del item['_id']
            proxy = Proxy(**item)
            proxy_list.append(proxy)
        # 返回满足要求代理IP（Proxy对象）列表
        return proxy_list

    def get_proxies(self,protocol=None,domain=None,count=0,nick_type=0):
        """
        3.2、实现根据协议类型 和 要访问网站的域名，获取代理IP列表
        :param protocol:协议：http，https
        :param domain:域名：jd.com
        :param count: 用于限制获取多个代理IP，默认是获取所有的
        :param nick_type: 匿名类型，默认获取高匿的代理ip
        :return: 满足要求的代理ip的列表
        """
        # 定义查询条件
        conditions = {'nick_type':nick_type}
        # 根据协议，指定查询条件
        if protocol is None:
            # 如果没有传入协议类型，返回支持http和https的代理IP
            conditions['protocol'] = 2
        elif protocol.lower() == 'http':
            conditions['protocol'] = {'$in':[0,2]}
        else:
            conditions['protocol'] = {'$in':[1,2]}

        if domain:
            conditions['disable_domains'] = {'$nin':[domain]}

        # 满足要求的代理ip的列表
        return self.find(conditions,count=count)


    def random_proxy(self,protocol=None,domain=None,count=0,nick_type=0):
        """
        3.3、实现根据协议类型 和 要访问网站的域名，随机获取一个代理IP
        :param protocol:协议：http，https
        :param domain:域名：jd.com
        :param count: 用于限制获取多个代理IP，默认是获取所有的
        :param nick_type: 匿名类型，默认获取高匿的代理ip
        :return: 满足要求的随机的一个代理IP（Proxy对象）
        """

        proxy_list = self.get_proxies(protocol=protocol,domain=domain,count=count,nick_type=nick_type)
        # 从 proxy_list 列表中随机取出一个代理IP返回
        return random.choice(proxy_list)

    def disable_domain(self,ip,domain):
        """
        3.4、实现把指定域名添加到指定IP的disable_domain列表中
        :param ip: IP地址
        :param domain: 域名
        :return: 如果返回True，表示添加成功，返回false，添加失败
        """
        # print(self.proxies.count_documents({'_id':ip, 'disable_domains':domain}))
        if self.proxies.count_documents({'_id':ip, 'disable_domains':domain}) == 0:
            # 如果disable_domains 字段中没有这个域名，才添加
            self.proxies.update_one({'_id':ip},{'$push':{'disable_domains':domain}})
            return True
        else:
            return False

if __name__ == '__main__':
    mongo = MongoPool()
    # proxy = Proxy(ip='115.221.247.33', port='9999')

    # proxy = Proxy(ip='103.115.255.186',port='80')
    # print(proxy)
    # proxy = check_proxy(proxy)
    # print(proxy.speed)
    # if proxy.speed > -1:
    #     mongo.insert_one(proxy)
    #     print("插入成功{}".format(proxy))
    # else:
    #     print("无需插入")

    # mongo.insert_one(proxy)
    # proxy = Proxy(ip='115.221.247.33', port='8888')
    # mongo.update_one(proxy)
    # proxy = Proxy(ip='115.221.247.33', port='8888')
    # mongo.delete_one(proxy)

    # for proxy in mongo.find_all():
    #     print(proxy)

    # dic = {'ip': '103.115.255.187', 'port': '80', 'protocol': 0, 'nick_type': 0, 'speed': 4.5, 'area': None, 'score': 49, 'disable_domains': ['taobao.com']}
    # dic = {'ip': '103.115.255.188', 'port': '80', 'protocol': 0, 'nick_type': 0, 'speed': 3.5, 'area': None, 'score': 48, 'disable_domains': ['jingdong.com']}
    # dic = {'ip': '103.115.255.190', 'port': '80', 'protocol': 0, 'nick_type': 2, 'speed': 6.5, 'area': None, 'score': 47, 'disable_domains': ['jd.com']}
    # proxy = Proxy(**dic)
    # mongo.insert_one(proxy)

    # for proxy in mongo.find({'nick_type':0},count=10):
    #     print(proxy)

    # for proxy in mongo.get_proxies(protocol='https'):
    for proxy in mongo.get_proxies(protocol='http',domain='taobao.com'):
        print(proxy)

    # print(mongo.random_proxy(protocol='http',domain='taobao.com'))

    # mongo.disable_domain('103.115.255.187','baidu.com')
    # for proxy in mongo.find_all():
    #     print(proxy)
