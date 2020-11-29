from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestFrom():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    # def teardown(self):
    #     pass

    def test_form(self):
        self.driver.get("https://testerhome.com/account/sign_in")
        self.driver.find_element(By.CSS_SELECTOR, '#user_login').send_keys("username")
        self.driver.find_element(By.CSS_SELECTOR, '#user_password').send_keys("234")
        self.driver.find_element(By.CSS_SELECTOR, '#user_remember_me').click()
        self.driver.find_element(By.XPATH, '//*[@type = "submit"]').click()
        sleep(3)