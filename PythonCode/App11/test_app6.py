from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestContact():
    def setup_class(self):
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

    # 设为类级别的，只销毁一次就行了
    def teardown_class(self):
        sleep(3)
        self.driver.quit()

    """
    企业微信app，删除联系人
    1.通讯录页面搜索要删除的联系人
    2.一步步删除联系人
    3.回到搜索页面，查找之前要删除的联系人是否还存在
    """
    def test_contact(self):
        name = "测试101"

        # 点击通讯录tab按钮
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        # 点击搜索按钮
        self.driver.find_element(MobileBy.XPATH, '//*[@text="微信测试"]/../../../../../android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.TextView')\
            .click()
        # 输入搜索内容
        self.driver.find_element(MobileBy.XPATH, '//*[@text="搜索"]').send_keys(name)
        # 点击联系人
        self.driver.find_element(MobileBy.XPATH, f'//*[@text="{name}" and @clickable = "false"]').click()
        # 点击进入设置页面
        self.driver.find_element(MobileBy.XPATH, '//*[@text="个人信息"]/../../../../../android.widget.LinearLayout[2]').click()
        # 点击编辑成员
        self.driver.find_element(MobileBy.XPATH, '//*[@text="编辑成员"]').click()
        # 点击删除成员
        self.driver.find_element(MobileBy.XPATH, '//*[@text = "删除成员"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text = "确定"]').click()

        # assert不知道怎么写

