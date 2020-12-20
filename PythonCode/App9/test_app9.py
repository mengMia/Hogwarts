from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By


class TestToast():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'io.appium.android.apis'
        # 对于安卓来说，默认的工作引擎就是ui2，可以不加这个指定
        desired_caps['automationName'] = 'uiautomator2'
        # 设置到这个popupmenu页面，就会省略掉之前的点击路径，直接进入到这个popup页面
        desired_caps['appActivity'] = 'io.appium.android.apis.view.PopupMenu1'
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        sleep(3)
        self.driver.quit()

    def test_toast(self):
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Make a Popup!").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='Search']").click()
        """
        第一种定位方式，用xpath
        textcontent = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        print(textcontent)
        assert textcontent == "Clicked popup menu item Search"
        """

        # 第二种定位方式，用contains函数检查text中是否包含部分字符串
        print(self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'Clicked popup menu')]").text)
        # 打印当前页面的dom树
        # print(self.driver.page_source)
    if __name__ == '__main__':
        pytest.main()
