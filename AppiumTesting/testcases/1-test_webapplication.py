from datetime import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

desired_caps = {
  "appium:deviceName": "OPPO",
  "appium:uid": "OV6PEQ5PSGGEOBWW",
  "platformName": "Android",
  "appium:platformVersion": "10",
  "appium:ignoreHiddenApiPolicyError": "true",
  "appium:noRetest": "true",
  "appium:automationName": "UiAutomator2",
  "appPackage": "com.idbeauty",
  "appActivity": "com.idbeauty.MainActivity"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
customer_code = driver.find_element(MobileBy.CLASS_NAME, "android.widget.EditText")
customer_code.clear()
customer_code.send_keys("Demo")
#driver.find_element(MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]").click();

time.sleep(2)
driver.quit()