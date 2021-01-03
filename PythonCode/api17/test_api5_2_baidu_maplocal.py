from mitmproxy import http


def request(flow: http.HTTPFlow):
    # 发起请求后，数据包传到这个方法里，判断url是不是我们预期的url
    # 注意这里的url是：https://www.baidu.com/，不是https://www.baidu.com
    if flow.request.pretty_url == "https://www.baidu.com/":
        # 创造一个response
        flow.response = http.HTTPResponse.make(
            200,
            b"Hello World",
            {"Content-Type": "text/html"}
        )