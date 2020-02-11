import xlrd
# 打印某个单元格

# 打开工作簿
xlsx = xlrd.open_workbook('E:\PYTHON-Test-Excel\新材料学院97人.xlsx')
# 定位到工作表
table = xlsx.sheet_by_index(0)
# 打印出单元格(x+1,y+1)
print(table.cell(3,8).value)
