import datetime
import json

import requests


class Tag:
    # 1.token可以放到类里面定义,当token修改的时候变成对类的修改？？？
    # token=None
    # 2.token可以放在init方法里，创建对象的时候就初始化好，只需要在初始化的时候获取一次就可以，在test_tag里获取token，只需要实例化这个类就可以获取到token：tag=Tag()
    def __init__(self):
        self.token=self.get_token()

    # 获取token理论上来说不应该放在这个地方，应该放在一个公共的地方
    def get_token(self):
        corpid = 'ww485f3e5163864f5a'
        corpsecret = 'orTmGl1LvfG_7MNsnTDaH5MUAdy1rgiaiPz5hkaxVxI'
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                         params={'corpid': corpid, 'corpsecret': corpsecret})
        print(json.dumps(r.json(), indent=2))
        # 断言可以加也可以不加，但是如要测获取token失败的情况，就不要加断言了，加了断言会在这里报错，后续的用例就不执行了？
        # 如果是说这里出错后面的用例就不需要再跑了,那么可以加断言
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
        token = r.json()['access_token']
        return token


    def add(self, group_name, tag):
        """
        添加标签
        :param group_name:
        :param tag:
        :return:
        """
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
                          params={"access_token": self.token},
                          json={
                                "group_name": group_name,
                                "tag": tag
                            }
                          )
        print(json.dumps(r.json(), indent=2))
        return r

    def list(self):
        """
        获取标签列表
        :return: 列表r
        """
        r = requests.post(
            # post请求带参数的话，放在params里
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list?',
            params={"access_token": self.token},
            json={
                "tag_id": []
            }
        )
        print(json.dumps(r.json(), indent=2))
        # list也要测试某个查询失败的情况，所以去掉断言
        # assert r.status_code == 200
        # assert r.json()['errcode'] == 0
        return r

    def update(self, id, tag_name):
        """
        编辑标签
        :return:编辑标签接口的响应json数据
        """
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag",
                          params={"access_token": self.token},
                          json={
                              "id": id,
                              "name": tag_name
                          })
        print(json.dumps(r.json(), indent=2))
        return r

    def delete(self, tag_id, group_id):
        """
        删除标签
        :param tag_id:
        :param group_id:
        :return:
        """

        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
                          params={"access_token": self.token},
                          json={
                              "tag_id": tag_id,
                              "group_id": group_id
                          })
        print(json.dumps(r.json(), indent=2))
        return r

    def get_tag_id(self, group_name):
        """
        获取tag_id
        :return:
        """
        r=self.list()
        tag_group = r.json()['tag_group']
        tag_id = []
        for group in tag_group:
            if group['group_name'] == group_name:
                tag = group['tag']
                for tag_ele in tag:
                    tag_id.append(tag_ele['id'])
                return tag_id