from appium.webdriver.common.mobileby import MobileBy

from Homework.App11.deleteContact_PO.page.base_page import BasePage


class ContactEditPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    def delete_contact(self):
        self.find(MobileBy.XPATH, '//*[@text = "删除成员"]').click()
        self.find(MobileBy.XPATH, '//*[@text = "确定"]').click()
        from PythonCode.App11.deleteContact_PO.page.search_page import SearchPage
        return SearchPage(self.driver)