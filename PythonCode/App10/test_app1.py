from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import assert_that, close_to

# 这个代码有两条测试用例，但是每次执行测试用例的时候都要重启app，在第一条测试用例结束之后，应该点击取消之后可以回到主搜索界面，但是某些设置导致每次app都重启，待解决
class TestFind():
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
        desired_caps['unicodeKeyBoard'] = 'true' # 输入中文搜索词的时候需要加这个，但是貌似不加也不会有问题
        desired_caps['resetKeyBoard'] = 'true'
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        sleep(3)
        # self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/action_close").click()
        self.driver.quit()
        # pass

    @pytest.mark.parametrize('searchkey, type, price',[
        ('阿里巴巴', 'BABA', 250),
        ('小米', '01810', 28)
    ])
    def test_search(self, searchkey, type, price):
        """
        1.打开雪球app
        2.点击搜索输入框
        3.向搜索输入框输入搜索词，”阿里巴巴“或“小米”
        4.在搜索结果里面选择第一个，点击
        5.判断股票价格
        :return:
        """
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/tv_search").click()
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text").send_keys(searchkey)
        self.driver.find_element(MobileBy.XPATH,
                                 '//*[@resource-id="com.xueqiu.android:id/name"]').click()

        # 这里注意f"的用法，和'{type}'
        price_ele = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{type}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        # 这里一定要加上float，否则是字符串形式的
        current_price = float(price_ele.text)
        print(current_price)
        expect_price = price
        assert_that(current_price, close_to(expect_price, expect_price*0.1))


