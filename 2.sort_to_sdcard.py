#!/usr/bin/python3
# -*- coding: UTF-8 -*- 
import os

def sorting():
    a = input("input:")
    b = input("input:")
    c = input("input:")

    list = [a,b,c]
    sorted(list)

    f = open('NameSorting.txt', 'w')
    f.writelines("\n".join(sorted(list)))
    f.close()
    
    shellcmd = "adb push NameSorting.txt /sdcard"
    os.system(shellcmd)

#主函数
if __name__=='__main__':
    sorting()





