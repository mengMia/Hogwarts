import pytest

from Homework.python6.code.calculator import Calculator


class TestCalc:
    def setup_class(self):
        print("计算开始")
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    # 加法
    @pytest.mark.parametrize('a, b, expect', [
        [1, 3, 4], [0.1, 0.99, 1.09], [0, 0, 0],
        [100000000000000, 100000000000000, 200000000000000],
        [-3, -2, -5]
    ])
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        assert result == expect

    @pytest.mark.parametrize('a, b, expect', [
        [0.1, 0.1, 0.2], [0.1, 0.2, 0.3]
    ])
    def test_add_float(self, a, b, expect):
        result = self.calc.add(a, b)
        assert round(result, 2) == expect

    # 除法
    @pytest.mark.parametrize('a, b, expect', [
        [10, 5, 2]
    ])
    def test_div_int(self, a, b, expect):
        result = self.calc.div(a, b)
        assert result == expect

    # 除数为0的测试用例分开写
    @pytest.mark.parametrize('a, b', [
        [0.1, 0], [10, 0], [-2, 0]
    ])
    def test_div_zero(self, a, b):
        with pytest.raises(ZeroDivisionError):
            self.calc.div(a, b)

    # 浮点数的测试用例分开写
    @pytest.mark.parametrize('a, b, expect', [
        [10, 3, 3.3], [2, 5, 0.4], [1, 3, 0.3]
    ])
    def test_div_float(self, a, b, expect):
        result = self.calc.div(a, b)
        assert round(result, 1) == expect

