import json

import requests


class BaseApi:
    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        corpid = 'ww485f3e5163864f5a'
        corpsecret = 'orTmGl1LvfG_7MNsnTDaH5MUAdy1rgiaiPz5hkaxVxI'
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {'corpid': corpid, 'corpsecret': corpsecret}
        }
        r = self.send(data)
        # print(json.dumps(r.json(), indent=2))
        # 断言可以加也可以不加，但是如要测获取token失败的情况，就不要加断言了，加了断言会在这里报错，后续的用例就不执行了？
        # 如果是说这里出错后面的用例就不需要再跑了,那么可以加断言
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
        print("token获取")
        token = r.json()['access_token']
        return token

    params = {}
    def send(self, data):
        """
        封装request方法
        :param kwargs:
        :return:
        """
        # request方法是get和post的底层方法，只要传入请求方式就可以了
        raw_data = json.dumps(data)
        for k, v in self.params.items():
            raw_data = raw_data.replace("${" + k + "}", v)
        print(raw_data)
        data = json.load(raw_data)
        r = requests.request(*data)
        print(json.dumps(r.json(), indent=2))
        return r