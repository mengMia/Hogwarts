import pytest

"""
fixture的用法
"""

# @pytest.mark.usefixtures("login")
def test_case1(login):
    print(login)
    print("用例1")

def test_case2():
    print("用例2")

def test_case3(conn_db):
    print(conn_db)
    print("用例3")