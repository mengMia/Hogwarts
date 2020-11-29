"""
1.打开页面：https://testerhome.com/
2.点击-社团标签
3.点击-霍格沃兹学院
4.访问顶部的第一个帖子
"""
from selenium import webdriver
import time

class TestHogwarts():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        # pass

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    def test_hogwarts(self):
        self.driver.get("https://ceshiren.com/")
        # time.sleep(2)
        # self.driver.find_element_by_id("ember47").click()  # 精华帖，用这个好像定位不到精华帖
        # time.sleep(2)
        # self.driver.find_element_by_class_name("raw-link").click()
        self.driver.find_element_by_xpath('//*[@title = "原创精华文章,有100元奖金"]').click()
        self.driver.find_element_by_class_name("raw-link").click()

        self.driver.find_element_by_xpath('//*[@title = "在最近的一年，一月，一周或一天最活跃的主题"]').click()


