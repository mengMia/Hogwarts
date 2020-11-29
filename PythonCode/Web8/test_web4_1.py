from selenium.webdriver.common.by import By

from PythonCode.Web8.base import Base


class TestTestDemo(Base):
    def test_testdemo(self):
        self.driver.get("https://ceshiren.com")
        self.driver.find_element(By.LINK_TEXT, "所有分类").click()

        # 断言，点击所有分类之后，按钮是高亮的，class属性在点击前和点击后发生了变化
        element = self.driver.find_element(By.LINK_TEXT, "所有分类")
        result = element.get_attribute("class")
        assert result == 'active'