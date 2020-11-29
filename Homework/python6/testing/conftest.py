from typing import List

import pytest

from python6.code.calculator import Calculator


@pytest.fixture(scope='module')
def get_calc():
    print("计算开始")
    calc = Calculator()
    yield calc
    print("计算结束")

def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    # items.reverse()
    print(type(items))
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')