from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from PythonCode.Web8.base import Base


class TestFile(Base):
    def test_file_upload(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element(By.XPATH, '//*[@class = "st_camera_off"]').click()
        self.driver.find_element_by_id("stfile").send_keys("E:\Learning\ComputerScience\charleslogo.jpg")
        sleep(3)

    def test_alert(self):
        """
        打开网页：https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable
        操作窗口右侧页面，将元素1拖拽到元素2
        此时会有一个alert弹窗，点击弹框中的确定
        按：点击运行
        关闭网页
        :return:
        """
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")

        drag = self.driver.find_element(By.CSS_SELECTOR, '#draggable')
        drop = self.driver.find_element(By.CSS_SELECTOR, '#droppable')
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop).perform()

        sleep(3)
        print("点击alert 确认")
        self.driver.switch_to.alert.accept()
        sleep(3)

        self.driver.switch_to.parent_frame()
        self.driver.find_element(By.CSS_SELECTOR, '#submitBTN').click()
        sleep(3)
