
# f = open('E:\\3.txt','r')
# # for eachline in f:
# #     print(eachline)
# file = open('E:\\4.txt','a')
# while True:
#     c = f.readline()
#     file.write(c)
#     if not c:
#         break
# f.close()
# file.close()


# print(a[-1])

a = ['½啥意思','dafou']
file = open('E:\\2.txt','a')

for i in range(len(a)):
    try:
        s = str(a[i]) + '\n'
        file.write(s)
    except:
        continue
file.close()