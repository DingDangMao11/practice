# coding:utf-8
import os
import time

from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = ''
desired_caps['deviceName'] = 'e2939b32'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = 'com.android.settings.MainSettings'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

os.system("adb wait-for-device root")
os.system("adb wait-for-device shell sleep 3s")
os.system("adb wait-for-device shell am start -a android.intent.action.MAIN -n com.android.settings/.MainSettings")
os.system("adb shell input swipe 500 1000 500 500")

try:
    result = driver.find_element_by_android_uiautomator('text(\"锁屏、密码和指纹\")')
    print result
    print '有 *锁屏、密码和指纹* 选项'
except Exception as e:
    print e
    print "!!!没找到指纹选项!!!"
driver.quit()
# os.system("adb reboot")
# time.sleep(20)
# os.system("adb wait-for-device")


