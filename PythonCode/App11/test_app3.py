from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestInteraction():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.LaunchSplashActivity'
        desired_caps['noReset'] = True  # 这里的noreset设置为true，重启app的时候就不会清除登录信息
        # desired_caps['dontStopAppOnReset'] = True
        desired_caps['skipDeviceInitialization'] = True
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        # desired_caps['settings[waitForIdleTimeout]'] = 0
        # desired_caps['chromedriverExecutableDir'] = "E:/Learning/ComputerScience/SoftwareTesting/Hogwarts/driver"
        # desired_caps['chromedriverChromeMappingFile'] = "E:/Learning/ComputerScience/SoftwareTesting/Hogwarts/ProjectExercise/PythonCode/App10/mapping.json"
        desired_caps['skipServerInstallation'] = True
        # 使用appium自动启动指定的模拟器
        # desired_caps['avd'] = 'Pixel_23_6'
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        sleep(3)
        self.driver.quit()

    def test_daka(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="工作台"]').click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("打卡").'
                                                        'instance(0))').click()
        # 或者
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector()\
        #                          .scrollable(true).instance(0)) \
        #                          .scrollIntoView(new UiSelector()\
        #                          .text("打卡").instance(0));').click()
        # settings
        self.driver.update_settings({"waitForIdleTimeout":0})
        self.driver.find_element(MobileBy.XPATH, '//*[@text="外出打卡"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "次外出")]').click()
        # sleep(2)
        # assert "外出打卡成功" in self.driver.page_source  # 这里没有使用find_element方法，是不会用到隐式等待时间的，所以需要加一个显示等待
        WebDriverWait(self.driver, 10).until(lambda x: "外出打卡成功" in x.page_source)
        # success = self.driver.find_element(MobileBy.XPATH, '//*[@text="外出打卡成功"]').text
        # assert success == "外出打卡成功"