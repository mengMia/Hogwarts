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
    企业微信app，点击通讯录，添加联系人,手动输入添加
    """
    def test_contact(self):
        name = "test4"
        gender = "男"
        phonenum = "13500000004"
        # 点击通讯录tab按钮
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        # 滚动查找“添加成员”按钮
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("添加成员").'
                                                        'instance(0))').click()
        # 点击”手动输入添加“
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()

        # 联系人表单

        # 输入姓名
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "姓名")]/../android.widget.EditText').send_keys(name)
        # 或者通过：//*[contains(@text, '姓名')]/../*[@text="必填"]来定位这个姓名的输入框

        # 选择性别
        self.driver.find_element(MobileBy.XPATH, '// *[contains( @ text, "性别")] /..// *[ @ text = "男"]').click()
        if gender == "男":
            # 这里需要加个显示等待，因为从上面一步定位的男，切换到下面再定位男，会有报错，
            WebDriverWait(self.driver, 10).until(lambda x : x.find_element(MobileBy.XPATH, '//*[@text="女"]'))
            self.driver.find_element(MobileBy.XPATH, '//*[@text="男"]').click()
        else:
            self.driver.find_element(MobileBy.XPATH, '//*[@text="女"]').click()

        # 输入手机号
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "手机") and contains(@class, "TextView")]/..//*[@text="手机号"]').send_keys(phonenum)

        # 点击保存
        self.driver.find_element(MobileBy.XPATH, '//*[@text="保存"]').click()

        # sleep(2)
        # print(self.driver.page_source) 需要等待2s才能抓取到toast
        # 添加断言
        text_toast = self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text   # 这里find_element方法会调用隐式等待，每隔0.5s去查找toast
        assert '添加成功' == text_toast


