#!/usr/bin/python3
# -*- coding: UTF-8 -*- 
import os

def score():
    score = input("请输入分数:")
    if int(score) >= 90:
        print ('A')
    elif int(score) >= 60:
        print ('B')
    else:
        print ('C')

#主函数
if __name__=='__main__':
    score()





