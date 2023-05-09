from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

username = "prashantsharma"
accessToken = "FnWOBgCsWRSsSLTkXpYaaYAqlMeX1Ecnjh2VlgnRIFglW1hzDG"

ch_capability = {
	'LT:Options': {
		"username": "prashantsharma",
		"accessKey": "FnWOBgCsWRSsSLTkXpYaaYAqlMeX1Ecnjh2VlgnRIFglW1hzDG",
		"platformName": "Windows 10",
		"build": "parallel",
		"project": "parallel"
	},
    "browserName": "Chrome",
	"browserVersion": "112.0",
}
url = "https://" + username + ":" + accessToken + "@hub.lambdatest.com/wd/hub"
driver1 = webdriver.Remote(
    command_executor=url,
    desired_capabilities=ch_capability
)

capability = {
	"browserName": "Firefox",
	"browserVersion": "112.0",
	"LT:Options": {
		"username": "prashantsharma",
		"accessKey": "FnWOBgCsWRSsSLTkXpYaaYAqlMeX1Ecnjh2VlgnRIFglW1hzDG",
		"platformName": "Windows 10",
		"build": "parallel",
		"project": "parallel"
	}
}
url = "https://" + username + ":" + accessToken + "@hub.lambdatest.com/wd/hub"
driver2 = webdriver.Remote(
    command_executor=url,
    desired_capabilities=capability
)
Username = "prashantsharma@lambdatest.com"
pd = "aARUSH@123"
Url = "https://accounts.lambdatest.com/login"
driver2.get(Url)

uname = driver2.find_element("id", "email")
uname.send_keys(Username)
password = driver2.find_element("id", "password")
password.send_keys(pd)
driver2.find_element("id", "login-button").click()
time.sleep(1)
driver2.quit()