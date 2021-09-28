# _*_ coding : UTF-8 _*_
# 开发团队 : 柴俊峰
# 开发人员 ：柴俊峰
# 开发时间 ：2021/1/12 23:37
# 文件名称 : proxy_api.py
# 开发工具 ：PyCharm

from flask import Flask
from flask import request
import json
from core.db.mongo_pool import MongoPool
from settings import PROXIES_MAX_COUNT

"""
1、在proxy_api.py中，创建ProxyApi类
2、实现初始方法
    2.1 初始一个Flask的Web服务
    2.2 实现根据协议类型和域名，提供随机的获取高可用代理ip的服务
        2.2.1 可用通过 protocol 和 domain 参数对ip进行过滤
        2.2.2 protocol：当前请求的协议类型
        2.2.3 domain： 当前请求域名
    2.3 实现根据协议类型和域名，提供获取多个高可用代理ip的服务
        2.3.1 可用通过 protocol 和 domain 参数对ip进行过滤
        2.3.2 实现给指定的i上追加上不可用域名的服务
    2.4 如果在获取ip的时候，有指定域名参数，将不在获取该ip，从而进一步提高代理ip的可用性
3、 实现run方法，用于启动Flask的Web服务
4、 实现start方法，用于通过类名，启动服务
"""


# 1、在proxy_api.py中，创建ProxyApi类
class ProxyApi(object):

    def __init__(self):
        # 2、实现初始方法
        # 2.1 初始一个Flask的Web服务
        self.app = Flask(__name__)
        # 创建MongoPool对象，用于操作数据库
        self.mongo_pool = MongoPool()

        @self.app.route('/random')
        def random():
            """
            http://localhost:16888/random?protocol=https&domain=jd.com

            2.2 实现根据协议类型和域名，提供随机的获取高可用代理ip的服务
                2.2.1 可用通过 protocol 和 domain 参数对ip进行过滤
                2.2.2 protocol：当前请求的协议类型
                2.2.3 domain： 当前请求域名
            """
            protocol = request.args.get('protocol')
            domain = request.args.get('domain')
            # print(protocol)
            # print(domain)
            # return '测试'
            proxy =self.mongo_pool.random_proxy(protocol=protocol,domain=domain,count=PROXIES_MAX_COUNT)
            if protocol:
                return '{}://{}:{}'.format(protocol,proxy.ip,proxy.port)
            else:
                return '{}:{}'.format(proxy.ip,proxy.port)

        @self.app.route('/proxies')
        def proxies():
            """
            http://localhost:16888/proxies?protocol=http&domain=jd.com

                2.3 实现根据协议类型和域名，提供获取多个高可用代理ip的服务
                2.3.1 可用通过 protocol 和 domain 参数对ip进行过滤
                2.3.2 实现给指定的i上追加上不可用域名的服务
            """
            # 获取协议：http/https
            protocol = request.args.get('protocol')
            # 域名：如：jd.com
            domain = request.args.get('domain')

            proxies = self.mongo_pool.get_proxies(protocol=protocol,domain=domain,count=PROXIES_MAX_COUNT)
            # proxies是一个Proxy对象的列表，但是Proxy对象不能进行json序列化，需要转换为字典列表
            # 转换为字典列表
            proxies = [proxy.__dict__ for proxy in proxies]
            # 返回json格式值串
            return json.dumps(proxies)

        @self.app.route('/disable_domain')
        def disable_domain():
            """
            http://localhost:16888/disable_domain?ip=183.88.226.50&domain=jd.com

            2.4 如果在获取ip的时候，有指定域名参数，将不在获取该ip，从而进一步提高代理ip的可用性
            """
            ip = request.args.get('ip')
            domain = request.args.get('domain')
            if ip is None:
                return '请提供ip参数'
            if domain is None:
                return '请提供domain参数'

            self.mongo_pool.disable_domain(ip, domain)
            return '{} 禁用域名 {}'.format(ip,domain)


    def run(self):
        # 3、 实现run方法，用于启动Flask的Web服务
        self.app.run('0.0.0.0',port=16888)

    @classmethod
    def start(cls):
        # 4、 实现start方法，用于通过类名，启动服务
        proxy_api = cls()
        proxy_api.run()


if __name__ == '__main__':
    # proxy_api = ProxyApi()
    # proxy_api.start()
    ProxyApi.start()

