import pytest
import time


@pytest.mark.run(order=2)
def test_case1(login):
    print(login)
    print("用例1")

@pytest.mark.parametrize('a', [1, 2, 3])
@pytest.mark.run(order=1)
def test_case2(a):
    # time.sleep(2)
    assert False
    print("用例2")




