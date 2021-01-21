import json

from hamcrest import *
from jsonpath import jsonpath
import requests

class TestDemo:
    def test_get(self):
        r = requests.get('http://httpbin.testing-studio.com/get', auth=('user', 'pass'))
        print(r)
        print(r.json())
        assert r.status_code == 200

    # 构造get query请求
    def test_query(self):
        payload={
            "level":1,
            "name": "ET"
        }
        r = requests.get('http://httpbin.testing-studio.com/get', params=payload)
        print(r.text)
        assert r.status_code == 200

    # 构造post的form请求，参数应为data,是以form表单的形式发送出去
    def test_post_form(self):
        payload = {
            "level": 1,
            "name": "ET"
        }
        r = requests.post('http://httpbin.testing-studio.com/post',
                          # data={
                          #     "level": 1,
                          #     "name": "ET"
                          # }
                          data=payload)
        print(r.text)
        assert r.status_code == 200

    # 构造请求的header
    def test_header(self):
        r = requests.get('http://httpbin.testing-studio.com/get', headers={"h": "header demo"})
        print(r.text)
        assert r.status_code == 200
        assert r.json()["headers"]["H"] == "header demo"

    # 构造json请求，发送json参数，实际上是以data形式发送的，可以看到这个响应结果里面的data是json格式，而且header部分的content-type是application/json
    def test_post_json(self):
        payload = {
            "level": 1,
            "name": "ET"
        }
        r = requests.post('http://httpbin.testing-studio.com/post', json=payload)
        print(r.text)
        assert r.status_code == 200
        assert r.json()['json']['level']==1

    def test_hogwarts_json(self):
        r = requests.get('https://ceshiren.com/categories.json')
        print(r.text)
        assert r.status_code == 200
        assert r.json()['category_list']['categories'][0]['name'] == "开源项目"
        print(jsonpath(r.json(), '$..name'))
        # 取所有name中的第一个
        assert jsonpath(r.json(), '$..name')[0] == "开源项目"

    def test_hamcrest(self):
        r = requests.get('https://ceshiren.com/categories.json')
        print(r.text)
        assert r.status_code == 200
        assert_that(r.json()['category_list']['categories'][0]['name'], equal_to("开源项目"))
        print(jsonpath(r.json(), '$..name'))
        # 取所有name中的第一个
        assert jsonpath(r.json(), '$..name')[0] == "开源项目"


