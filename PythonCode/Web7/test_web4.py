from time import sleep

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://ceshiren.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    # def teardown(self):
    #     self.driver.quit()
    #     # pass

    def test_wait(self):
        self.driver.find_element_by_xpath('//*[@title="有了新帖的活动主题"]').click()  # 最新

        # # 这个自定义的方法一定要有个参数，要不然会报错
        # def wait(x):
        #     return len(self.driver.find_elements_by_xpath('//*[@class = "ember-view"]')) >= 1  # 精华帖
        # WebDriverWait(self.driver, 10).until(wait)  # 这里的wait不要加括号，加了括号表示调用的意思，不是传参了

        # 这句代码有点问题
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.driver.find_element_by_xpath('//*[@title="原创精华文章,有100元奖金"]')))
        self.driver.find_element_by_xpath('//*[@title="在最近的一年，一月，一周或一天最活跃的主题"]').click()     # 热门
