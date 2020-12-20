from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWebDriverWait():
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

    def test_wait(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.XPATH,
                                 '//*[@resource-id="com.xueqiu.android:id/name" and @text="阿里巴巴"]').click()
        # self.driver.find_element_by_xpath("//*[contains(@resource-id, 'title_container')]//*[@text='股票']").click()
        locator = (MobileBy.XPATH, "//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        # 使用显示等待，until里面传入的是method，method里面需要传入locator
        # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        # 使用lambda表达式
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*locator))
        current_price = float(self.driver.find_element(*locator).text)
        print(current_price)

    if __name__ == '__main__':
        pytest.main()
