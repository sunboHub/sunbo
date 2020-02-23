# 位置参数
def hh(k, b):
    s = (k + 2) * (b + 3)
    return s


c = hh(5, 6)
print(c)

# 默认参数 默认b为0
def hh1(k, b=0):
    s = (k + 2) * (b + 3)
    return s

x = hh1(5)
print(x)

# 可变参数 元组(*num)
def sum111(*num):
    s = 0
    for j in num:
        s = s + j
    return s



w = sum111(1, 2, 4)
print(w)
