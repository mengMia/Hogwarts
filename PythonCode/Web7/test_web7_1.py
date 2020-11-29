from time import sleep

from PythonCode.Web7.base import Base


class TestWindows(Base):
    def test_window(self):
        """
        打开百度页面
        点击登录
        弹框中点击立即注册，输入用户名和账号
        返回刚才的登录页面，点击登录
        输入用户名和密码，点击登录
        :return:
        """
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_link_text("登录").click()
        # print(self.driver.current_window_handle)
        self.driver.find_element_by_link_text("立即注册").click()
        # print(self.driver.current_window_handle)
        # print(self.driver.window_handles)
        windows = self.driver.window_handles
        self.driver.switch_to_window(windows[-1])
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("username")
        self.driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys("18009990000")

        sleep(3)
        self.driver.switch_to_window(windows[0])
        # 返回刚才的登录页面，点击登录
        self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()
        # 输入用户名和密码，点击登录
        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("18009990000")
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys("hi90900")
        self.driver.find_element_by_id("TANGRAM__PSP_11__submit").click()

        sleep(3)