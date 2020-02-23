# dict 字典(无序的)
# 键：值
d = {"name": "Tom", "Age": 18, "is Student": True}

li = [{"name": "Tom", "Age": 18, "is Student": True}, {"name": "Bob", "Age": 28, "is Student": False}]

# 找
print(d["Age"])
print(d.get("Age"))

print(li[1]["name"])
# 增
d["sex"] = "男"
print(d)
# 改
d["Age"] = 19
print(d)
# 删
d.pop("name")
print(d)

# set(无序的，不可重复)
s1 = set([1, 2, 3, 4])
s2 = set([2, 3, 4, 5])
# 并集
s = s1 | s2
print(s)
# 交集
s = s1 & s2
print(s)
# 添加
s.add(8)
print(s)
# 移除
s.remove(2)
print(s)
# 清空
s.clear()
print(s)
