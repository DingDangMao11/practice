# -*- coding:utf-8 -*-

import xlsxwriter
# 创建一个excel
workbook = xlsxwriter.Workbook("result1.xlsx")
# 创建一个sheet
worksheet = workbook.add_worksheet()
# 自定义样式，加粗
bold = workbook.add_format({'bold': 1})
# --------1、准备数据并写入excel---------------
# 向excel中写入数据，建立图标时要用到
headings = ['TIME(s)', 'VOLTAGE_NOW(uV)']
data = [
    ['0',   '5',   '10',  '16',  '21',
     '26',  '32',  '38',  '44',  '49',
     '54',  '59',  '65',  '70',  '75',
     '81',  '87',  '92',  '97',  '103',
     '109', '114', '119', '125', '130'],
    [3712148, 3643789, 3803945, 3676748, 3844716,
     3938222, 3951405, 3962392, 3964101, 3968495,
     3973866, 3977040, 3980214, 3981923, 3983632,
     3984853, 3986073, 3987538, 3988271, 3989247,
     3989735, 3990956, 3990956, 3991689, 3993642, ],
]

# 写入表头
worksheet.write_row('A1', headings, bold)

# 写入数据
worksheet.write_column('A2', data[0])
worksheet.write_column('B2', data[1])

# --------2、生成图表并插入到excel---------------
# 创建一个柱状图(line chart)
chart_col = workbook.add_chart({'type': 'line'})

# 配置第一个系列数据
chart_col.add_series({
    # 这里的sheet1是默认的值，因为我们在新建sheet时没有指定sheet名
    'name': '=Sheet1!$B$1',
    'categories': '=Sheet1!$A$2:$A$26',
    'values':   '=Sheet1!$B$2:$B$26',
    'line': {'color': 'red'},
})

# 设置图表的title 和 x，y轴信息
chart_col.set_title({'name': 'Voltage change diagram'})
chart_col.set_x_axis({'name': 'Time(s)'})
chart_col.set_y_axis({'name':  'VOLTAGE_NOW(uV)'})

# 设置图表的风格
chart_col.set_style(1)

# 把图表插入到worksheet并设置偏移
worksheet.insert_chart('B2', chart_col, {'x_offset': 25, 'y_offset': 10})

workbook.close()
