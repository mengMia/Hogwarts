from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from PythonCode.Web8.test_web5_2_podemo.page.base_page import BasePage


class AddMemberPage(BasePage):
    # def __init__(self, driver: WebDriver):
    #     self.driver = driver

    # 添加联系人
    def add_member(self, username, account, phonenum):
        # sleep(2)
        self.driver.find_element(By.ID, 'username').send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, '#memberAdd_acctid').send_keys(account)
        self.driver.find_element(By.CSS_SELECTOR, '#memberAdd_phone').send_keys(phonenum)
        self.driver.find_element(By.CSS_SELECTOR, '.js_btn_save').click()
        sleep(2)
        return True

    # 验证联系人是否添加成功
    def get_member(self):
        contactlist = self.driver.find_elements(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        # 列表推导式
        titilelist = [element.get_attribute("title") for element in contactlist]

        return titilelist