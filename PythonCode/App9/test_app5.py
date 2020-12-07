from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

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
        2.定位首页的搜索框
        3.判断搜索框是否可用，并查看搜索框name属性值
        4.打印搜索框这个元素的左上角坐标和它的宽高
        5.向搜索输入框输入”阿里巴巴“
        6.判断【阿里巴巴】是否可见
        7.如果可见，打印搜索成功，不可见打印搜索失败
        :return:
        """
        element = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        # 搜索框是否可用
        search_enabled = element.is_enabled()
        # 查看搜索框的name属性值
        print(element.text)
        # 打印搜索框的坐标
        print(element.location)
        # 打印宽和高
        print(element.size)
        if search_enabled == True:
            element.click()
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
            ele2 = self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/name" and @text="阿里巴巴"]')
            # 判断【阿里巴巴】是否可见
            # ele2.is_displayed()
            ele2_displayed = ele2.get_attribute("displayed")
            if ele2_displayed == 'true':
                print("搜索成功")
            else:
                print("搜索失败")
        # current_price = float(self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/current_price').text)
        # print(current_price)
        # assert current_price > 200

    if __name__ == '__main__':
        pytest.main()
