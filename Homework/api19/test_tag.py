import datetime
import json

import pytest
from jsonpath import jsonpath

from PythonCode.api19.tag import Tag


class TestTag():
    def setup_class(self):
        self.tag = Tag()

    def test_tag_list(self):
        """
        获取标签列表的测试用例
        :return:
        """
        r_list = self.tag.list()
        # print(json.dumps(r_list.json(), indent=2))

    @pytest.mark.parametrize("tag_id, tag_name", [
        ['etb90BDQAADvLPTkJV6PQz8OV4RV7o7w', 'tag1_new_'],
        ['etb90BDQAAbJlk41UQh52U9JA4CAGrQQ', 'tag1_中文_'],
    ])
    def test_tag_update(self, tag_id, tag_name):
        tag_name = tag_name + str(datetime.datetime.now().strftime("%Y%m%d-%H%M"))
        # print("第一次调用获取list")
        # r_list = self.tag.list()
        print("调用update方法")
        r_update = self.tag.update(
            id=tag_id,
            tag_name=tag_name
        )
        print("第一次调用获取list")
        r = self.tag.list()
        # 断言
        # tags = [
        #     tag
        #     for group in r.json()['tag_group'] if group['group_name'] == group_name
        #     for tag in group['tag'] if tag['name'] == tag_name
        # ]
        assert jsonpath(r.json(), f"$..[?(@.name=='{tag_name}')]")[0]['name'] == tag_name

    @pytest.mark.parametrize("group_name, tag_name, order",[
        ["标签组11", "标签名1", "1"],
        ["tag_group21", "tag_name2", "2"],
    ])
    def test_tag_add(self, group_name, tag_name, order):
        tag = [{"name": tag_name, "order": order}]
        # self.tag.add方法里面的tag是一个列表，
        r = self.tag.add(
            group_name=group_name,
            tag=tag
        )
        assert r.status_code == 200
        assert r.json()["errcode"] == 0
        # r = self.tag.list()
        # assert jsonpath(r.json(), f"$..[?(@.name=='{tag_name}')]")[0]['name'] == tag_name

    # add方法的更优版本
    @pytest.mark.parametrize("group_name, tag_name, order", [
        ["标签组1", "标签名1", "1"],
        ["tag_group2", "tag_name2", "2"],
        ["python15", "tag_name1", "1"],
        ["python15", "tag_name2", "2"],
    ])
    def test_add_and_detect(self, group_name, tag_name, order):
        tag = [{"name": tag_name, "order": order}]
        result = self.tag.add_and_detect(group_name, tag)
        print(result)
        assert result

    # @pytest.mark.parametrize('group_name',[
    #     "python15"
    # ])
    def test_tag_delete_group(self):
        group_ids = ["etb90BDQAAjenj9E2f5QrjFmkqQmAmdQ"]
        r = self.tag.delete_group(group_ids)
        assert r.json()["errcode"] == 0

    # @pytest.mark.parametrize('group_name', [
    #     "python15"
    # ])
    def test_tag_delete_tag(self):
        # tag_id = self.tag.get_tag_id(group_name)
        # tag_id = tag_id[0]
        tag_ids = ["etb90BDQAAZZ6-MRo7b0IT80tfjCPvjg"]
        r = self.tag.delete_tag(tag_ids)
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
    # def test_get_tag_id(self):
    #     r = self.tag.get_tag_id(group_name="python15")
    #     print(r)

    def test_tag_delete_and_detect_group(self):
        r = self.tag.delete_and_detect_group(["etb90BDQAAjpPhhAxDDdwy1twGX36X3g"])
        assert r.json()["errcode"] == 0




