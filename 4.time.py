#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import time
import xlwt
import subprocess

def fun_timer():

    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('local_time', cell_overwrite_ok=True)

    for i in range(5):
        # 读取手机本地时间
        out1 = subprocess.Popen("adb shell date", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        local_time = out1.stdout.readlines()
        local_time = str(local_time)
        local_time = local_time[3:-6]
        print(local_time)
        time.sleep(2)
        sheet.write(i, 0, str(local_time))
    book.save('local_time.xls')

#主函数
if __name__=='__main__':
    fun_timer()