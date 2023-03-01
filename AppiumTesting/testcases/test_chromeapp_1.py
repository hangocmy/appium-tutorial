from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

desired_caps = {
    "appium:deviceName": "OPPO",
    "appium:uid": "OV6PEQ5PSGGEOBWW",
    "platformName": "Android",
    "appium:platformVersion": "10",
    "appium:ignoreHiddenApiPolicyError": "true",
    "appium:noReset": "true",
    "dontStopAppOnReset": "true",
    "appium:automationName": "UiAutomator2",
    "appium:appPackage": "com.android.chrome",
    "appium:appActivity": "com.google.android.apps.chrome.Main"
}
# dontStopAppOnReset: true
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
print(driver.capabilities)
driver.get('http://google.com')
driver.find_element(MobileBy.CLASS_NAME, 'android.widget.EditText').send_keys('Appium')
driver.find_element(MobileBy.ANDROID_UIAUTOMATOR('new UiSelector().text("Android"))'))

#driver.quit()
