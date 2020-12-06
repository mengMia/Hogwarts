from appium import webdriver

desire_cap={
  "platformName": "android",
  "deviceName": "127.0.0.1:7555",
  "appPackage": "com.xueqiu.android",
  "appActivity": ".view.WelcomeActivityAlias",
  "noReset": True  # 不对应用进行reset，比如弹窗，第一次弹出来关掉之后，设置这个参数，第二次打开就不会有弹窗了
}

# 和appium server创建连接
driver = webdriver.Remote("http://localhost:4723/wd/hub", desire_cap)
driver.implicitly_wait(10)
el1 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
el1.click()
el2 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el2.send_keys("生物")
el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView[1]")
el3.click()
