import datetime
import json

import requests
import yaml

from PythonCode.api19.base_api import BaseApi


class Tag(BaseApi):
    def __init__(self):
        """
        继承父类的init方法，获取token
        """
        # super().__init__()
        self.params["token"] = self.token

    def find_group_id_by_name(self, group_name):
        """
        判断group_name是否已经存在
        :param group_name:
        :return:
        """
        for group in self.list().json()["tag_group"]:
            if group_name in group["group_name"]:
                return group["group_id"]
        print("group name not in goup")
        return ""

    def is_group_id_exist(self, group_id):
        """
        判断group_id是否已经存在
        :param group_id:
        :return:
        """
        for group in self.list().json()["tag_group"]:
            if group_id in group["group_id"]:
                print("这个是is_group_id_exist方法，return true")
                return True
        print("这个是is_group_id_exist方法，return false")
        return False

    def add(self, group_name, tag, **kwargs):
        """
        添加标签
        :param group_name:
        :param tag:
        :return:
        """
        data = {
                "method": "post",
                "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
                "params":{"access_token": self.token},
                "json":{
                        "group_name": group_name,
                        "tag": tag,
                        **kwargs
                        }
                }
        r = self.send(data)
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
            group_id = self.find_group_id_by_name(group_name)
            if not group_id:
                # 这个返回说明是接口有问题
                return ""
            self.delete_group([group_id])
            self.add(group_name, tag, **kwargs)
        result = self.find_group_id_by_name(group_name)
        if not result:
            print("add not success")
        return result

    def list(self):
        """
        获取标签列表
        :return: 列表r
        """
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list?",
            "params": {"access_token": self.token},
            "json":{
                "tag_id": []
            }
        }
        r = self.send(data)
        return r

    def update(self, id, tag_name):
        """
        编辑标签
        :return:编辑标签接口的响应json数据
        """
        # data = {
        #     "method": "post",
        #     "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag",
        #     "params": {"access_token": self.token},
        #     "json": {
        #         "id": id,
        #         "name": tag_name
        #         }
        # }
        self.params["id"] = id
        self.params["tag_name"] = tag_name
        with open("../api19/tag.yaml", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        print(data)
        r = self.send(data["update"])
        return r

    def delete_group(self, group_id):
        """
        根据group_id删除标签
        :param group_id:
        :return:
        """
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            "params": {"access_token": self.token},
            "json": {
                "group_id": group_id
            }
        }
        r = self.send(data)
        return r

    def delete_tag(self, tag_id):
        """
        根据tag_id删除标签
        :param tag_id:
        :return:
        """
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            "params": {"access_token": self.token},
            "json": {
                "tag_id": tag_id,
            }
        }
        r = self.send(data)
        return r

    def delete_and_detect_group(self, group_ids):
        delete_group_ids = []
        print("第一次调用delete_group方法")
        r = self.delete_group(group_ids)
        # 40068说明这个group id不存在或者不合法，要检测是否真的不存在
        if r.json()["errcode"] == 40068:
            for group_id in group_ids:
                if not self.is_group_id_exist(group_id):
                    group_id_tmp = self.add_and_detect("123", [{"name": "标签123"}])
                    delete_group_ids.append(group_id_tmp)
                else:
                    delete_group_ids.append(group_id)
            print("第二次调用delete_group方法")
            r = self.delete_group(delete_group_ids)
        print("删除成功")
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