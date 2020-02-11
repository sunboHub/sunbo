import requests
import re
import os
import urllib
import time


def wang():
    url = 'https://pvp.qq.com/web201605/herolist.shtml'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
    }
    req = requests.get(url,headers=headers)
    req.encoding = req.apparent_encoding
    regular1 = re.compile('a href="herodetail/(.*?).shtml')
    regular2 = re.compile('alt="(.*?)">')

    result1 = re.findall(regular1,req.text)
    result2 = re.findall(regular2,req.text)
    print(result1)
    print(result2)
    a = 0
    for num in result1:
        print(result2[a])
        for b in range(1,8):
            try:
                b = str(b)
                path = os.path.join(WW, result2[a] + b +'.jpg')
                time.sleep(0)
                print('http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/'+num+'/'+num+'-bigskin-'+b+'.jpg')
                urllib.request.urlretrieve('http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/'+num+'/'+num+'-bigskin-'+b+'.jpg',filename=path)
            except:
                continue
        a += 1
WW = r"C:\\Users\Administrator\Desktop\wangz"


wang()











