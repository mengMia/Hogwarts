# name = "hogwarts"
# age = 20
# print('my name is {0}, age is {1}, {0}{1}{1}'.format(name, age))
#
# list1 = [1, 3, 4]
# dict1 = {'name': 'tom', 'gender': 'male'}
# print('my list is {}, dict is {}'.format(list1, dict1))
#
# namelist = ['lili', 'tom', 'jerry']
# print('we name : {} 、{} and {}'.format(namelist[0], namelist[1], namelist[2]))
# print('we name : {} 、{} and {}'.format(*namelist))  # 解包
#
# print('name is {name}, gender is {gender}'.format(**dict1))

# name = "hogwarts"
# age = 20
#
# list1 = [1, 3, 4]
# dict1 = {'name1': 'tom', 'gender': 'male'}
# print(f"my name is {name}, age is {age}, my list is {list1[0]}, dict is {dict1['name1']}")
# # print(f'my name is {name}, age is {age}, my list is {list1[0]}, dict is {dict1['name1']}')  # 这里使用单引号会报错，因为name1用了单引号
# print(f'result is {(lambda x : x + 1)(2)}')

# """
# 文件读取
# """
# f = open('data.txt')
# print(f.readable())
# print(f.readlines())
# f.close()
#
# # with是当执行完语句之后自动关闭掉这个文件，不需要close
# # 图片的读取需要使用rb的模式，读取二进制
# # 正常的文本使用默认的即可，不需要额外指定mode
# with open('data.txt', 'rb') as f:
#     print(f.readlines())
import json

data = {
    "name": ["henry", 'nickname'],
    "age": 26,
    "gender": "female"
}
print(type(data))
data1 = json.dumps(data)
print(data1)
print(type(data1))

data2 = json.loads(data1)
print(type(data2))


