from time import sleep

import yaml
from appium import webdriver

from PythonCode.App11.deleteContact_PO.page.base_page import BasePage
from PythonCode.App11.deleteContact_PO.page.main_page import MainPage

with open('../datas/caps.yaml') as f:
    myconfig = yaml.safe_load(f)
    desired_caps = myconfig['desirecaps']
    ip = myconfig['server']['ip']
    port = myconfig['server']['port']


class App(BasePage):
    def start(self):
        if self.driver == None:
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
            # # desired_caps['settings[waitForIdleTimeout]'] = 0
            # desired_caps['skipServerInstallation'] = True
            self.driver = webdriver.Remote(f"http://{ip}:{port}/wd/hub", desired_caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver.launch_app()
        return self

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        sleep(3)
        self.driver.quit()

    def goto_main(self)->MainPage:
        # 进入到首页
        return MainPage(self.driver)