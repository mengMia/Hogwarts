import requests


class TestCookie():
    # 通过请求头信息传递cookie
    def test_header_cookie(self):
        url = "http://httpbin.testing-studio.com/cookies"
        header = {"Cookie": "hogwarts=school"}
        r = requests.get(url=url, headers=header)
        print(r.request.headers)

    # 通过cookies参数传递cookie
    def test_cookies_cookie(self):
        url = "http://httpbin.testing-studio.com/cookies"
        header = {"User-agent": "hogwarts"}
        cookie_data = {
            "hogwarts":"ET",
            "teacher": "feier"
        }
        r = requests.get(url=url, headers=header, cookies=cookie_data)
        print(r.request.headers)
