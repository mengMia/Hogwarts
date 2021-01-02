from appium.webdriver.common.mobileby import MobileBy

from PythonCode.App11.deleteContact_PO.page.base_page import BasePage
from PythonCode.App11.deleteContact_PO.page.contactsetting_page import ContactSettingPage


class BriefInfoProfilePage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    def click_setting(self):
        self.find(MobileBy.XPATH,
                                 '//*[@text="个人信息"]/../../../../../android.widget.LinearLayout[2]').click()
        return ContactSettingPage(self.driver)