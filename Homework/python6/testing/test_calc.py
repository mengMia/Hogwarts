import allure
import pytest
import yaml

from Homework.python6.code.calculator import Calculator


# 解析测试数据
def get_data():
    with open('data/calc.yml', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return data


class TestCalc:
    # """
    # 使用fixture来将方法配置为setup方法  将该方法放在conftest文件中也可
    # """
    # @pytest.fixture
    # def get_calc(self):
    #     print("开始计算")
    #     calc = Calculator()
    #     yield calc
    #     print("计算结束")

    # 加法
    @allure.story("加法")
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('a, b, expect', get_data()['ADD']['datas'], ids=get_data()['ADD']['ids'])
    def test_add(self, get_calc, a, b, expect):
        # result = self.calc.add(a, b)
        result = get_calc.add(a, b)
        assert result == expect

    # 浮点数的加法
    @allure.story("浮点数的加法")
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('a, b, expect', get_data()['ADD_float']['datas'], ids=get_data()['ADD_float']['ids'])
    def test_add_float(self, get_calc, a, b, expect):
        # result = self.calc.add(a, b)
        result = get_calc.add(a, b)
        assert round(result, 2) == expect

    # int除法
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('a, b, expect', get_data()['DIV_int']['datas'], ids=get_data()['DIV_int']['ids'])
    def test_div_int(self, get_calc, a, b, expect):
        result = get_calc.div(a, b)
        assert result == expect

    # 除数为0的测试用例分开写
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('a, b', get_data()['DIV_zero']['datas'], ids=get_data()['DIV_zero']['ids'])
    def test_div_zero(self, get_calc, a, b):
        with pytest.raises(ZeroDivisionError):
            get_calc.div(a, b)

    # 浮点数的除法测试用例分开写
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('a, b, expect', get_data()['DIV_float']['datas'], ids=get_data()['DIV_float']['ids'])
    def test_div_float(self, get_calc, a, b, expect):
        result = get_calc.div(a, b)
        assert round(result, 1) == expect

    # 减法
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('a, b, expect', get_data()['SUB']['datas'], ids=get_data()['SUB']['ids'])
    def test_sub(self, get_calc, a, b, expect):
        result = get_calc.sub(a, b)
        assert result == expect

    # 乘法
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('a, b, expect', get_data()['MUL']['datas'], ids=get_data()['MUL']['ids'])
    def test_mul(self, get_calc, a, b, expect):
        result = get_calc.mul(a, b)
        assert result == expect