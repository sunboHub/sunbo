import requests
import re
import os
import urllib
def TUTU():
    url = "http://search.yhd.com/c9719-0-0"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
    }
    req = requests.get(url,headers=headers)
  
    req.encoding = req.apparent_encoding

    regular = re.compile('<div style="position: relative">\n<img ((src)|(original))="//(.*?)(("/>)|(" />))')
    result = re.findall(regular,req.text)

   

    # print(result)
    num = 1
    for uuu in result:
        path = os.path.join(r'F:\\a', str(num) + '.jpg')
        # print(path)
        num += 1
        urllib.request.urlretrieve('http://' + uuu[3], filename=path)


TUTU()


