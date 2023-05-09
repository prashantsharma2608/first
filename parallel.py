


import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib3
def setUp(self):
    # username: Username can be found at automation dashboard
    username="prashantsharma"
    # accessToken:  AccessToken can be generated from automation dashboard or profile section
    accessToken="nOt0r5Le5LhYZjrmZ6DpW4QvvXBXTCyG670NB1H02zr1ik9Zwh"
    # gridUrl: gridUrl can be found at automation dashboard
    gridUrl = "hub.lambdatest.com/wd/hub"

    desired_cap = {
        'platform' : "win10",
        'browserName' : "chrome",
        'version' :  "67.0",
        "resolution": "1024x768",
        "name": "LambdaTest python google search test ",
        "build": "LambdaTest python google search build",
        "network": True,
        "video": True,
        "visual": True,
        "console": True,
    }

    # URL: https://{username}:{accessToken}@hub.lambdatest.com/wd/hub
    url = "https://"+username+":"+accessToken+"@"+gridUrl

    print("Initiating remote driver on platform: "+desired_cap["platform"]+" browser: "+desired_cap["browserName"]+" version: "+desired_cap["version"])
    self.driver = webdriver.Remote(
        desired_capabilities=desired_cap,
        command_executor= url
    )



def test_search_in_google(self):
    driver = self.driver
    print("Driver initiated successfully.  Navigate url")
    driver.get("https://www.google.com/ncr")

    print("Searching lambdatest on google.com ")
    time.sleep(8)
    elem = driver.find_element_by_name("q")
    elem.send_keys("lambdatest.com")
    elem.submit()

    print("Printing title of current page :"+driver.title)
    driver.execute_script("lambda-status=passed")
    print("Requesting to mark test : pass")

def tearDown(self):
    self.driver.quit()

if __name__ == "__main__":
unittest.main()