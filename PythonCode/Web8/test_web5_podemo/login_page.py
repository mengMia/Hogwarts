from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from PythonCode.Web8.test_web5_podemo.register_page import RegisterPage


class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 扫码
    def scan(self):
        pass

    # 进入注册页
    def goto_register(self):
        self.driver.find_element(By.CSS_SELECTOR, '.login_registerBar_link').click()
        return RegisterPage(self.driver)