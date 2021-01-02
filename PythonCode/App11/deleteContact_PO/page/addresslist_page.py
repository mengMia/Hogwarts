from appium.webdriver.common.mobileby import MobileBy

from PythonCode.App11.deleteContact_PO.page.base_page import BasePage
from PythonCode.App11.deleteContact_PO.page.search_page import SearchPage


class AddressListPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    def search(self, name):
        # 点击搜索按钮
        self.find(MobileBy.XPATH,
                                 '//*[@text="微信测试"]/../../../../../android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.TextView')\
            .click()
        # 输入搜索内容
        self.find(MobileBy.XPATH, '//*[@text="搜索"]').send_keys(name)
        return SearchPage(self.driver)