# -*- coding:utf-8 -*-
import os

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

if __name__ == "__main__":
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '8.1'
    desired_caps['deviceName'] = 'e4d42545'
    desired_caps['unicodeKeyboard'] = 'true'
    desired_caps['resetKeyboard'] = 'true'
    desired_caps['app'] = 'com.miui.home'
    desired_caps['appActivity'] = '.launcher.Launcher'

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    print "Start driver success!"

    print "Trying to click browser icon"
    driver.find_element_by_android_uiautomator('text(\"Music\")').click()
    print "Finish clicking browser icon. The browser should be opened."

    driver.quit()
