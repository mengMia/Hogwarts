from appium.webdriver.common.mobileby import MobileBy

# from PythonCode.App11.page.contactadd_page import ContactAddPage

"""
邀请（添加）联系人页面
"""

class MemberInviteMenuPage:
    def __init__(self, driver):
        """
        定义一个方法接收driver
        """
        self.driver = driver

    def add_member_manual(self):
        """
        点击“手动输入添加”
        """
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        from PythonCode.App11.page.contactadd_page import ContactAddPage
        return ContactAddPage(self.driver)

    def get_toast(self):
        text_toast = self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text   # 这里find_element方法会调用隐式等待，每隔0.5s去查找toast
        return text_toast