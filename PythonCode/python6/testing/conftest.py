from typing import List

import pytest


@pytest.fixture(scope="function", params=['tom', 'jerry'])
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
    items.reverse()
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')