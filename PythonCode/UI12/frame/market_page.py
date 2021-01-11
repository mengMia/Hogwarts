from selenium.webdriver.common.by import By

from PythonCode.UI12.frame.base_page import BasePage
from PythonCode.UI12.frame.search_page import SearchPage


class MarketPage(BasePage):
    def goto_search(self):
        self.find(By.ID, "com.xueqiu.android:id/action_search").click()
        return SearchPage(self.driver)