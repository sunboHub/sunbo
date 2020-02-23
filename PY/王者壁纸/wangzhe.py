import requests
import re
import os
import urllib

def wang():
    url = 'https://pvp.qq.com/web201605/herolist.shtml'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
    }
    req = requests.get(url, headers=headers)
    req.encoding = req.apparent_encoding
    regular1 = re.compile('a href="herodetail/(.*?).shtml')
    regular2 = re.compile('alt="(.*?)">')

    result1 = re.findall(regular1, req.text)
    result2 = re.findall(regular2, req.text)
    print(result1)
    print(result2)
    for num in result1:
        a = result1.index(num)
        print(result2[a])
        os.mkdir(f'C:\\Users\Administrator\Desktop\wang\{result2[a]}')
        for b in range(1, 8):
            try:
                b = str(b)
                path = f'C:\\Users\Administrator\Desktop\wang\{result2[a]}\{result2[a]}-{b}.jpg'
                url_jpg = f'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{num}/{num}-bigskin-{b}.jpg'
                # data = requests.get(url_jpg).content
                # with open(path,'wb') as f:
                #     f.write(data)
                urllib.request.urlretrieve(url_jpg, filename=path)
            except:
                continue
            else:
                print(f'{result2[a]}{b} --> {url_jpg}')
wang()
