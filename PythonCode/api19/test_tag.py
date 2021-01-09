import datetime
import json

import pytest
import requests
# 如果是import jsonpath，会报错，module not callable
from jsonpath import jsonpath

from PythonCode.api19.tag import Tag


class TestTag():
    def setup_class(self):
        self.tag = Tag()

    @pytest.mark.parametrize("tag_id, tag_name", [
        ['etb90BDQAAf5dmQpHyNg_Ijtk-Q0QD4A', 'tag1_new_'],
        ['etb90BDQAAf5dmQpHyNg_Ijtk-Q0QD4A', 'tag1_中文'],
        ['etb90BDQAAf5dmQpHyNg_Ijtk-Q0QD4A', 'tag1  空格'],
    ])
    def test_tag_list(self, tag_id, tag_name):
        tag_name = tag_name + str(datetime.datetime.now().strftime("%Y%m%d-%H%M"))
        r_list = self.tag.list()
        r_update = self.tag.update(
            id=tag_id,
            tag_name = tag_name
        )
        r = self.tag.list()
        # 断言
        # tags = [
        #     tag
        #     for group in r.json()['tag_group'] if group['group_name'] == group_name
        #     for tag in group['tag'] if tag['name'] == tag_name
        # ]
        assert jsonpath(r.json(), f"$..[?(@.name=='{tag_name}')]")[0]['name'] == tag_name

    @pytest.mark.parametrize("group_name, tag_name, order",[
        ["标签组1", "标签名1", "1"],
        ["tag_group2", "tag_name2", "2"],
    ])
    def test_tag_add(self, group_name, tag_name, order):
        tag = [{"name": tag_name, "order": order}]
        r = self.tag.add(
            group_name=group_name,
            tag=tag
        )
        r = self.tag.list()
        assert jsonpath(r.json(), f"$..[?(@.name=='{tag_name}')]")[0]['name'] == tag_name

    @pytest.mark.parametrize('group_name',[
        "python15"
    ])
    def test_tag_delete(self, group_name):
        tag_id = self.tag.get_tag_id(group_name)
        tag_id = tag_id[0]
        r = self.tag.delete(tag_id, group_id=None)
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

    def test_get_tag_id(self):
        r = self.tag.get_tag_id(group_name="python15")
        print(r)




