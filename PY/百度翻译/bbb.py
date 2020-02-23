import requests
import os
def sou():
    url = 'http://www.baidu.com/'

    respone = requests.get(url)
    respone.encoding = respone.apparent_encoding
    
    return respone.text


a = sou()
f = open('12.html','w')
f.write(str(a))