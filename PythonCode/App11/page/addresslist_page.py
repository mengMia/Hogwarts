
"""
通讯录界面
"""
from PythonCode.App11.page.member_invite_menu_page import MemberInviteMenuPage


class AddressListPage:
    def __init__(self, driver):
        """
        定义一个方法接收driver
        """
        self.driver = driver

    def click_addmember(self):
        """
        点击添加成员按钮
        """
        # 滚动查找”添加成员“按钮
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("添加成员").'
                                                        'instance(0))').click()

        return MemberInviteMenuPage(self.driver)