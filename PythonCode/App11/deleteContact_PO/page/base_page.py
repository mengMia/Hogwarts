from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    # def find_and_click(self, by, locator):
    #     self.find(by, locator).click()

    def get_pagesource(self):
        return self.driver.page_source

