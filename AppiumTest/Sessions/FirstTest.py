from appium import webdriver

desired_cap = {
  "deviceName": "sdk_gphone64_x86_64",
  "platformName": "Android",
  "app": "D:\\GIT\\appium-tutorial\\Calculator.apk"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)