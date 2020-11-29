from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class RegisterPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 填写注册信息
    def register(self):
        # 企业名称
        self.driver.find_element(By.CSS_SELECTOR, '#corp_name').send_keys('aaaa')
        # 管理员名称
        self.driver.find_element(By.CSS_SELECTOR, '#manager_name').send_keys('bbbb')
        # 管理员电话号码
        self.driver.find_element(By.CSS_SELECTOR, '#register_tel').send_keys('13122220000')
        # 点击注册按钮
        self.driver.find_element(By.CSS_SELECTOR, '#submit_btn').click()
        return True
