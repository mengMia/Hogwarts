from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestFind():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
        desired_caps['noReset'] = True
        # desired_caps['dontStopAppOnReset'] = True 设置为true代表不重新启动一个app，直接在原来的app页面上操作，但是加了这个好像有问题，提示无法启动雪球app
        desired_caps['skipDeviceInitialization'] = True
        desired_caps['unicodeKeyBoard'] = 'true' # 输入中文搜索词的时候需要加这个，但是貌似不加也不会有问题
        desired_caps['resetKeyBoard'] = 'true'
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        sleep(3)
        self.driver.quit()

    # 雪球app上滑动
    def test_touchaction(self):
        sleep(5)
        action = TouchAction(self.driver)
        # action.press(x=696,y=1000).wait(200).move_to(x=696,y=225).release().perform()
        # 获取屏幕的尺寸
        window_size = self.driver.get_window_rect()
        width = window_size['width']
        height = window_size['height']
        x1 = int(width/2)
        y_start = int(height*0.8)
        y_end = int(height*0.2)
        action.press(x=x1,y=y_start).wait(200).move_to(x=x1,y=y_end).release().perform()

