# import os
#
# print(os.path.exists("b"))
# if not os.path.exists("b"):
#     os.mkdir("b")
# if not os.path.exists("b/test.txt"):
#     f = open("b/test.txt", "w")
#     f.write("hello, os using")
#     f.close()

# import time
#
# # print(time.asctime())
# # print(time.time())
# # print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
#
# # 获取两天前的时间
# now_timestamp = time.time()
# two_day_before = now_timestamp - 60*60*24*2
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(two_day_before)))
import urllib.request

response = urllib.request.urlopen('https://www.baidu.com')
print(response.status)
print(response.read())