from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import *
from selenium.webdriver.common.by import By


class TestAtttibute():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
        desired_caps['noReset'] = True
        # desired_caps['dontStopAppOnReset'] = True
        desired_caps['skipDeviceInitialization'] = True
        desired_caps['unicodeKeyBoard'] = 'true'  # 输入中文搜索词的时候需要加这个，但是貌似不加也不会有问题
        desired_caps['resetKeyBoard'] = 'true'
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        sleep(3)
        self.driver.quit()

    # get_attribute示例代码
    # @pytest.mark.skip
    def test_get_attr(self):
        # find_element本来就自带了异常处理
        search_ele = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        print(search_ele.get_attribute("content-desc"))
        print(search_ele.get_attribute("resource-id"))
        print(search_ele.get_attribute("enabled"))
        print(search_ele.get_attribute("clickable"))
        print(search_ele.get_attribute("bounds"))
        assert 'search' in search_ele.get_attribute("resource-id")

    # 断言示例代码
    def test_assert(self):
        a = 10
        b = 20
        assert a < b

    def test_hamrest(self):
        assert_that(10, equal_to(10), "10等于10")
        # close_to用法，10上下浮动2个
        assert_that(8, close_to(10, 2))
        # contains_string用法，包含某些字符串
        assert_that("contains some string", contains_string("string"))

    if __name__ == '__main__':
        pytest.main()
