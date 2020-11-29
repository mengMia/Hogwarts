from PythonCode.Web7.base import Base


class TestFrame(Base):
    """
    到frame下找一个元素，“请拖拽我”
    切出frame找另外一个元素，”点击运行“
    """
    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        # print(self.driver.find_element_by_id("draggable").text)
        # 到frame下找一个元素，“请拖拽我”
        self.driver.switch_to.frame("iframeResult")
        print(self.driver.find_element_by_id("draggable").text)

        # 切回原来的页面
        # self.driver.switch_to.parent_frame()
        self.driver.switch_to.default_content()
        print(self.driver.find_element_by_id("submitBTN").text)
