from selenium import webdriver
from time import sleep
import time
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from threading import Thread
# This array 'caps' defines the capabilities browser, device and OS combinations where the test will run
username = "prashantsharma"
accessToken = "FnWOBgCsWRSsSLTkXpYaaYAqlMeX1Ecnjh2VlgnRIFglW1hzDG"
caps = [{
            "browserName": "Firefox",
            "browserVersion": "112.0",
            "LT:Options": {
                "username": "prashantsharma",
                "accessKey": "FnWOBgCsWRSsSLTkXpYaaYAqlMeX1Ecnjh2VlgnRIFglW1hzDG",
                "platformName": "Windows 10",
                "build": "parallel",
                "project": "parallel"
            }
},
       {
            "browserName": "Chrome",
            "browserVersion": "113.0",
            "LT:Options": {
                # "username": "prashantsharma",
                # "accessKey": "FnWOBgCsWRSsSLTkXpYaaYAqlMeX1Ecnjh2VlgnRIFglW1hzDG",
                "platformName": "Windows 10",
                "build": "parallel",
                "project": "parallel"
	       }
}
]

url = "https://" + username + ":" + accessToken + "@hub.lambdatest.com/wd/hub"
def run_session():
    driver = webdriver.Remote(
        command_executor=url,
        desired_capabilities=caps)

    sleep(5)
    Username = "prashantsharma@lambdatest.com"
    pd = "aARUSH@123"
    Url = "https://accounts.lambdatest.com/login"
    driver.get(Url)

    uname = driver.find_element("id", "email")
    uname.send_keys(Username)
    password = driver.find_element("id", "password")
    password.send_keys(pd)
    driver.find_element("id", "login-button").click()
    time.sleep(1)
    driver.quit()
# Stop the driver
# The Thread function takes run_session function and each set of capability from the caps array as an argument to run each session in parallel
for cap in caps:
    Thread(target=run_session, args=(cap,)).start()


pipeline {
    agent any

    stages {
        stage('test'){
            steps{
                git branch: 'main', url: 'https://github.com/prashantsharma2608/first.git'
            }
        }
        stage('Test'){
            steps{
                echo 'the job has been tested'
            }
        }
    }
}
node {
    withEnv(["LT_USERNAME=prashantsharma",
    "LT_ACCESS_KEY=qvitkAIKuMTkUYduwzBszg7OGoCl729DEDQY7NcVf33MhG5rG3",]){

   stage('setup') {

    try{
      git 'https://github.com/prashantsharma2608/first.git'
    }
    catch (err){
      echo err
   }

   }
   stage('build') {
      sh 'npm install'
    }

   stage('test') {
          try{
          sh './node_modules/.bin/nightwatch -e chrome,edge tests'
          }
          catch (err){
          echo err
          }
   }
   stage('end') {
     echo "Success"
     }
 }
}