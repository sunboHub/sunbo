# 数据增加
# append()  在列表末尾增加数据，增加的为序列
# extend()  在列表末尾增加数据，增加的为单个
# insert()  在指定位置增加

# 格式
# 在末尾加
list1 = [1,2,3,4]

list1.append([5,6,7])
print(list1)

list1.extend([8,9,10])
print(list1)

# 指定位置加

list1.insert(2,'我加')
list1.insert(4,'我再加')
print(list1)

# 数据删除
# del   删除列表，删除指定数据
# pop   删除指定下标数据（默认最后一个）
# remove  移除列表中某个数据的第一个匹配项
# clear   清空列表

# del
list2 = [1,2,3,4,4,5,6]
print(list2)

del list2[1]

print(list2)

# list3 = [1,2,3]
# del list3
# print(list3)


# pop
list2.pop(1)
print(list2)

# remove
list2.remove(4)
print(list2)

# clear
list2.clear()
print(list2)




# 数据修改

# 修改指定下标数据
# reverse()  逆置
# sort()     排序

# 直接改
list4 = [2,5,4,6,9,8,73]

list4[2] = 3
print(list4)

# 反过来 reverse()

list4.reverse()
print(list4)

# 排序 sort()

list4.sort()
print(list4)


# 复制  copy()

list5 = list4.copy()
print(list5)