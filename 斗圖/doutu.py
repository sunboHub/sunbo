import module.get_urlList as get_urlList
import urllib
import os

# url = f'http://www.doutula.com/photo/list/?page=1'
# Doutu = get_urlList.Reques(url)
# urlList = Doutu.get_content('data-original="(.*?)" alt="(.*?)"')
# print(urlList)

for i in range(1, 3255):
    os.mkdir(f'C:\\Users\Administrator\Desktop\doutu\第{i}頁')
    Doutu = get_urlList.Reques(f'http://www.doutula.com/photo/list/?page={i}')
    urlList = Doutu.get_content('data-original="(.*?)" alt="(.*?)"')
    print(f'第{i}頁')
    print(urlList)
    for a in urlList:
        try:
            path = f'C:\\Users\Administrator\Desktop\doutu\第{i}頁\{a[1]}.jpg'
            urllib.request.urlretrieve(a[0], filename=path)
        except:
            continue
        else:
            print(f'{a[1]}-->{a[0]}')