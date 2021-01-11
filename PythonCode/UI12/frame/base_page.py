from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _black_list = [(By.XPATH, "//*[@resource-id = 'com.xueqiu.android:id/iv_action_back']")]
    _max_num = 3
    _error_num = 0
    def __init__(self, driver: WebDriver=None):
        """
        初始化应用
        """
        if driver is None:
            caps = {}
            caps["platformName"] = "android"
            caps['platformVersion'] = '6.0'
            caps['deviceName'] = 'emulator-5554'
            caps["appPackage"] = "com.xueqiu.android"
            caps["appActivity"] = ".view.WelcomeActivityAlias"
            caps["noReset"] = "true"
            caps['skipDeviceInitialization'] = True
            caps['skipServerInstallation'] = True

            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver = driver

    def find(self, by, locator=None):
        """
        查找元素
        :return:
        """
        try:
            if locator is None:
                result = self.driver.find_element(*by)
            else:
                result = self.driver.find_element(by, locator)
            # 元素找到了，计数器置0
            self._error_num = 0
            return result
        # 捕获黑名单中的元素
        except Exception as e:
            # 如果计数器超过最大查找次数，抛出异常；否则更新计数器
            if (self._error_num > self._max_num):
                raise e
            self._error_num += 1
            # 遍历黑名单，在页面上去找有没有这些元素
            for black_ele in self._black_list:
                ele = self.driver.find_elements(*black_ele)
                if len(ele) > 0:
                    ele[0].click()
                    # 处理完黑名单之后，再次查找原来的元素
                    return self.find(by, locator)
            raise e
