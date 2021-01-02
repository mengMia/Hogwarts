from appium.webdriver.common.mobileby import MobileBy

from PythonCode.App11.deleteContact_PO.page.addresslist_page import AddressListPage
from PythonCode.App11.deleteContact_PO.page.base_page import BasePage


class MainPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    def goto_message(self):
        # 进入消息页面
        pass

    def goto_address(self):
        # 进入联系人列表页
        self.find(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        return AddressListPage(self.driver)