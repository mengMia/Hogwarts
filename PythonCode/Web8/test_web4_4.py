import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# from Web8.base import Base


class TestShelve():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def test_shelve(self):
        """
        把cookies存到shelve数据库中，存完之后下面就可以注释掉了
        :return:
        """
        # cookies = [
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
        #      'value': '1688853129966621'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
        #      'value': '1688853129966621'},
        #     {'domain': '.qq.com', 'expiry': 1606632364, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
        #      'value': 'GA1.2.2135300826.1606545740'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
        #      'value': 'CV6C30zl8QL96nyDjNIBkbNz_NP8egdA2RadvQbUFvccjRJawbDIJ2zRELBKyfOT'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
        #      'value': 'a7774100'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1609138032, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
        #      'path': '/', 'secure': False, 'value': 'zh'},
        #     {'domain': '.qq.com', 'expiry': 1669617964, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
        #      'value': 'GA1.2.1202945471.1606545739'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
        #      'path': '/', 'secure': False, 'value': '1606545955'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
        #      'value': '3709789285253896'},
        #     {'domain': 'work.weixin.qq.com', 'expiry': 1606577274, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
        #      'secure': False, 'value': '607nu3f'},
        #     {'domain': '.qq.com', 'expiry': 1909567521, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/',
        #      'secure': False, 'value': '6b60e4eff9298e93'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1638081738, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
        #      'path': '/', 'secure': False, 'value': '0'},
        #     {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
        #      'value': '3TRkZl334i'},
        #     {'domain': '.qq.com', 'expiry': 1608003913, 'httpOnly': False, 'name': 'lskey', 'path': '/',
        #      'secure': False,
        #      'value': '00010000776fecf51d80c2fb9d2959db89674d40dbf38bca6b3cea0609a3fc575616a923475361bcb5994f8b'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1638081955, 'httpOnly': False,
        #      'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1606545739'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
        #      'value': '8MMuGXnHdwdpdnUNgEmraqeX069tbGwUXrQfL_LWHpbps32V37I1WWukzAsQaFLXNDCOv2NCKnBytmmTPbzZDFZpb_q85NSaJHrzdrJR4gabHcy04LmGP0yolROYQ_DpgONsjZWQZhaILnl6570edJzrU5nC7IgMTrf-Z3TeZu4KvBD2H3ZSthAAVlf0LuELD2IlHusyWkoC5SLuT-riLkZz4VhSSfN5EldM4TN1okIC3pZyngadzmoUH4RijAn9bHHRplsS2Rn2KxmWCmDYOw'},
        #     {'domain': '.qq.com', 'expiry': 1920546345, 'httpOnly': False, 'name': 'pac_uid', 'path': '/',
        #      'secure': False, 'value': '1_2993786681'},
        #     {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/',
        #      'secure': False, 'value': '2993786681'},
        #     {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
        #      'value': '37cef6b0887ef79b4be22279c86ee54aea464286da1dbdc4b703ed802da79420'},
        #     {'domain': '.qq.com', 'expiry': 1608003913, 'httpOnly': False, 'name': 'luin', 'path': '/', 'secure': False,
        #      'value': 'o2993786681'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
        #      'value': '1970325055200623'},
        #     {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
        #      'secure': False, 'value': '4780375100'},
        #     {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
        #      'secure': False, 'value': '5380769792'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
        #      'value': '1'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
        #      'value': 'direct'}]
        # db = shelve.open("cookies")
        # db['cookie'] = cookies
        # db.close()
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
        self.driver.find_element(By.CSS_SELECTOR, '.ww_fileImporter_fileContainer_uploadInputMask').send_keys(
            "E:\Learning\ComputerScience\contact.xlsx")
        # 验证文件名称
        filename = self.driver.find_element(By.CSS_SELECTOR, '.ww_fileImporter_fileContainer_fileNames').text
        # print(filename)
        assert filename == "contact.xlsx"
        sleep(3)
