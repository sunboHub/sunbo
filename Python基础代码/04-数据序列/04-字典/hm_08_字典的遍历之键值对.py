dict1 = {'name': 'TOM', 'age': 20, 'gender': '男'}

for item in dict1.items():
    print(item)


# dict1.items()   结果是一个元组，

for key, value in dict1.items():
    # print(key)
    # print(value)
    # 目标： key=value
    print(f'{key}={value}')