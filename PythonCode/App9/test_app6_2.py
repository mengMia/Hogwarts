from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestTouchAction():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'cn.kmob.screenfingermovelock'
        desired_caps['appActivity'] = 'com.samsung.ui.MainActivity'
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

    #
    def test_touchaction_unlock(self):
        action = TouchAction(self.driver)
        action.press(x=120,y=172).wait(200).move_to(x=364,y=179).wait(200).move_to(x=599,y=174).wait(200)\
            .move_to(x=599,y=417).wait(200).move_to(x=601,y=654).release().perform()