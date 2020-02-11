# 字符串的引号

a = 'I am TOM'

b = "I am TOM"

# 三引号可换行输出
c = '''I am
 TOM'''

d = 'I\'m TOM'

e = "I'm TOM"

print(c)
print(type(c))



# 字符串的下标或索引
# 默认分配是012345-----即是下标

str1 = 'abcdefg'

print(str1[0])

print(str1[3])


# 切片
# 项目名[起始:结束:步长]    包前不包后   前闭后开         是冒号：：：：

str2 = '0123456789'

print(str2[0:5])

print(str2[1:6:2])

print(str2[:])

print(str2[::-1])