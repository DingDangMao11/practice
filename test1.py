#!/usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import xlrd
from xlrd import open_workbook

x_data = []
y_data = []
x_volte = []
temp = []
wb = open_workbook('SOCdata1.xlsx')

for s in wb.sheets():
    print 'Sheet:', s.name
    for row in range(s.nrows):
        print 'the row is:', row
        values = []
        for col in range(s.ncols):
            values.append(s.cell(row, col).value)
        print values
        x_data.append(values[0])
        y_data.append(values[1])
plt.plot(x_data, y_data, 'bo-', label=u"VOLTAGE_NOW", linewidth=1)
plt.title(u"VOLTAGE_NOW")
plt.legend()

plt.xlabel(u"Time/s")
plt.ylabel(u"VOLTAGE_NOW/μV")

plt.show()
print 'over!'
