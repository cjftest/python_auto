# _*_ coding : UTF-8 _*_
# 开发团队 : 柴俊峰
# 开发人员 ：柴俊峰
# 开发时间 ：2020/12/15 23:12
# 文件名称 : 爬虫-线程池与进程池.py
# 开发工具 ：PyCharm


import time
import os
import threading
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
from queue import Queue


def work(n):
    print(f"给{n}打销售电话，进程号:{os.getpid()}，线程号：{threading.current_thread()}")
    time.sleep(3)
    print(f"销售电话结束：{n}，进程号:{os.getpid()}，线程号：{threading.current_thread()}")
    print("\n")

def main():
    userlist = ['刘德华', '郭富城', '梁朝伟', '周星驰', '吴孟达']

    # 1、创建线程池
    pool = ThreadPoolExecutor(max_workers=3)

    # 1、创建进程池
    # pool = ProcessPoolExecutor(max_workers=3)

    # 2、循环指派任务
    [pool.submit(work,user) for user in userlist]

    # 3、关闭线程池/进程池
    pool.shutdown()


if __name__ == '__main__':
    main()

