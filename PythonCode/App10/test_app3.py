from appium import webdriver
from selenium.webdriver.common.by import By


class TestWXMicro():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = "android"
        desired_caps['deviceName'] = ""
        desired_caps['appPackage'] = "com.tencent.mm"
        desired_caps['appActicity'] = "com.tencent.mm.ui.LauncherUI"
        desired_caps['noReset'] = True
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        # desired_caps['chromedriverExecutable'] =
        desired_caps['chromedriverExecutableDir'] = "E:/Learning/ComputerScience/SoftwareTesting/Hogwarts/driver"
        desired_caps['chromeOptions'] = {
            'androidProcess': 'com.tencent.mm:appbrand0'
        }
        desired_caps['adbPort'] = 5038
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.XPATH, "//*[@text='通讯录']")
        self.driver.implicitly_wait(10)

    def test_search(self):
