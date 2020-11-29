import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By



class TestWeiXinImport():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_weixin_import(self):
        """
        登录企业微信
        常用入口-导入通讯录
        上传文件
        断言文件上传成功
        """
        # 从数据库中取出cookie
        db = shelve.open("cookies")
        cookies = db['cookie']
        db.close()

        # 先不带入cookie信息打开企业微信
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")

        # 加入cookie
        for cookie in cookies:
            # 如果cookie里面的expiry有小数的话，可以通过以下两种方式处理
            # 方式一
            # if isinstance(cookie.get("expiry"), float):
            #     cookie["expiry"] = int(cookie["expiry"])
            # 方式二
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)

        # # 加入cookie之后打开企业微信
        # self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
        # 或者直接刷新一下当前页面，也可以完成登录的操作
        self.driver.refresh()

        # 找到导入联系人按钮，
        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(2)').click()
        # 上传文件
        self.driver.find_element(By.CSS_SELECTOR, '.ww_fileImporter_fileContainer_uploadInputMask').send_keys("E:\Learning\ComputerScience\contact.xlsx")
        # 验证文件名称
        filename = self.driver.find_element(By.CSS_SELECTOR, '.ww_fileImporter_fileContainer_fileNames').text
        # print(filename)
        assert filename == "contact.xlsx"
        sleep(3)


