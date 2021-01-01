"""
base_page.py 基类模块：主要用来初始化driver， 定位find， 常用的最基本的方法
"""
import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    # 基类里面加日志
    # logging是python的日志工具
    root_logger = logging.getLogger()
    print(f"root_logger.handlers:{logging.getLogger().handlers}")
    for h in root_logger.handlers[:]:
        root_logger.removeHandler(h)
    logging.basicConfig(level=logging.INFO)

    # 每个页面都需要这个方法，所以可以抽离出来放到基类中
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, locator):
        logging.info(by)
        logging.info(locator)
        # find里面可以加入页面出现弹框的处理逻辑
        return self.driver.find_element(by, locator)

    def find_and_click(self, by, locator):
        logging.info('click')
        self.find(by, locator).click()

    # 封装滚动查找
    def find_by_scroll(self, text):
        logging.info('find_by_scroll')
        logging.info(text)
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                                        f'new UiScrollable(new UiSelector()\
                                                        .scrollable(true).instance(0))\
                                                        .scrollIntoView(new UiSelector()\
                                                        .text("{text}").instance(0));')

    def get_toast_text(self):
        logging.info('get_toast_text')
        result = self.find(MobileBy.XPATH,
                               '//*[@class="android.widget.Toast"]').text
        logging.info(result)
        return result