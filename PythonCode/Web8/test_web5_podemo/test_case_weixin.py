from PythonCode.Web8.test_web5_podemo.index_page import IndexPage


class TestWX:
    def setup(self):
        self.index = IndexPage()

    def test_register(self):
        # 从首页进入登录页->进入注册页->进行注册
        # assert self.index.goto_login().goto_register().register()

        # 从首页直接进入注册页注册
        assert self.index.goto_register().register()