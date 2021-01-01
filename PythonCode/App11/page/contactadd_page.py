
"""
编辑联系人页面
"""
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

# from PythonCode.App11.page.member_invite_menu_page import MemberInviteMenuPage
from PythonCode.App11.page.base_page import BasePage


class ContactAddPage(BasePage):
    # def __init__(self, driver):
    #     """
    #     定义一个方法接收driver
    #     """
    #     self.driver = driver

    """
    这个页面上的输入姓名、性别、手机号，这几个服务可以拆开写，如下，也可以合在一个方法里
    """
    # def set_name(self):
    #     pass
    #
    # def set_gender(self):
    #     pass
    #
    # def set_phonenum(self):
    #     pass

    def add_contact(self, name, gender, phonenum):
        # 输入姓名
        self.find(MobileBy.XPATH, '//*[contains(@text, "姓名")]/../android.widget.EditText').send_keys(
            name)
        # 或者通过：//*[contains(@text, '姓名')]/../*[@text="必填"]来定位这个姓名的输入框

        # 选择性别
        self.find(MobileBy.XPATH, '// *[contains( @ text, "性别")] /..// *[ @ text = "男"]').click()
        if gender == "男":
            # 这里需要加个显示等待，因为从上面一步定位的男，切换到下面再定位男，会有报错，
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, '//*[@text="女"]'))
            self.find(MobileBy.XPATH, '//*[@text="男"]').click()
        else:
            self.find(MobileBy.XPATH, '//*[@text="女"]').click()

        # 输入手机号
        self.find(MobileBy.XPATH,
                                 '//*[contains(@text, "手机") and contains(@class, "TextView")]/..//*[@text="手机号"]').send_keys(
            phonenum)

        # 点击保存
        self.find(MobileBy.XPATH, '//*[@text="保存"]').click()

        # 点击保存之后需要返回到这个界面，获取toast，所以获取toast的方法，应该在MemberInviteMenuPage这个页面里添加
        from PythonCode.App11.page.member_invite_menu_page import MemberInviteMenuPage
        return MemberInviteMenuPage(self.driver)