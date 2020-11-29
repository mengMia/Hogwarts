from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from PythonCode.Web8.test_web5_2_podemo.page.add_member_page import AddMemberPage
from PythonCode.Web8.test_web5_2_podemo.page.base_page import BasePage


class MainPage(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    # 放在基类里面
    # def __init__(self):
    #     options = Options()
    #     options.debugger_address = '127.0.0.1:9222'
    #     self.driver = webdriver.Chrome(options=options)
    #     self.driver.implicitly_wait(3)
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    # 首页点击添加联系人，直接进入添加页面
    def goto_addmember(self):
        # 点击添加联系人
        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)').click()  #拥有相同父节点的，并且属性值为xx的第一个元素
        # 返回一个添加联系人页面
        return AddMemberPage(self.driver)

    # 点击通讯录按钮，进入通讯录页面，点击添加成员按钮，进入添加页面
    def goto_contact_member(self):
        # 点击通讯录
        self.driver.find_element(By.CSS_SELECTOR, '#menu_contacts > span').click()
        sleep(2)
        # 点击添加成员按钮
        self.driver.find_element(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)').click()

        # 返回通讯录页面,添加联系人
        return AddMemberPage(self.driver)