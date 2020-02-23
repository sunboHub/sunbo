# 一、while

a = 0
while a < 5:
    print(a)
    a = a + 1

print('循环结束')

# 二、break(结束循环) 和 continue(结束本次循环，进入下次循环)

# 1. break(结束循环)
i = 1
while i < 5:
    if i == 3:
        print(f'吃了{i}个馒头吃饱了')
        break
    print(f'吃了第{i}个馒头')
    i += 1

# 2. continue(结束本次循环，进入下次循环)
q = 1
while q <= 5:
    if q == 3:
        print(f'第{q}个有虫子，不吃了')
        q += 1
        continue
    print(f'吃了第{q}个苹果')
    q += 1

# 三、while 的嵌套
j = 1
while j <= 4:
    k = 1
    while k <= 3:
        print(f'吃了第{k}顿饭')
        k += 1
    print(f'第{j}天过去了----------------------------------------')
    j += 1    
print('四天终于过完了，他妈的')

# 打印一个5*5
m = 1
while m <= 5:
    n = 1
    while n <= 5:
        print('@',end=' ')
        n += 1
    print()
    m += 1    
# 打印一个递增三角形
o = 1
while o <= 5:
    p = 1
    while p <= o:
        print('@',end='-')
        p += 1
    print()
    o += 1

# 打印一个递减三角形
o = 5
while o >= 1:
    p = 1
    while p <= o:
        print('@',end='-')
        p += 1
    print()
    o -= 1

# 打印乘法口诀表
r = 1
while r <= 9:
    s = 1
    while s <= r:
        print(f'{s}*{r}={r*s}',end='\t')
        s += 1
    print()
    r += 1

# while...else      else 后缩进的指循环正常结束后执行的代码
# 如果是break终⽌循环的情况，else下⽅缩进的代码将不执⾏
# 循环在continue控制下是可以正常结束的，当循环结束后，则执⾏else后缩进的代码


# for 临时变量 in 序列
a = [1, 2, 3, 4]
for v in a:
    print(v * 2)

li = [['1', '2', '3'], ['a', 'b' , 'c']]
for v in li:
    for k in v:
        print(k + 'ss')
