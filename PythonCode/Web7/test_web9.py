from time import sleep

from selenium.webdriver.common.by import By

from PythonCode.Web7.base import Base


class TestJS(Base):
    def test_js_scroll(self):
        """
        百度搜索selenium测试
        点击百度一下
        滑动到底部
        :return:
        """
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("selenium测试")
        ele = self.driver.execute_script('return document.getElementById("su")')
        ele.click()
        # 滑动到最底部
        self.driver.execute_script('document.documentElement.scrollTop=10000')
        sleep(3)
        # 点击下一页
        self.driver.find_element(By.CSS_SELECTOR, '#page > div > a.n').click()
        sleep(3)

        # 打印上述过程的性能数据
        for code in [
            'return document.tile', 'return JSON.stringify(performance.timing)'
        ]:
            print(self.driver.execute_script(code))

        # print(self.driver.execute_script("return document.tile;return JSON.stringify(performance.timing)"))  这种方式执行返回的是none

    def test_datetime(self):
        """
        12306网站上对readonly属性的日期进行修改
        先移除readonly属性
        再修改日期
        :return:
        """
        self.driver.get("https://www.12306.cn/index/")
        time_ele = self.driver.execute_script('a = document.getElementById("train_date"); a.removeAttribute("readonly")')
        sleep(3)
        self.driver.execute_script("document.getElementById('train_date').value = '2020-12-30'")
        sleep(3)
        print(self.driver.execute_script("return document.getElementById('train_date').value"))

