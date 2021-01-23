"""
base_page.py 基类模块：主要用来初始化driver， 定位find， 常用的最基本的方法
"""
import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    # 基类里面加日志
    # logging是python的日志工具
    # >> todo:理解logging
    # >> todo: logging的等级，1一个日记本利，不同颜色来表明：
    # >> todo: 1.noset 0 等于没写，废话
    # >> todo: 2. debug， 10， 一些额外信息，备注，往往和主体功能无关，日报里面的备注
    # >> todo: 3.info，20，主体功能的信息。日报，做了啥
    # >> todo:  4.warning，30，警告，下次可能要出错了。
    # >> todo: 5.error，40，犯错，违法
    # >> todo: 6.critical，50，极其严重。

    # 其他类
    # >> todo: 1.日志收集器 logger：日记本
    # >> todo: 2.日志收集器级别 level
    # >> todo: 3.日志处理器准备 handler：不同记号的笔
    # >> todo: 4.日志处理器级别设置
    # >> todo: 5.设置日志格式format
    # >> todo: 6.添加日志处理器

    # 创建一个logger日志对象
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