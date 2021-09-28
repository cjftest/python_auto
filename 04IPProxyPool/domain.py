# _*_ coding : UTF-8 _*_
# 开发团队 : 柴俊峰
# 开发人员 ：柴俊峰
# 开发时间 ：2021/1/12 23:37
# 文件名称 : domain.py
# 开发工具 ：PyCharm

from settings import MAX_SCORE
import sys
import logging

class Proxy(object):
    def __init__(self,ip,port,protocol=-1,nick_type=-1,speed=-1,area=None,score=MAX_SCORE,disable_domains=[]):
        # ip：代理的ip地址
        self.ip = ip
        # port ：代理ip的端口号
        self.port = port
        # protocol 代理ip支持的协议类型，http是0，https是1，http和https都支持是2
        self.protocol = protocol
        # nick_type 代理ip的匿名程度，高匿：0，匿名：1，透明：2，
        self.nick_type = nick_type
        # speed 代理ip的响应速度，单位：s
        self.speed = speed
        # area 代理ip所在的地区
        self.area = area
        # score 代理ip的评分，用于衡量代理ip的可用性
        # 默认分值可以通过配置文件进行配置，在进行代理可用性检查的时候，每遇到一次请求失败就减1分，减到0的时候从池中删除，如果检查代理可用，就恢复默认分值
        self.score = score
        # 不可用域名列表，有些代理ip在某些域名不可用，但是在其他域名下可用
        self.disable_domains = disable_domains

    # 提供 __str__方法，返回数据字符串
    def __str__(self):
        return str(self.__dict__)