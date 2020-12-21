from appium import webdriver
from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestBrowser():
    def setup(self):
        # desired_caps = {
        #     'platformName': 'android',
        #     'platformVersion': '6.0',
        #     'browserName': 'Browser',
        #     'noReset': True,
        #     'deviceName': 'emulator-5554',
        #     'chromedriverExecutable': 'E:/Learning/ComputerScience/SoftwareTesting/Hogwarts/chromedriver24.exe'
        # }
        desired_caps = {
            'platformName': 'android',
            'platformVersion': '6.0',
            'appPackage': 'io.appium.android.apis',
            'appActivity': 'io.appium.android.apis.ApiDemos',
            'noReset': True,
            'deviceName': 'emulator-5554',
            'chromedriverExecutable': 'E:/Learning/ComputerScience/SoftwareTesting/Hogwarts/chromedriver24.exe'
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        self.driver.get("http://m.baidu.com")
        self.driver.find_element(By.ID, 'index-kw').click()
        self.driver.find_element(By.ID, 'index-kw').send_keys("appium")
        search_locator = (By.ID, 'index-bn')
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(search_locator))
        self.driver.find_element(*search_locator).click()

    def test_webview(self):
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Views').click()
        webview = "WebView"
        # 打印上下文，在点击webview之前，是native app页面
        print(self.driver.contexts)
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        f'scrollIntoView(new UiSelector().text("{webview}").'
                                                        'instance(0))').click()
        # 第一种定位方式：用mumu模拟器的时候，渲染不出来webview里面的元素，所以定位会失败，找不到这个元素，可以尝试使用真机安装appium的这个demo api（io.appium.android.apis）
        # 不推荐使用这种方式，不同手机渲染效果不一样，会导致用例在其他手机上无法执行
        # 这种方式的page_source是dom树的类型，xml格式的
        # self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'i has no focus').send_keys("this is a test")
        # self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'i am a link').click()
        # print(self.driver.page_source)

        # 点击webview之后，多了一个webview页面
        print(self.driver.contexts)
        # 想要操作webview页面，需要把context切换为webview，否则会报错：找不到元素
        self.driver.switch_to.context(self.driver.contexts[-1])
        # 第二种定位方式：通过谷歌开发者工具，inspect，进行网页端元素的定位
        # 这种方式的page_source是html格式的
        self.driver.find_element(By.ID, 'i_am_a_textbox').send_keys("this is a test")
        self.driver.find_element(By.ID, 'i am a link').click()
        print(self.driver.page_source)