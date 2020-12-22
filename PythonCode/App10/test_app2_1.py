from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWebview():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
        desired_caps['noReset'] = True
        # desired_caps['dontStopAppOnReset'] = True
        desired_caps['skipDeviceInitialization'] = True
        desired_caps['unicodeKeyBoard'] = 'true'  # 输入中文搜索词的时候需要加这个，但是貌似不加也不会有问题
        desired_caps['resetKeyBoard'] = 'true'
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        sleep(3)
        self.driver.quit()

    # 这个代码还有些问题，代码一直执行不停
    def test_webview(self):
        """
        1.雪球app点击交易
        2.点击A股开户
        3.进入页面输入手机号和验证码
        :return:
        """
        # 点击交易
        self.driver.find_element(MobileBy.XPATH, '//*[@text="交易"]').click()
        # 通过映射到chrome开发者工具上进行定位,暂时这个没映射过去，路径不对
        # self.driver.switch_to.context(self.driver.contexts[-1])
        # self.driver.find_element(MobileBy.XPATH, '//*[@id="Layout_app_3V4"]/div/div/ul/li[1]/div[2]/h1').click()

        # 点击A股开户
        # 通过uiautomator2上的元素进行定位
        A_locator = (MobileBy.ACCESSIBILITY_ID, 'A股开户')
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(A_locator))
        self.driver.find_element(*A_locator).click()

        # 切换上下文,一般新页面的上下文会放在最后一个
        self.driver.switch_to.context(self.driver.contexts[-1])
        # 切换窗口，点击立即开户之后的页面，相当于浏览器上新开了一个窗口，这个可以在谷歌浏览器开发者工具上的inspect查看
        self.driver.switch_to.window(self.driver.window_handles[-1])

        # 填写手机号和验证码
        phone_locator = (MobileBy.ID, 'phone-number')
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(phone_locator))
        self.driver.find_element(*phone_locator).send_keys("12345678901")
        self.driver.find_element(MobileBy.ID, 'code').send_keys("1234")
        # self.driver.find_element(MobileBy.XPATH, '')

