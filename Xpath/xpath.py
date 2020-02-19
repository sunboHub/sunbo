from lxml import etree
import requests

respone = requests.get('https://www.cmdy5.com/')
respone.encoding = respone.apparent_encoding
# print(respone.text)

selector = etree.HTML(respone.text)
res1 = selector.xpath('//div[@id="topnav-1"]/div/ul/li/a/text()')
res2 = selector.xpath('//div[@id="topnav-1"]/div/ul/li/a/@href')

result = zip(res1,res2)
print(dict(result))
