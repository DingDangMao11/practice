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

count = 0
while (count < 1):
    os.system("adb wait-for-device root")
    os.system("adb wait-for-device shell sleep 3s")
    os.system("adb wait-for-device shell am start -a android.intent.action.MAIN -n com.android.settings/.MainSettings")
    os.system("adb shell input swipe 500 1000 500 500")

    # result = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.TextView")
    # result = driver.find_elements_by_image('./lock.png')
    result = driver.find_element_by_android_uiautomator('text(\"锁屏、密码和指纹\")')

    if result:
        print result
        print '有*锁屏、密码和指纹*选项'
    else:
        print "!!!没找到指纹选项!!!"
    driver.quit()
    os.system("adb reboot")
    time.sleep(20)
    os.system("adb wait-for-device")
    count = count + 1

print "done !"
