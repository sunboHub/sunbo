import requests
import urllib
import os

url = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/513/513-bigskin-1.jpg'



# res = requests.get(url)
# res.encoding = res.apparent_encoding
# a = open('a.jpg','w')
# a.write(res.content)
path = os.path.join(r'E:\python-test\王者壁纸.py', 'A.jpg')
urllib.request.urlretrieve(url,filename=path)