from selenium.webdriver.common.by import By

from PythonCode.UI12.frame.base_page import BasePage
from PythonCode.UI12.frame.market_page import MarketPage


class MainPage(BasePage):
    def goto_market(self):
        # 在点击行情tab之前，点击那个编辑按钮，弹出登录页面，制造异常
        self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']").click()
        # 点击行情
        self.find(By.XPATH, "//*[@resource-id='android:id/tabs']//*[@text='行情']").click()
        return MarketPage(self.driver)
