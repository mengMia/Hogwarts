"""
app.py 模块，存放app相关的一些操作。
比如 启动应用，重启应用，停止应用，进入到首页
"""
from time import sleep

from appium import webdriver

from PythonCode.App11.page.main_page import MainPage


class App:
    def start(self):
        # 启动app
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.LaunchSplashActivity'
        desired_caps['noReset'] = True  # 这里的noreset设置为true，重启app的时候就不会清除登录信息
        desired_caps['skipDeviceInitialization'] = True
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        # desired_caps['settings[waitForIdleTimeout]'] = 0
        desired_caps['skipServerInstallation'] = True
        # 使用appium自动启动指定的模拟器
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)
        return self  #这句很关键，调用start之后，又返回到app了，所以可以链式调用：self.app = App()；# self.main = self.app.start().goto_main()

    def restart(self):
        # 重启app
        pass

    def stop(self):
        # 停止app
        sleep(3)
        self.driver.quit()

    # 这里加个箭头表示返回值的类型提示，可以联想出mainpage页的一些方法
    def goto_main(self)->MainPage:
        # 进入到首页
        return MainPage(self.driver)