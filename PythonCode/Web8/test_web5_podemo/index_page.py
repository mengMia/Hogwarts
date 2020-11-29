"""

"""
from selenium import webdriver
from selenium.webdriver.common.by import By

# from Web8.base import Base
from PythonCode.Web8.test_web5_podemo.login_page import LoginPage
from PythonCode.Web8.test_web5_podemo.register_page import RegisterPage


class IndexPage():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")

    # 进入登录页
    def goto_login(self):
        # 点击登录
        self.driver.find_element(By.CSS_SELECTOR, '.index_top_operation_loginBtn').click()
        # 返回一个登录页面
        return LoginPage(self.driver)

    # 进入注册页
    def goto_register(self):
        # 点击立即注册
        self.driver.find_element(By.CSS_SELECTOR, '.index_head_info_pCDownloadBtn').click()
        # 返回一个注册页面
        return RegisterPage(self.driver)
