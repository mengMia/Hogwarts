from appium import webdriver

from PythonCode.App11.deleteContact_PO.page.app import App


class TestDeleteContact:
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def test_deleteContact(self):
        name = "测试21"
        result = self.main.goto_address().search(name).click_membername(name).click_setting().edit_member().delete_contact().elementexist()
        assert "无搜索结果" == result
