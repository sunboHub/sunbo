import get_urlList
import urllib
import os
wangzhe = get_urlList.Reques('https://pvp.qq.com/web201605/herolist.shtml')
hero_code = wangzhe.get_content('a href="herodetail/(.*?).shtml')
hero_name = wangzhe.get_content('alt="(.*?)">')
for code in hero_code:
    a = hero_code.index(code)
    print(hero_name[a])
    os.mkdir(fr'C:\\Users\Administrator\Desktop\wang\{hero_name[a]}')
    for i in range(1,8):
        try:
            url_jpg = fr'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{code}/{code}-bigskin-{str(i)}.jpg'
            urllib.request.urlretrieve(url_jpg,filename=fr'C:\\Users\Administrator\Desktop\wang\{hero_name[a]}\{hero_name[a]}-{str(i)}.jpg')
            print(f'{hero_name[a]}{i} --> {url_jpg}')
        except:
            continue