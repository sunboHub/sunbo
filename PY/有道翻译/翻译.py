import tkinter as t
import requests
import hashlib
import time
import random
import re

def md5(word):
    word = word.encode()
    result = hashlib.md5(word)
    return result.hexdigest()
def youdao():
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    word = e1.get()
    p = md5('5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36')
    r = str(int(time.time() * 1000))
    i = r + str(random.randint(0, 9))
    sign = md5('fanyideskweb' + word + i + 'n%A-rKaT5fb[Gy?;N5@Tj')
    words = {'i': word,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': i,
            'sign':sign,
            'ts': r,
            'bv': p,
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_CLICKBUTTION'}
    headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'OUTFOX_SEARCH_USER_ID=-1908424474@10.108.160.17; JSESSIONID=aaacA5MfRi17B4U-Az8_w; OUTFOX_SEARCH_USER_ID_NCOO=2100063124.1301084; ___rl__test__cookies=1579413912095',
            'Host': 'fanyi.youdao.com',
            'Referer': 'http://fanyi.youdao.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    result = requests.post(url,data=words,headers=headers)
    regular = re.compile('{"tgt":"(.*?)","src":"(.*?)"}')
    res = re.findall(regular, result.text)
    print(result.text)
    text.insert(t.END, res[0])
    text.see(t.END)
    text.update()



# 控件
root = t.Tk()
# 窗口大小
root.geometry('245x360')

root.title('有道翻译')

r0 = t.Label(root,text = '输入单词:',font = 15)
r0.grid(row = 0,column = 0)
# 输入框
e1 = t.Entry(root,font = 22)
e1.grid(row = 0,column = 1)


# 列表框
text = t.Listbox(root,font = ('微软雅黑',15),width = 20,height = 10)
text.grid(row = 2, columnspan = 2)

# 按钮
a1 = t.Button(root,text = '翻译',font = 12,command = youdao)#,command = readpass
a1.grid(row = 3,columnspan = 2)
root.mainloop()



# print(t)  # b396e111b686137a6ec711ea651ad37c
# print(r)
# print(i)
# print(sign)

# youdao()
# a = youdao()
# print(a)
