from appium.webdriver.common.mobileby import MobileBy

from PythonCode.App11.page.addresslist_page import AddressListPage


class MainPage:
    def __init__(self, driver):
        """
        定义一个方法接收driver
        """
        self.driver = driver

    def goto_message(self):
        """
        进入到消息页
        :return:
        """
        pass

    def goto_address(self):
        """
        点击通讯录tab，进入到通讯录页面
        :return:
        """
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        return AddressListPage(self.driver)