from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        # pass

    # def teardown(self):
    #     self.driver.quit()
    #     # pass

    # 鼠标点击事件
    @pytest.mark.skip
    def test_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        element_click = self.driver.find_element(By.XPATH, '//*[@value="click me"]')
        element_doubleclick = self.driver.find_element(By.XPATH, '//*[@value="dbl click me"]')
        element_rightclick = self.driver.find_element(By.XPATH, '//*[@value="right click me"]')
        # 创建一个对象
        action = ActionChains(self.driver)
        # click
        action.click(element_click)
        # 右击用的是contex_click
        action.context_click(element_rightclick)
        action.double_click(element_doubleclick)
        sleep(3)
        action.perform()
        # pass

    # 鼠标移动到某个元素上
    def test_movetoelement(self):
        self.driver.get("https://www.baidu.com/")
        ele = self.driver.find_element(By.XPATH, '//*[@class="s-top-right-text c-font-normal c-color-t"]')
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        sleep(3)
        action.perform()
        sleep(3)

    # 拖拽
    def test_dragdrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag_ele = self.driver.find_element(By.CSS_SELECTOR, '#dragger')
        # drag_ele = self.driver.find_element(By.XPATH, '//*[@class="drag"]')
        drop_ele = self.driver.find_element(By.XPATH, '/html/body/div[2]')
        action = ActionChains(self.driver)
        # action.drag_and_drop(drag_ele, drop_ele).perform()
        # action.click_and_hold(drag_ele).release(drop_ele).perform()
        action.click_and_hold(drag_ele).move_to_element(drop_ele).release().perform()
        sleep(3)

    # 模拟键盘操作
    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele = self.driver.find_element(By.CSS_SELECTOR, 'body > label:nth-child(2) > input[type=textbox]')

        ele.click()
        action = ActionChains(self.driver)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(3)
