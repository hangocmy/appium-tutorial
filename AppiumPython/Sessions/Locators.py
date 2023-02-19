from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


desired_cap = {
  "deviceName": "sdk_gphone64_x86_64",
  "uid": "emulator-5554",
  "platformName": "Android",
  "platformVersion": "12",
  "appPackage": "com.google.android.calculator",
  "appActivity": "com.android.calculator2.Calculator",
  "app": "E:\\GIT\\appium-tutorial\\Calculator.apk"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)

#older versions
#driver.find_element_by_id("com.google.android.calculator:id/digit_7").click()

# number7 = driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/digit_7")
# number7.click()

driver.find_element(AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='7']").click()
