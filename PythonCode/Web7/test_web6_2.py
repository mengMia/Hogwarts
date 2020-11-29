from time import sleep

from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By


class TestTouchAction():
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    # def teardown(self):
    #     pass

    def test_touchaction_scrollbuttom(self):
        """
        打开chrome
        打开url
        向搜索框中输入selenium测试
        通过touchaction点击搜索框
        滑动到底部，点击下一页
        关闭Chrome
        :return:
        """
        self.driver.get("https://www.baidu.com/")
        ele = self.driver.find_element(By.CSS_SELECTOR, '#kw')
        ele_search = self.driver.find_element(By.CSS_SELECTOR, '#su')

        ele.send_keys("selenium测试")
        action = TouchActions(self.driver)
        action.tap(ele_search)
        action.perform()
        action.scroll_from_element(ele, 0, 10000).perform()
        # sleep(3)

