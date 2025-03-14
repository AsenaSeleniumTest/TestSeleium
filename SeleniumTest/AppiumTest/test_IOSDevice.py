from Appium import webdriver
from Appium.webdriver.common.appiumby import AppiumBy

class TestBasePage:
    driver = None   
    APPIUM_SERVER_URL = "http://localhost:4723/wd/hub"
    capabilities = {
        "platformName": "iOS",
        "platformVersion": "18.3.1",
        "deviceName": "Ipad Pro",
        "udid": "auto",  
        "automationName": "XCUITest",
        "app": "/Users/Shared/Jenkins/Home/workspace/SeleniumTest/AppiumTest/Applications/BPBDemo.app"
    }
    def test_setup(self,driver_setup):
        self.driver = driver_setup