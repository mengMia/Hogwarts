from mitmproxy import http
import json

def response(flow: http.HTTPFlow):
    # 加上过滤条件
    if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
        # 保存响应数据，并转换为python对象
        # 用json.load会报错，因为该方法是加在文件的，需要使用json.loads
        # data = json.load(flow.response.content)
        # File"D:\tools\Python38\lib\json\__init__.py", line
        # 293, in load return loads(fp.read(),AttributeError: 'bytes'
        # object has no attribute 'read'

        data = json.loads(flow.response.content)
        # 修改第一支股票的名称
        # data['data']['items'][0]['quote']['name'] = "爱尔霍格沃兹"
        data['data']['items'][1]['quote']['name'] *= 2
        data['data']['items'][2]['quote']['name'] = ""



        # 把修改后的内容赋值给response原始数据格式
        # text是一个二进制的数据格式，content是字符串格式
        flow.response.text = json.dumps(data)