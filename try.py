import pytest
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

# username = "prashantsharma"
# accessToken = "FnWOBgCsWRSsSLTkXpYaaYAqlMeX1Ecnjh2VlgnRIFglW1hzDG"
# url = "https://" + username + ":" + accessToken + "@hub.lambdatest.com/wd/hub"
gridUrl = "https://hub.lambdatest.com/wd/hub"
def driver_init_1():
    ch_options = ChromeOptions()
    ch_options.browser_version = "112.0"
    ch_options.platform_name = "Windows 11"
    lt_options = {}
    lt_options["username"] = "prashantsharma";
    lt_options["accessKey"] = "nOt0r5Le5LhYZjrmZ6DpW4QvvXBXTCyG670NB1H02zr1ik9Zwh";
    lt_options["build"] = "parallel"
    lt_options["project"] = "parallel"
    lt_options["w3c"] = True
    lt_options["plugin"] = "python-python"
    ch_options.set_capability('LT:Options', lt_options)


    driver = webdriver.Remote(
        command_executor=gridUrl,
        options=ch_options
    )
    Username = "prashantsharma@lambdatest.com"
    pd = "aARUSH@123"
    Url = "https://accounts.lambdatest.com/login"

    # driver = webdriver.Chrome()
    driver.get(Url)

    uname = driver.find_element("id", "email")
    uname.send_keys(Username)
    password = driver.find_element("id", "password")
    password.send_keys(pd)
    driver.find_element("id", "login-button").click()
    time.sleep(1)
    # request.cls.driver = driver
    # yield
    driver.close()
def driver_init_2():

    options = FirefoxOptions()
    options.browser_version = "112.0"
    options.platform_name = "Windows 11"
    lt_options = {}
    lt_options["username"] = "prashantsharma";
    lt_options["accessKey"] = "nOt0r5Le5LhYZjrmZ6DpW4QvvXBXTCyG670NB1H02zr1ik9Zwh";
    lt_options["build"] = "parallel"
    lt_options["project"] = "parallel"
    lt_options["w3c"] = True
    lt_options["plugin"] = "python-python"
    options.set_capability('LT:Options', lt_options)

    Username = "prashantsharma@lambdatest.com"
    pd = "aARUSH@123"
    Url = "https://accounts.lambdatest.com/login"

    # url = "https://" + username + ":" + accessToken + "@hub.lambdatest.com/wd/hub"
    driver = webdriver.Remote(
        command_executor=gridUrl,
        options=options
    )
    driver.get(Url)

    uname = driver.find_element("id", "email")
    uname.send_keys(Username)
    password = driver.find_element("id", "password")
    password.send_keys(pd)
    driver.find_element("id", "login-button").click()
    time.sleep(1)
    driver.quit()