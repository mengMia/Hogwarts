from Homework.Web8.test_web_podemo.page.main_page import MainPage


class TestWX:
    def setup(self):
        self.main = MainPage()

    def test_addmember(self):
        username = "测试27"
        account = "test27@qq.com"
        phonenum = "12100000027"
        # 首页点击添加联系人，直接进入添加页面
        # addmember = self.main.goto_addmember()

        # 点击通讯录按钮，进入通讯录页面，点击添加成员按钮，进入添加页面
        addmember = self.main.goto_contact_member()
        addmember.add_member(username, account, phonenum)
        assert username in addmember.get_member(username)