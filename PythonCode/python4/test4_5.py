# list_a = [1,2,3,4]
# list_a.append(0)
# print(list_a)

# """
# 列表生成式
# 生成一个平方列表，比如[1,4,9..]，使用for循环，和使用列表生成式
# """
# """
# 使用for循环
# """
# list_squre = []
# for i in range(1,4):
#     list_squre.append(i**2)
#
# print(list_squre)
#
# """
# 使用列表推导式
# """
# list_squre2 = [i**2 for i in range(1,4)]
# print("list_squre2", list_squre2)
#
# # 先执行for循环，然后是if判断，最后执行i**2
# list_squre3 = [i**2 for i in range(1,4) if i != 1]
# print(list_squre3)
#
# # 两层for嵌套循环
# list_squre4 = [i*j for i in range(1,4) for j in range(1,4)]
# print(list_squre4)


"""
元组
"""
# 定义
# tuple_a = (1,2,3)
# tuple_b = 1,2,3
# print(type(tuple_a))
# print(type(tuple_b))

# 不可变特性
# tuple_a = (1,2,3)
# tuple_a[0] = "a" #执行会报错

# a = [1,2,3]
# # 放入tuple里面的a相当于一个指针，修改a前后，a的内存地址没变
# tuple_b = (1,2,a);
# tuple_b[2][0] = "a";
# print(tuple_b)


# """
# 集合
# """
# a = {1,2,3}
# b = {1,4,5}
# print(a.difference(b))
# print(a.union(b))
# print(a.intersection(b))
# print(a.add("a"))
#
# # 列表推导式
# print({i for i in "addhfidhfihdjf"})  #打印出来的是去重的
#
# # 集合去重
# string = "loveyouforhdh"
# print(set(string))

"""
字典
"""

dict_a = {"a":1, "b":2}
dict_b = dict(a = 1, b = 2)
print("dict_a:", dict_a)
print("dict_b:", dict_b)

dict_a.keys()
dict_a.values()

dict_a.pop("a") #把key为a对应的键值对删除，并且返回a对应的value
dict_a.popitem() # 随机删除一个键值对，并且返回

a = {}
b = dict_a.fromkeys((1, 2, 3))
print(b) #{1:None, 2:None, 3:None}

a = {}
b = dict_a.fromkeys((1, 2, 3), "a")
print(b) #{1:a, 2:a, 3:a}

print({i: i * 2 for i in range(1, 3)})  #{1: 2, 2: 4}