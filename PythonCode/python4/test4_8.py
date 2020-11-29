# def div(a, b):
#     return a / b
#
#
# f = open("data.txt")
# try:
#     print(div(1, 1))
#     list1 = [1, 2, 3]
#     print(list1[3])
#     f.readlines()
#     # f.close() 此时由于前面的异常，导致close方法无法执行，可通过finally来解决
#
# except Exception as e:
#     print(e)
#     print("这里有个异常")
# else:
#     print("没有异常")  # 没有异常的时候要执行的语句
# finally:  # 最终都会被执行，无论是否有异常产生
#     print("finally")
#     f.close()

"""
手动抛出异常
"""


def set_age(num):
    if num <= 0 or num > 200:
        raise ValueError(f"值错误：{num}")
    else:
        print(f"设置的年龄为：{num}")


set_age(-1)
