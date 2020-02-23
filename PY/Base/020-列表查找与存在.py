# index()    查找数据是否存在，存在为true，否则报错
# count()    查找数据出现次数
# len()      统计数据个数


list1 = ['YOM','LISA','MICAL']

print(list1.index('YOM',0,2))

print(list1.count('YOM'))

print(len(list1))


# in            判断存在
# not in        判断不存在


list2 = [1,2,3,4,5]

print(2 in list2)
print(2 not in list2)


num = int(input('请输入数字'))
if num in list2:
    print(f'您输入的数字是{num},已经存在')
else:
    print(f'您输入的数字是{num},不存在')
