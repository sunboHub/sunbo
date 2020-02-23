import xlwt
new_network = xlwt.Workbook()
worksheet = new_network.add_sheet('第一个表')
worksheet.write(0,0,'东西1')
worksheet.write(0,1,'东西2')
new_network.save('E:/PYTHON-Test-Excel/SAVE/新工作簿.xls')
