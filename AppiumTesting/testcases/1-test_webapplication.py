from datetime import time

from appium import webdriver

desired_caps = dict(
    deviceName = 'sdk_gphone64_x86_64',
    uid = 'emulator-5554',
    platformName = 'Android',
    browserName = 'Chrome'
)

driver = webdriver.Remote('http://127.0.0.1:4723', desired_caps)

driver.get("https://google.com")
print(driver.title)
time.sleep(2)