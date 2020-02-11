import requests
import hashlib,time
import random

def md5(word):
    word = word.encode()
    result = hashlib.md5(word)
    return result.hexdigest()
def youdao():
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    words = {'i': word,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': i,
            'sign':sign,
            'ts': r,
            'bv': t,
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
    return result.text



word = input('请输入单词:')
t = md5('5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36')
r = str(int(time.time()*1000))
i = r + str(random.randint(0,9))
sign = md5('fanyideskweb' + word + i + 'n%A-rKaT5fb[Gy?;N5@Tj')

# print(t)  # b396e111b686137a6ec711ea651ad37c
# print(r)
# print(i)
# print(sign)

# youdao()
a = youdao()
print(a)
