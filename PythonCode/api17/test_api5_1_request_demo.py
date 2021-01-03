# request方法名是不能修改的
# 当mitmdump加载脚本的时候，有请求来的时候就会加载request方法
from mitmproxy import http


def request(flow: http.HTTPFlow):
    # 增加请求的头信息中的字段
    flow.request.headers["myheader"] = "ET"
    print(flow.request.headers)