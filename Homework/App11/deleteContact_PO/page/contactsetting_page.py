from appium.webdriver.common.mobileby import MobileBy

from PythonCode.App11.deleteContact_PO.page.base_page import BasePage
from PythonCode.App11.deleteContact_PO.page.contactedit_page import ContactEditPage


class ContactSettingPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    def edit_member(self):
        self.find(MobileBy.XPATH, '//*[@text="编辑成员"]').click()
        return ContactEditPage(self.driver)