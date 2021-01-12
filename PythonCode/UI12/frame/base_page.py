from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from PythonCode.UI12.frame.handle_black import handle_black_list


class BasePage:
    black_list = [(By.XPATH, "//*[@resource-id = 'com.xueqiu.android:id/iv_action_back']")]
    max_num = 3
    error_num = 0
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

    @handle_black_list
    def find(self, by, locator=None):
        """
        查找元素
        :return:
        """
        if locator is None:
            result = self.driver.find_element(*by)
        else:
            result = self.driver.find_element(by, locator)
        return result
