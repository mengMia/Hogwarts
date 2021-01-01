from appium.webdriver.common.mobileby import MobileBy

# from PythonCode.App11.page.contactadd_page import ContactAddPage
from PythonCode.App11.page.base_page import BasePage

"""
邀请（添加）联系人页面
"""

class MemberInviteMenuPage(BasePage):
    # def __init__(self, driver):
    #     """
    #     定义一个方法接收driver
    #     """
    #     self.driver = driver

    def add_member_manual(self):
        """
        点击“手动输入添加”
        """
        self.find(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        from PythonCode.App11.page.contactadd_page import ContactAddPage
        return ContactAddPage(self.driver)

    def get_toast(self):
        text_toast = self.get_toast_text()
        return text_toast