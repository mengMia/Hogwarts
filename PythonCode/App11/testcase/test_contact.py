from PythonCode.App11.page.app import App


class TestContact:

    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def test_addcontact(self):
        name = "test1"
        gender = "男"
        phonenum = "12100000001"
        result = self.main.goto_address().\
            click_addmember().\
            add_member_manual().\
            add_contact(name, gender, phonenum).get_toast()
        assert '添加成功' == result