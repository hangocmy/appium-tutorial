from datetime import time

from appium import webdriver

desired_caps = {
  "appium:deviceName": "Galaxy J7 Pro",
  "platformName": "Android",
  "appium:platformVersion": "9",
  "appium:automationName": "uiautomator2",
  "appium:appPackage": "com.android.chrome",
}

driver = webdriver.Remote('http://127.0.0.1:4723', desired_caps)

driver.get("https://google.com")
print(driver.title)

time.sleep(2)
driver.quit()