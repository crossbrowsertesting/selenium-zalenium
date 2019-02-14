import unittest
from selenium import webdriver
import requests, time
import os


class SeleniumCBT(unittest.TestCase):
    def setUp(self):
        self.username = "YOUR_USERNAME"
        self.authkey  = "YOUR_AUTHKEY"
        caps = {}
        caps['name'] = 'Zalenium Test'
        caps['browserName'] = 'Chrome'
        caps['version'] = '72'
        caps['platform'] = 'Windows 10'
        caps['screenResolution'] = '1366x768'
        caps['record_video'] = 'true'

        try:
            self.driver = webdriver.Remote(
            desired_capabilities = caps,
            #command_executor = "http://localhost:4444/wd/hub")
            command_executor="http://%s:%s@hub.crossbrowsertesting.com:80/wd/hub"%(self.username, self.authkey))
            

        except Exception as e:
            raise e

    def test_CBT(self):
        self.driver.get("http://crossbrowsertesting.github.io/login-form.html")
        self.driver.find_element_by_xpath("//*[@id=\"username\"]").send_keys("tester@crossbrowsertesting.com")
        self.driver.find_element_by_xpath("//*[@type=\"password\"]").send_keys("test123")
        self.driver.find_element_by_xpath("//*[@id=\"submit\"]").click()

        print("The title is ", self.driver.title)
        time.sleep(10)

        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

