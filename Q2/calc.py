# coding:utf-8

from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.1'
desired_caps['deviceName'] = 'e2939b32'
desired_caps['appPackage'] = 'com.miui.calculator'
desired_caps['appActivity'] = 'com.miui.calculator.cal.CalculatorActivity'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

driver.find_element_by_id("btn_1_s").click()
driver.find_element_by_id("btn_3_s").click()
driver.find_element_by_id("btn_5_s").click()
driver.find_element_by_id("btn_7_s").click()
driver.find_element_by_id("btn_9_s").click()
driver.find_element_by_id("btn_plus_s").click()
driver.find_element_by_id("btn_1_s").click()
driver.find_element_by_id("btn_equal_s").click()
print "done !"
driver.quit()
