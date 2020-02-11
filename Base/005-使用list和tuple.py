# list 列表
li = [3231.23, 'hhhhh', 55, True, None]
# 打印全部
print(li)
# 打印第三个
print(li[3])
# 修改第三个为
li[3] = False
print(li)
# 在列表末尾添加7
li.append(7)
print(li)
# 把5554插入到第一个位置
li.insert(1, 5554)
print(li)
# 删除第0个
li.pop(0)
print(li)

length = len(li)
print(length)

# tuple 元组 (确定后不可更改)
tup = (231, '你好', 365.3)
a = (1,)
print(a)
