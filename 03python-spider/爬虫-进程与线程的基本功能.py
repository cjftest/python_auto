# _*_ coding : UTF-8 _*_
# 开发团队 : 柴俊峰
# 开发人员 ：柴俊峰
# 开发时间 ：2020/12/10 23:04
# 文件名称 : 爬虫-进程与线程的基本功能.py
# 开发工具 ：PyCharm

import time,os,threading
from multiprocessing import Process
from threading import Thread



def work(n):
    print(f"给{n}打销售电话，进程号:{os.getpid()}，线程号：{threading.current_thread()}")
    time.sleep(3)
    print(f"销售电话结束：{n}，进程号:{os.getpid()}，线程号：{threading.current_thread()}")

userlist = ['刘德华','郭富城','梁朝伟']

# # 单进程与单线程
# for item in userlist:
#     work(item)

# def main():
#     # 多进程 类似于创建多个部门来完成这个工作
#     plist = []
#     for item in userlist:
#         # 循环创建进程
#         p = Process(target=work,args=(item,))
#         # 生成进程
#         p.start()
#         # 把创建的进程加入到列表中
#         plist.append(p)
#
#     # 阻塞终止进程的执行
#     [i.join() for i in plist]
#     # for i in plist:
#     #     i.join()


def main():
    # 多线程 类似于给这个部门增加人手
    plist = []
    for item in userlist:
        # 循环创建线程
        p = Thread(target=work,args=(item,))
        # 生成线程
        p.start()
        # 把创建的线程加入到列表中
        plist.append(p)

    # 阻塞终止线程的执行
    [i.join() for i in plist]
    # for i in plist:
    #     i.join()


if __name__ == '__main__':
    main()

