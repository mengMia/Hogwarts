import _thread
import logging
import selenium
from time import sleep, ctime

logging.basicConfig(level=logging.INFO)


# def loop0():
#     logging.info("start loop0 at " + ctime())
#     sleep(4)
#     logging.info("end loop0 at " + ctime())
#
#
# def loop1():
#     logging.info("start loop1 at " + ctime())
#     sleep(2)
#     logging.info("end loop1 at " + ctime())
#
# # 主线程
# def main():
#     logging.info("start all at " + ctime())
#     _thread.start_new_thread(loop0, ())
#     _thread.start_new_thread(loop1, ())
#     sleep(6)  # 加6秒的原因是：主线程如果结束了，其他线程都会被kill，所以要让主线程等6s，
#     logging.info("end all at " + ctime())
#
#
# if __name__ == '__main__':
#     main()


"""
通过锁的操作，让主线程等待其他线程结束之后（执行完解锁）再结束
"""

