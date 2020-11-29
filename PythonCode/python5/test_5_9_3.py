import allure
from selenium import webdriver
import time
import pytest

@allure.testcase("https://www.baidu.com的搜索功能")
@pytest.mark.parametrize('test_data1', ['allure', 'pytest', 'unittest'])
def test_steps_demo(test_data1):
    with allure.step("step one: 打开浏览器输入百度网址"):

        driver = webdriver.chrome(executable_path = '/Users/')