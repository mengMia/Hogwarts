from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import assert_that, close_to


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
        self.driver.quit()

    def test_search(self):
        """
        1.打开雪球app
        2.点击搜索输入框
        3.向搜索输入框输入”阿里巴巴“
        4.在搜索结果里面选择“阿里巴巴”，点击
        5.获取这只香港阿里巴巴的股价，并判断价格>200
        :return:
        """
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/name" and @text="阿里巴巴"]').click()
        current_price = float(self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/current_price').text)
        print(current_price)
        assert current_price > 200
        # 使用hamcrest断言
        expect_price = 250
        assert_that(current_price, close_to(expect_price, expect_price * 0.1))

    def test_get_currentPrice(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.XPATH,
                                 '//*[@resource-id="com.xueqiu.android:id/name" and @text="阿里巴巴"]').click()
        current_price = float(self.driver.find_element(MobileBy.XPATH, "//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text)
        print(current_price)

    def test_myinfo_uiauto(self):
        """
        1.点击我的，进入到个人信息页面
        2.点击登录，进入登录页面
        3.输入用户名、密码
        4.点击登录
        :return:
        """
        # 定位“我的”有两种方法
        # 1.直接用text进行定位
        # self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        # 2.先用tabname，找到之后再用text,通过组合属性的方式定位元素，用.
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/tab_name").text("我的")').click()
        sleep(3)
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("帐号密码")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys("18225510081")
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys("57030qwert!!")
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()
        # 通过父亲结点定位元素
        # self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/title_container").childSelector(text("股票"))').click()

    def test_scroll_find_element(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("关注")').click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("银行螺丝钉").'
                                                        'instance(0))').click()
        sleep(5)
    if __name__ == '__main__':
        pytest.main()
