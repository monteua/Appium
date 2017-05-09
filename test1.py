import appium
import unittest

class SimpleTest(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['browserName'] = 'Browser'

        self.driver = appium.webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def testOpenPage(self):
        self.driver.get('https://en.wikipedia.org')
        text = self.driver.find_element_by_xpath('//div/h2').text
        self.assertEquals(text, "Today's featured article")


if __name__ == '__main__':
    unittest.main()
