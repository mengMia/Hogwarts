import yaml
import pytest

result = yaml.safe_load(open("data.yaml"))
print(result)

# 参数化，生成多条测试用例
# 使用string
class TestData:
    @pytest.mark.parametrize(["a", "b"], yaml.safe_load(open("data.yaml")))
    def test_param(self, a, b):
        print(a + b)