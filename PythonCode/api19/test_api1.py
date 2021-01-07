import datetime
import json

import jsonpath
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
    # 存在的问题
    # todo:与底层具体的实现框架代码耦合严重，比如公司换了协议，比如使用pb
    # todo:代码冗余，需要封装，编辑标签的代码里又获取了一次所有的标签
    # todo：无法清晰的描述业务
    # todo：使用jsonpath表达更灵活的递归查找，层次比较深的时候适合jsonpath，但是数据量比较大的时候用这个会比较慢
    def test_tag_list(self):
        corpid = 'ww485f3e5163864f5a'
        corpsecret = 'orTmGl1LvfG_7MNsnTDaH5MUAdy1rgiaiPz5hkaxVxI'
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                         params={'corpid': corpid, 'corpsecret': corpsecret})
        print(json.dumps(r.json(), indent=2))
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
        token = r.json()['access_token']

        #获取标签列表
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


        # 编辑标签
        # tag_name = 'tag1_new' + str(datetime.datetime.now().time())
        tag_name = 'tag1_new' + str(datetime.datetime.now().strftime("%Y%m%d-%H%M"))
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag",
                          params={"access_token" : token},
                          json={
                              "id": 'etb90BDQAAf5dmQpHyNg_Ijtk-Q0QD4A',
                              "name": tag_name
                          })
        print(json.dumps(r.json(), indent=2))

        # for group in r.json()['tag_group']:
        #     if group['group_name']=='python15':
        #         for tag in group['tag']:
        #             if tag['name']=='tag1_new':
        #                 assert True  这样写，断言可能走不到最后，会有问题

        # 重新获取标签列表，用于断言
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
            params={"access_token": token},
            json={
                'tag_id': []
            }
        )
        print(json.dumps(r.json(), indent=2))
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

        # 断言
        tags = [
            tag
            for group in r.json()['tag_group'] if group['group_name'] == 'python15'
            for tag in group['tag'] if tag['name'] == tag_name
        ]
        assert tags != []

        # 使用jsonpath，性能会比较差，如果json结构比较简单，可以使用jsonpath，还有jmepath
        # jsonpath(f"$..[?(@.name='{tag_name}')]")  这个好像不对