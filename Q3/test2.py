import xlrd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from pylab import *

from datetime import date, datetime


def read_excel():
    # 打开文件
    workbook = xlrd.open_workbook(r'SOCdata1.xlsx.xlsx')
    # 获取所有sheet
    # print(workbook.sheet_names()) # [u'sheet1', u'sheet2']
    # 根据sheet索引或者名称获取sheet内容
    sheet1 = workbook.sheet_by_index(0)  # sheet索引从0开始
    # sheet的名称，行数，列数
    # print(sheet1.name,sheet1.nrows,sheet1.ncols)
    # 获取整行和整列的值（数组）
    rows = sheet1.row_values(0)
    cols4 = sheet1.col_values(4)  # 获取第四行内容
    cols3 = sheet1.col_values(3)  # 获取第三列内容
    cols2 = sheet1.col_values(2)
    cols1 = sheet1.col_values(1)
    cols0 = sheet1.col_values(0)

    dic = {}  # 采用数据字典统计文章类型数目
    for item in cols0:
        if item in dic.keys():
            dic[item] += 1
        else:
            dic[item] = 1
    a = []
    b = []
    for key in dic:
        a.append(key)
        b.append(dic[key])
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文标签
    size = []
    t = sum(b)  # 统计总的发表篇幅
    label = a
    # 计算每种类型所占的比例
    for u in b:
        i = u / t
        size.append(i)
        plt.plot(size)
    plt.title('文章类型比例图')
    plt.pie(size, labels=label, colors="rgb", autopct='%1.lf%%', shadow=True, startangle=90)
    # plt.axis('equal')
    plt.show()


if __name__ == '__main__':
    read_excel()
