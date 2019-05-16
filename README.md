<h1><strong>Getting Started with Zalenium and CrossBrowserTesting</strong></h1>
<em>For this document, we provide example test located in our <a href="https://github.com/crossbrowsertesting/selenium-zalenium">Zalenium Github Repository</a>.</em>

Zalenium’s main goal is to allow anyone to have a disposable and flexible Selenium Grid infrastructure. A <a href="http://www.seleniumhq.org/docs/">Selenium</a> Grid that scales up and down dynamically with this solution based on <a href="https://github.com/elgalu/docker-selenium">docker-selenium</a> to run your tests is started in seconds. When you need a different browser, Zalenium  is easily integrated with the CrossBrowserTesting platform, so you can perform tests on a wide variety of OS/Device/Browser combinations, all from one test.
<h3>Let's walk through getting setup.</h3>
<strong>1.</strong> Start by installing <a href="https://docs.docker.com/install/">docker</a>, a standalone container image that includes everything needed to run an application: code, runtime, system tools, system libraries and settings.

<strong>2.</strong> Use docker to pull selenium and zalenium using the commands:
<pre><code>docker pull elgalu/selenium
docker pull dosel/zalenium
</code></pre>
<strong>3.</strong> Start Zalenium with the command:
<pre><code>
export CBT_USERNAME="YOUR_USERNAME"
export CBT_AUTHKEY="YOUR_AUTHKEY"
export CBT_HUB_URL= "http://hub.crossbrowsertesting.com:80/wd/hub"
docker run --rm -ti --name zalenium -p 4444:4444 \
-e CBT_USERNAME -e CBT_AUTHKEY -e CBT_HUB_URL \
-v /tmp/videos:/home/seluser/videos \
-v /var/run/docker.sock:/var/run/docker.sock \
--privileged dosel/zalenium start --cbtEnabled true
</code></pre>

<strong>4.</strong> Create an empty file called /zalenium/test/selenium_test.py with the following content:

<pre><code>
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
        caps['username']=self.username
        caps['password']=self.authkey

        try:
            self.driver = webdriver.Remote(
            desired_capabilities = caps,
            command_executor = "http://localhost:4444/wd/hub")    

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
</code></pre>
<strong>5.</strong>  Now you are ready to run your test using the command:
<pre><code>python selenium_test.py</code></pre>
<div class="blue-alert">You’ll need to use your Username and Authkey to run your tests on CrossBrowserTesting. To get yours, sign up for a <a href="https://crossbrowsertesting.com/freetrial"><b>free trial</b></a> or purchase a <a href="https://crossbrowsertesting.com/pricing"><b>plan</b></a>.</div>
As you can probably make out from our test, we visit a simple login page and display the title.

We kept it short and sweet for our purposes, but there is so much more you can do with Zalenium! Being built on top of Selenium means the sky is the limit as far as what you can do. If you have any questions or concerns, feel <a href="mailto:info@crossbrowsertesting.com">free to get in touch</a>.
