import requests

class TestDemo:
    def test_get(self):
        r = requests.get('http://httpbin.testing-studio.com/get', auth=('user', 'pass'))
        print(r)
        print(r.json())
        assert r.status_code == 200