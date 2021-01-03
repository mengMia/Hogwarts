from mitmproxy import http
import json


def response(flow: http.HTTPFlow):
    # 加上过滤条件
    if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
        # 保存响应数据，并转换为python对象，固定模式
        data = json.loads(flow.response.content)
        # 对数据进行批量修改，自已定义一个方法
        data_new = json_travel(data, num=5)

        # 把修改后的内容赋值给response原始数据格式，固定模式
        flow.response.text = json.dumps(data_new)

# 响应数据里都有哪些数据类型：dict、list、string、num（int、float）
def json_travel(data, array=None, text=1, num=1):
    """
    完成对json数据的倍数操作
    :param data: 要修改的内容
    :param array: 列表的修改规则，为None默认不修改
    :param text: 字符串的修改规则，为1默认不修改
    :param num: 整数或者浮点数的修改规则，为1默认不修改
    :return: data_new
    """
    # 定义返回的数据
    data_new = None
    # 判断传入data的类型
    if isinstance(data, dict):
        # 把修改的数据定义为一个空字典
        data_new = dict()
        # 对传入的响应数据进行遍历：
        for k, v in data.items():
            # 每一个key所对应的value，也就是v传入的json_travel急需处理
            data_new[k] = json_travel(v, array, text, num)

    # 如果是列表，对列表的每一项进行遍历
    elif isinstance(data, list):
        data_new = list()

        for item in data:
            item_new = json_travel(item, array, text, num)
            # 如果传入的array为空，对列表的元素不做处理
            if array is None:
                data_new.append(item_new)
            else:
                # 判断传入的array修改规则，是否可以正常修改
                if isinstance(array, int) and array >= 0:
                    # 对每一个元素进行加倍修改
                    for i in range(array):
                        data_new.append(item_new)
                else:
                    data_new = data

    # 如果是字符串
    elif isinstance(data, str):
        # 如果text是正整数,要进行加倍操作
        if isinstance(text, int) and text >= 0:
            # 对字符串做加倍操作
            data_new = data * text
        else:
            data_new = data

    # 如果是int或者float这样的数字
    elif isinstance(data, int) or isinstance(data, float):
        # 对数字做乘积运算
        data_new = data * num

    # 其他数据类型保持原样
    else:
        data_new = data

    return data_new