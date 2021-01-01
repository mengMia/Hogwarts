
"""
通讯录界面
"""
from PythonCode.App11.page.base_page import BasePage
from PythonCode.App11.page.member_invite_menu_page import MemberInviteMenuPage


class AddressListPage(BasePage):
    # def __init__(self, driver):
    #     """
    #     定义一个方法接收driver
    #     """
    #     self.driver = driver

    def click_addmember(self):
        """
        点击添加成员按钮
        """
        # 滚动查找”添加成员“按钮
        self.find_by_scroll("添加成员").click()

        return MemberInviteMenuPage(self.driver)