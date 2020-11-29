from typing import List

import pytest


@pytest.fixture(scope="module", params=['tom', 'jerry'])
def login(request):
    print("登录操作")
    username = request.param  # 用来接收传入的参数
    yield username  #yield前面的操作相当于setup，后面的操作相当于teardown,yeild相当于return
    print("登出操作")


@pytest.fixture
def conn_db():
    print("完成数据库连接")
    return "database"

def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    # items.reverse()
    print(type(items))
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

        # 自己给测试用例加上标签，通过命令行的方式运行该标签的用例
        # pytest test6_6.py -m case1 -vs
        if 'test_case1' in item._nodeid:
            item.add_marker(pytest.mark.case1)