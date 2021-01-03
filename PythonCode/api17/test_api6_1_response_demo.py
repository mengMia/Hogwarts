from mitmproxy import http


def response(flow: http.HTTPFlow):
    # 打印响应数据
    print(flow.response)
    # 打印content
    print(flow.response.content)