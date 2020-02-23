# replace()  替换
# split()   字符串分割为列表，分割字符会消失
# join()    列表中多个字符串合并为一个大字符串


# 格式   字符串.replace(旧子串,新子串,替换次数)
#        字符串.split(分割字符,分割字符出现次数num)       将返回num+1个
#        字符或子串.join(多字符串组成的序列)


# replace
str = '1111022220555506666'
new1 = str.replace('2','6')
new2 = str.replace('2','6',2)
print(new1)
print(new2)


# split
new3 = str.split('0')
new4 = str.split('0',2)
print(new3)
print(new4)


# join
list = ['11', '22','33','44']
new5 = '小狗'.join(list)
print(new5)