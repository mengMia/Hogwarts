import pytest


def inc(x):
    return x + 1


# 参数化，生成多条测试用例
# 使用string
@pytest.mark.parametrize("a, b", [
    (1, 2),
    (10, 20),
    ('a', 'a1')
])

# 使用list
# @pytest.mark.parametrize(['a', 'b'], [
#     (1, 2),
#     (10, 20),
#     ('a', 'a1')
# ])

# # 使用tuple
# @pytest.mark.parametrize(('a', 'b'), [
#     (1, 2),
#     (10, 20),
#     ('a', 'a1')
# ])
def test_answer(a, b):
    assert inc(a) == b


def test_answer1():
    assert inc(4) == 5


@pytest.fixture()
def login():
    print("登录操作")
    username = 'Jerry'
    return username


class TestDemo:
    # 假设a需要登录，b不需要登录，c需要登录，可以使用pytest的fixture来解决这个问题
    def test_a(self, login):
        print(f"a username = {login}")

    def test_b(self):
        print("b")

    def test_c(self, login):
        print(f"c username = {login}")


if __name__ == '__main__':
    pytest.main(['test_5_6.py::TestDemo', '-v'])  # 使用python解释器要加上::TestDemo, -v参数加上日志打印
