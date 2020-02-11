# 查找字符串起始位置

# 从左侧开始
# find()   未找到则返回-1
# index()  未找到则报错

# 从右侧开始
# rfind()
# rindex()

# 查找字符出现次数
# count()  未找到是0

# 格式    字符串名字.find(字串,开始下标,结束下标)

str = '1212255855215525'

print(str.find('5'))
print(str.find('5',7,10))
print(str.find('5',1,4))
print(str.rfind('5'))

print(str.index('5'))
# print(str.index('5',1,4))
print(str.rindex('5'))

print(str.count('5'))
print(str.count('0'))