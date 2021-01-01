"""
app.py 模块，存放app相关的一些操作。
比如 启动应用，重启应用，停止应用，进入到首页
"""
from time import sleep

import yaml
from appium import webdriver

from PythonCode.App11.page.base_page import BasePage
from PythonCode.App11.page.main_page import MainPage


with open('../datas/caps.yml') as f:
    myconfig = yaml.safe_load(f)
    caps = myconfig['desirecaps']
    ip = myconfig['server']['ip']
    port = myconfig['server']['port']

class App(BasePage):
    def start(self):
        # app里面每次调用start方法的时候还会实例化一个driver，要想复用driver的话，需要加一个判断（因为给的默认值是None），
        # 在test_contact里面第一次调用start方法的时候，driver拥有了一个值，但是第二条测试用例再去调用start，还是会重新实例化一个driver，所以可以判断一下，如果已经有值了，就不进行实例化
        if self.driver == None:
            # 启动app
            # desired_caps = {}
            # desired_caps['platformName'] = 'Android'
            # desired_caps['platformVersion'] = '6.0'
            # desired_caps['deviceName'] = 'emulator-5554'
            # desired_caps['appPackage'] = 'com.tencent.wework'
            # desired_caps['appActivity'] = '.launch.LaunchSplashActivity'
            # desired_caps['noReset'] = True  # 这里的noreset设置为true，重启app的时候就不会清除登录信息
            # desired_caps['skipDeviceInitialization'] = True
            # desired_caps['unicodeKeyBoard'] = 'true'
            # desired_caps['resetKeyBoard'] = 'true'
            # desired_caps['skipServerInstallation'] = True
            self.driver = webdriver.Remote(f"http://{ip}:{port}/wd/hub", caps)
            self.driver.implicitly_wait(5)
        else:
            # 如果已经存在了，直接启动app,复用的逻辑
            # 这个launch_app是直接使用第一次实例化driver的时候定义的appPackage和appActivity
            self.driver.launch_app()
        return self  #这句很关键，调用start之后，又返回到app了，所以可以链式调用：self.app = App()；# self.main = self.app.start().goto_main()

    def restart(self):
        # 重启app
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        # 停止app
        sleep(3)
        self.driver.quit()

    # 这里加个箭头表示返回值的类型提示，可以联想出mainpage页的一些方法
    def goto_main(self)->MainPage:
        # 进入到首页
        return MainPage(self.driver)