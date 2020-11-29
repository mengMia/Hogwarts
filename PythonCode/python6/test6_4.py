import pytest
import yaml

from PythonCode.python6.code.calculator import Calculator

# @pytest.mark.parametrize('c', [7, 8, 9])
# @pytest.mark.parametrize('b', [4, 5, 6])
# @pytest.mark.parametrize('a', [1, 2, 3])
# def test_parm(a, b, c):
#     print(a, b, c)


def get_datas():
    with open("./datas/calc.yml", encoding='utf-8') as f:  #yaml里面有中文的时候，这里要加个编码格式
        datas = yaml.safe_load(f)
    add_datas = datas['add']['datas']
    add_ids = datas['add']['ids']

    return [add_datas, add_ids]

# 解析测试步骤文件
# addstepsfile 在
def steps(addstepsfile, calc, a, b, expect):
    with open(addstepsfile) as f:
        steps = yaml.safe_load(f)

    for step in steps:
        if "add" == step:
            result = calc.add(a, b)
        elif "add1" == step:
            result = calc.add1(a, b)
        assert expect == result

class TestCalc1:
    def setup_class(self):
        print("计算开始")
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize('a, b, expect', get_datas()[0], ids=get_datas()[1])
    def test_add(self, a, b, expect):
        # 由于每个测试用例都需要初始化，所以放在setup_class里面初始化即可
        # calc = Calculator()
        result = self.calc.add(a, b)
        assert result == expect

    def test_add_steps(self, ):
        a = 1
        b = 1
        expect = 2
        steps("./steps/add_steps.yml", self.calc, a, b, expect)
