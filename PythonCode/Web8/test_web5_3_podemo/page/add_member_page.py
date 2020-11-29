from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from PythonCode.Web8.test_web5_3_podemo.page.base_page import BasePage


class AddMemberPage(BasePage):
    # def __init__(self, driver: WebDriver):
    #     self.driver = driver

    # 添加联系人
    def add_member(self, username, account, phonenum):
        self.find(By.ID, "username").send_keys(username)
        self.find(By.ID, "memberAdd_acctid").send_keys(account)
        self.find(By.ID, "memberAdd_phone").send_keys(phonenum)
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        # 保存之后会跳回到通讯录页面，此时需要一个等待来确保跳回了通讯录页面，然后才能进行断言本次添加的联系人是否在列表中
        # 强制等待2s
        # sleep(2)

        # 显示等待
        checkbox = (By.CSS_SELECTOR, ".ww_checkbox")
        self.wait_for_click(checkbox)
        return True

    # 验证联系人是否添加成功
    def get_member(self, value):
        # # 这里只获取到了首页的联系人列表
        # contactlist = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        # # 列表推导式
        # titlelist = [element.get_attribute("title") for element in contactlist]
        # return titlelist


        # 获取所有页面的联系人
        total_list = []
        while True:
            contactlist = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
            titlelist = [element.get_attribute("title") for element in contactlist]
            # 如果在当前页面已经找到了，就不用往下一页翻了
            if value in titlelist:
                return titlelist
            total_list = total_list + titlelist
            result: str = self.find(By.CSS_SELECTOR, '.ww_pageNav_info_text').text
            num, total = result.split('/', 1)
            if int(num) == int(total):
                break
            else:
                self.find(By.CSS_SELECTOR, '.ww_commonImg_PageNavArrowRightNormal').click()
        return total_list