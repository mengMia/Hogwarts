from appium.webdriver.common.mobileby import MobileBy

from PythonCode.App11.page.addresslist_page import AddressListPage
from PythonCode.App11.page.base_page import BasePage


class MainPage(BasePage):
    # def __init__(self, driver):
    #     """
    #     定义一个方法接收driver
    #     """
    #     self.driver = driver
    # 把定位参数定义成一个类变量传入方法中
    address_element = (MobileBy.XPATH, '//*[@text="通讯录"]')
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
        # self.find(*self.address_element).click()
        self.find_and_click(*self.address_element)
        return AddressListPage(self.driver)
