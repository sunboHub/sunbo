import requests
import re
import os
import urllib
import time


def shou():
    url = 'http://ow.blizzard.cn/heroes/#all'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
    }
    req = requests.get(url,headers=headers)
    req.encoding = req.apparent_encoding
    regular1 = re.compile('data-hero-id="(.*?)"')
    regular2 = re.compile('class="portrait-title">(.*?)</span></span>')

    result1 = re.findall(regular1,req.text)
    result2 = re.findall(regular2,req.text)
    print(result1)
    print(result2)
    a = 0
    for n in result1:
        
        try:
            print(result2[a])
            print(n)
            print('http://overwatch.nosdn.127.net/1/assets/images/hero/'+n+'/intro-video.mp4')
            time.sleep(0)
            path = os.path.join(WW, result2[a] +'.mp4')
            urllib.request.urlretrieve('http://overwatch.nosdn.127.net/1/assets/images/hero/'+n+'/intro-video.mp4',filename=path)
        except:
            continue
        a += 1
WW = r"C:\\Users\Administrator\Desktop\sou"

# shou()













