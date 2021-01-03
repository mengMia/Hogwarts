from mitmproxy import http


def request(flow: http.HTTPFlow):
    # 要修改的url请求是包含quote.json的
    if "quote.json" in flow.request.pretty_url:
        # 打开保存在本地的数据文件
        with open("C:/Users/LENOVO/tmp/stock.json", "rb") as f:
            # 创造一个response
            flow.response = http.HTTPResponse.make(
                200,
                # 读取文件中的数据作为返回内容 ,
                f.read(),
                # 指定返回数据类型，json的响应格式
                {"Content-Type": "application/json"}
            )