from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Homework.Web8.test_web_podemo.page.add_member_page import AddMemberPage
from Homework.Web8.test_web_podemo.page.base_page import BasePage


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
        self.find(By.CSS_SELECTOR, '#menu_contacts > span').click()

        # 使用强制等待，使得添加成员按钮可点击
        # sleep(2)
        # self.find(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)').click()

        # # 使用显示等待，判断添加成员按钮可点击时等待结束，再进行click操作
        # # 获取添加成员按钮
        # locator = (By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)')
        # element = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        # element.click()

        # 封装该显示等待
        # 点击添加成员按钮
        # 这里有一个问题，采用显示等待之后，添加成员按钮点击了，但是没有跳转到输入页，感觉是页面加载速度的问题，如果强行加上sleep2秒或者人手动操作，就基本不会遇到这个问题，
        # locator = (By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)')
        # element = self.wait_for_click(locator)
        # element.click()

        # 点击添加成员按钮，有可能无法跳转到输入页，在这里加一个等待，如果找到输入页的某个元素，说明跳转成功，返回这个元素，否则反复点击多次，最后还没成功的话就抛出异常
        locator = (By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)')
        def wait_for_next(x:WebDriver):
            try:
                x.find_element(*locator).click()
                return x.find_element(By.ID, 'username')
            except:
                return False
        WebDriverWait(self.driver, 10).until(wait_for_next)

        # 返回通讯录页面,添加联系人
        return AddMemberPage(self.driver)