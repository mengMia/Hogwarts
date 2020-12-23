from time import sleep

from appium import webdriver
from appium.webdriver.extensions.android.gsm import GsmCallActions


class TestInteraction():
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
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        desired_caps['chromedriverExecutableDir'] = "E:/Learning/ComputerScience/SoftwareTesting/Hogwarts/driver"
        desired_caps['chromedriverChromeMappingFile'] = "E:/Learning/ComputerScience/SoftwareTesting/Hogwarts/ProjectExercise/PythonCode/App10/mapping.json"
        desired_caps['skipServerInstallation'] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        sleep(3)
        self.driver.quit()

    def test_mobile(self):
        # 模拟来电
        self.driver.make_gsm_call('13512345678', GsmCallActions.CALL)
        # 模拟来短信
        self.driver.send_sms('13612345678', 'hello appium')

        # 录屏,录屏和结束录屏只有8.0以上的版本支持，而且有部分手机不支持录屏
        self.driver.start_recording_screen()
        # 模拟网络设置
        # 001飞行模式，010wifi，100数据蜂窝，110wifi和蜂窝
        self.driver.set_network_connection(1)
        # 保存当前页面截图
        self.driver.get_screenshot_as_file('./photos/img.png')
        sleep(3)
        self.driver.set_network_connection(4)
        sleep(3)

        # 结束录屏
        self.driver.stop_recording_screen()