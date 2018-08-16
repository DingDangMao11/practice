# -*- coding:utf-8 -*-

import xlsxwriter
import xlrd

# 创建结果输出excel
workbook = xlsxwriter.Workbook("result2.xlsx")
worksheet = workbook.add_worksheet()

# 打开数据源, 获取内容
data = xlrd.open_workbook('SOCdata1.xlsx')
table = data.sheets()[0]
data1 = xlrd.open_workbook('SOCdata2.xlsx')
table1 = data1.sheets()[0]

# 写入数据
worksheet.write_column('A1', table.col_values(0))
worksheet.write_column('B1', table.col_values(3))
worksheet.write_column('A27', table1.col_values(0)[1:])
worksheet.write_column('B27', table1.col_values(3)[1:])
# 创建一个柱状图(line chart)
chart_col = workbook.add_chart({'type': 'line'})

# 配置第一个系列数据
chart_col.add_series({
    # 这里的sheet1是默认的值，因为我们在新建sheet时没有指定sheet名
    'name': '=Sheet1!$B$1',
    'categories': '=Sheet1!$A$2:$A$51',
    'values':   '=Sheet1!$B$2:$B$51',
    'line': {'color': 'red'},
})

# 设置图表的title 和 x，y轴信息
chart_col.set_title({'name': 'Voltage change diagram'})
chart_col.set_x_axis({'name': 'Time(s)'})
chart_col.set_y_axis({'name':  'VOLTAGE_NOW(uV)'})

# 设置图表的风格
chart_col.set_style(1)

# 把图表插入到worksheet并设置偏移
worksheet.insert_chart('B2', chart_col, {'x_offset': 40, 'y_offset': 18})
workbook.close()
