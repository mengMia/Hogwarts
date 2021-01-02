from appium.webdriver.common.mobileby import MobileBy

from Homework.App11.deleteContact_PO.page.base_page import BasePage


class SearchPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    def click_membername(self, name):
        self.find(MobileBy.XPATH, f'//*[@text="{name}" and @clickable = "false"]').click()
        from PythonCode.App11.deleteContact_PO.page.briefinfoprofile_page import BriefInfoProfilePage
        return BriefInfoProfilePage(self.driver)

    def elementexist(self):
        result = self.find(MobileBy.XPATH, '//*[@text = "无搜索结果"]').text
        return result