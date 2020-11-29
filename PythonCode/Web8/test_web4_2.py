from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# from Web8.base import Base


class TestTestDemo():
    def setup(self):
        options = Options()
        options.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=options)

    def teardown(self):
        self.driver.quit()

    def test_testdemo(self):
        self.driver.get("https://ceshiren.com")
        sleep(3)

    # 在当前已经登录企业微信的浏览器页面，获取联系人
    def test_weixin(self):
        self.driver.find_element(By.ID, 'menu_contacts').click()
        sleep(3)