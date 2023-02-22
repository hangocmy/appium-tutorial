from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_cap = {
    "deviceName": "sdk_gphone64_x86_64",
    "uid": "emulator-5554",
    "platformName": "Android",
    "platformVersion": "12",
    "appium:automationName": "uiautomator2",
    "appPackage": "com.google.android.calculator",
    "appActivity": "com.android.calculator2.Calculator",
    "app": "D:\\GIT\\appium-tutorial\\Calculator.apk"
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)

# older versions
# driver.find_element_by_id("com.google.android.calculator:id/digit_7").click()

driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/digit_7").click()

driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/op_add").click()

driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/digit_7").click()

result_preview = driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/result_preview")
result_text = result_preview.text
print(result_text)

#driver.quit()
