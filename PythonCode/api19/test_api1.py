import json

import requests


class TestTag():
    # 先用普通的测试用例把用例调通，然后再去封装
    def test_tag_list_test(self):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list?access_token=ACCESS_TOKEN',
            # data的这种格式看起来是个json，但在python里只是个字典，要结构化，使用json参数，如下
            data='''
        {
        "tag_id": [
            "etXXXXXXXXXX",
            "etYYYYYYYYYY"
            ]
        }
        '''
            )
        print(json.dumps(r.json(), indent=2))
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

    # 改进后的，结构化的测试用例
    def test_tag_list(self):
        corpid = 'ww485f3e5163864f5a'
        corpsecret = 'orTmGl1LvfG_7MNsnTDaH5MUAdy1rgiaiPz5hkaxVxI'
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                         params={'corpid': corpid, 'corpsecret': corpsecret})
        print(json.dumps(r.json(), indent=2))
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
        token = r.json()['access_token']

        r = requests.post(
            # post请求带参数的话，放在params里
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list?',
            params={"access_token": token},
            # data要结构化，结构化的数据利于维护,这里用json参数，会自动转换为字符串类型的json内容，
            json={
                "tag_id":[]
            }
        )
        print(json.dumps(r.json(), indent=2))
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
