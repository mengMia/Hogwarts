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

    # 构造post的form请求，参数应为data
    def test_post_form(self):
        payload = {
            "level": 1,
            "name": "ET"
        }
        r = requests.post('http://httpbin.testing-studio.com/post', data=payload)
        print(r.text)
        assert r.status_code == 200

