import pytest
import yaml


class TestDemo:
    @pytest.mark.parametrize("env", yaml.safe_load(open("env.yaml")))
    def test_demo(self, env):
        if "test" in env:
            print("这是测试环境")
            print(env)  # 此时只打印key，也就是test字符串，可以通过将env改成一个列表包裹字典的形式
            print("测试环境的ip是：", env["test"])
        if "dev" in env:
            print("这是开发环境")

    def test_yaml(self):
        print(yaml.safe_load(open("env.yaml")))
