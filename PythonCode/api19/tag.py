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

    def is_group_name_exist(self, group_name):
        """
        判断group_name是否已经存在
        :param group_name:
        :return:
        """
        for group in self.list().json()["tag_group"]:
            if group_name in group["group_name"]:
                return group["group_id"]
        # todo: 这里如果group_id是空，会和false重合，是编程语言上的问题，所以这里不能用false，应该抛出异常
        # print("group name not in group")
        # return False
        return ""

    def add(self, group_name, tag, **kwargs):
        """
        添加标签
        :param group_name:
        :param tag:
        :return:
        """
        data = {
                "group_name": group_name,
                "tag": tag,
                **kwargs
                }
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
                          params={"access_token": self.token},
                          json={
                                "group_name": group_name,
                                "tag": tag,
                                **kwargs
                            }
                          )
        print(json.dumps(r.json(), indent=2))
        return r

    def add_and_detect(self, group_name, tag, **kwargs):
        """
        解决添加标签的时候标签重复导致执行失败的问题, 数据清理
        :param group_name:
        :param tag:
        :param kwargs:
        :return:
        """
        r = self.add(group_name, tag, **kwargs)
        # 如果请求状态码正常，接口的错误码是40071，说明已经有group_name存在，要先检验是不是真的存在于现有的tag列表中，检验方法里返回了group_id，然后再删掉这个group_id
        if r.json()["errcode"] == 40071:
            group_id = self.is_group_name_exist(group_name)
            if not group_id:
                # 这个返回说明是接口有问题
                return False
            self.delete_group(group_id)
            self.add(group_name, tag, **kwargs)
        result = self.is_group_name_exist(group_name)
        if not result:
            print("add not success")
        return result

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

    def delete_group(self, group_id):
        """
        根据group_id删除标签
        :param group_id:
        :return:
        """
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
                          params={"access_token": self.token},
                          json={
                              "group_id": group_id
                          })
        print(json.dumps(r.json(), indent=2))
        return r

    def delete_tag(self, tag_id):
        """
        根据tag_id删除标签
        :param tag_id:
        :return:
        """
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
                          params={"access_token": self.token},
                          json={
                              "tag_id": tag_id,
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