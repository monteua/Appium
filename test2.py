from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import unittest
from time import sleep

class AppTest(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'emulator-5554'
        #desired_caps['browserName'] = 'Browser'
        desired_caps['app'] = 'D:/programming/appium/test/Calculone.apk'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def testPress2(self):
        sleep(2)
        element = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.Calculone:id/button3")')
        element.click()
        element.click()
        element = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.Calculone:id/infoText")').text
        print (element)
        self.assertEquals(element, "88")

if __name__ == '__main__':
    unittest.main()
