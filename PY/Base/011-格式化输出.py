age = 20
name = 'TOM'
weight = 60.03
stu_ID = 11


# %d %s %f

# 1.我今年X岁了---%d(int)
print('我今年%d岁了' % age)

# 2.我的名字叫X---%s(str)
print('我的名字叫%s' % name)

# 3.我的体重是X公斤---%f(float)--2f--保留两位
print('我的体重是%.2f公斤' % weight)

# 4.我的学号是X---%d(int)
print('我的学号是%d' % stu_ID)
# 4.1.我的学号是010--不足3位用0补充--超出原位输出
print('我的学号是%03d' % stu_ID)

# 5.我今年X岁了,体重X公斤，学号是X
print('我明年%d岁了,体重%.2f公斤，学号是%03d' % (age + 1,weight,stu_ID))

# f'{}'
print(f'我今年{age}岁了,体重{weight}公斤，学号是{stu_ID}')