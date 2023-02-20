from _ast import Assert

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

desired_cap = {
    "deviceName": "sdk_gphone64_x86_64",
    "uid": "emulator-5554",
    "platformName": "Android",
    "platformVersion": "12",
    "appPackage": "com.google.android.calculator",
    "appActivity": "com.android.calculator2.Calculator",
    "app": "D:\\GIT\\appium-tutorial\\Calculator.apk"
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)

# older versions
# driver.find_element_by_id("com.google.android.calculator:id/digit_7").click()

# number7 = driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/digit_7")
# number7.click()

driver.find_element(AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='7']").click()

driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/op_add").click()

driver.find_element(AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='7']").click()

# driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/eq").click()

result_preview = driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/result_preview")
result_text = result_preview.text
print(result_text)

#driver.quit()
