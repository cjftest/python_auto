# _*_ coding : UTF-8 _*_
# 开发团队 : 柴俊峰
# 开发人员 ：柴俊峰
# 开发时间 ：2021/1/12 23:39
# 文件名称 : settings.py
# 开发工具 ：PyCharm


# 在配置文件，setting.py中，定义MAX_SCORE = 50，表示代理ip默认的最高分数
MAX_SCORE = 50

# 日志的配置信息
import logging
# 默认的配置
LOG_LEVEL = logging.INFO    #默认等级
LOG_FMT = '%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s: %(message)s'
LOG_DATEFMT = '%Y-%m-%d %H:%M:%S'   #默认时间格式
LOG_FILENAME = 'log.log'    # 默认日志文件名称

# 设置代理IP的超时时间
TEST_TIMEOUT = 5

# MongoDB数据库的url
MONGO_URL = 'mongodb://127.0.0.1:27017'


PROXIES_SPIDERS = [
    # 爬虫的全类名，路径： 模块.类名
    # 'core.proxy_spider.proxy_spiders.JiangxianliSpider',
    'core.proxy_spider.proxy_spiders.ProxylistplusSpider',
    'core.proxy_spider.proxy_spiders.Ip66Spider',
    'core.proxy_spider.proxy_spiders.Ip3366Spider',
    'core.proxy_spider.proxy_spiders.KuaidailiSpider',


]

# 4.3.1 修改配置文件，增加爬虫运行时间间隔的配置，单位为小时
RUN_SPIDERS_INTERVAL = 12

# 配置检测代理ip的异步数量
TEST_PROXIES_ASYNC_COUNT = 10

# 配置检查代理ip的时间间隔，单位是小时
TEST_PROXIES_INTERVAL = 2

# 配置获取的代理ip最大数量，这个越小可用性就越高，但随机性就越差
PROXIES_MAX_COUNT = 50