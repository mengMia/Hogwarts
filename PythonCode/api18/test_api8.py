import requests
from requests.auth import HTTPBasicAuth


class TestAuth:
    def test_auth(self):
        r = requests.get(url="http://httpbin.testing-studio.com/basic-auth/hogw/123",
                     auth = HTTPBasicAuth("hogw", "123"))
        print(r.text)