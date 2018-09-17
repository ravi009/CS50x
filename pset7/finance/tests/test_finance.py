# flask run # in another tab
# xvfb-run python3 test_finance.py
import os, sys, time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
basedir = os.path.abspath(os.path.dirname(__file__))

import unittest
from application import app
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.keys import Keys

class TestFinance(unittest.TestCase):

    def setUp(self):
        opts = FirefoxOptions()
        opts.add_argument("--headless")
        self.driver = webdriver.Firefox(options=opts)

    def test_login(self):
        url = "https://edwd42-cs50-code42.c9users.io:8080"
        self.driver.get(url)
        # html = self.driver.page_source
        # print(html)
        # click the big red button to Open the App
        submit_button = self.driver.find_element_by_class_name("button")
        submit_button.click()
        time.sleep(2)
        print("27. sleeping for 2...")
        print("28. self.driver.title == " + self.driver.title)
        username = self.driver.find_element_by_id("username")
        time.sleep(1)
        username.send_keys("ee")
        password = self.driver.find_element_by_id("password")
        password.send_keys("dd")
        submit_button = self.driver.find_element_by_id("submit")
        submit_button.click()
        time.sleep(10)
        print("86. self.driver.title == " + self.driver.title)
        assert "C$50" in self.driver.title

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    # app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))
    unittest.main()
