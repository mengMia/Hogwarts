from time import sleep

from appium import webdriver

"""
雪球搜索框，
输入alibaba
点击搜索
"""
desired_caps={}
desired_caps['platformName']='Android'
desired_caps['platformVersion']='6.0'
desired_caps['deviceName']='emulator-5554'
desired_caps['appPackage']='com.xueqiu.android'
desired_caps['appActivity']='.view.WelcomeActivityAlias'
desired_caps['noReset']=True
desired_caps['dontStopAppOnReset']=True
desired_caps['skipDeviceInitialization']=True
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
driver.implicitly_wait(5)

driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
sleep(3)
driver.back() # 回到上一页
driver.back()