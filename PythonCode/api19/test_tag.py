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
        # 用jsonpath断言，就不需要用这个group了
        # group_name = "python15"
        tag_name = tag_name + str(datetime.datetime.now().strftime("%Y%m%d-%H%M"))
        # 获取token没有必要每次执行方法的时候都重新获取一次，所以将其放到setup_class里
        # tag = Tag()
        r_list = self.tag.list()
        r_update = self.tag.update(
            id=tag_id,
            tag_name = tag_name
        )
        # 获取修改之后的标签列表
        r = self.tag.list()
        # 断言
        # tags = [
        #     tag
        #     for group in r.json()['tag_group'] if group['group_name'] == group_name
        #     for tag in group['tag'] if tag['name'] == tag_name
        # ]
        # assert tags != []
        # 这个表达式不正确
        # assert jsonpath(r.json(), f"$..[?(@.name='{tag_name}')]") is not None
        assert jsonpath(r.json(), f"$..[?(@.name=='{tag_name}')]")[0]['name'] == tag_name

    # 专门写一个会执行失败的测试用例，测试特殊字符之类的
    # def test_tag_list(self, tag_id, tag_name):
    #     pass