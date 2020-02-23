import requests
import re

url = 'https://www.cmdy5.com/'
respone = requests.get(url)
respone.encoding = respone.apparent_encoding
regular = re.compile('<li><a href="(.*?)">(.*?)</a></li>')
result = re.findall(regular, respone.text)
list = []
for i in range(1,8):
    list.append(result[i][0])
list_1 = []


for a in list:
    list_1.append(a)
    index = a.rfind('.')
    post = a[0:index]
    postfix = a[index:]
    # print(post)
    # print(postfix)
    for c in range(2,400):
        new_address = post + '-' + str(c) + postfix
        list_1.append(new_address)

        

Big_list = []
for b in list_1:
    try:
        respone = requests.get(b)
        respone.encoding = respone.apparent_encoding
        regular = re.compile('<li class="p1 m1"><a class="link-hover" href="(.*?)" title="(.*?)">')
        result = re.findall(regular, respone.text)
        Big_list.extend(result)
        print(Big_list)
    except:
        continue
    # print(result)
    # print(respone.text)
# print(Big_list)



# https://www.cmdy5.com/dongzuopian-2.html






'https://www.cmdy5.com/play/38553.html?38553-1-1'