#!/usr/bin/python3
# -*- coding: UTF-8 -*- 
import os
import time
import xlwt

def fun_timer():


    f = open('data.txt', 'w')
    for m in range(5):
        a = os.system("adb shell date")
        f.writelines(str(a) + "\n")
        time.sleep(2)
    f.close()


#主函数
if __name__=='__main__':
    fun_timer()





