import requests
import parsel
import re


url = 'https://pvp.qq.com/web201605/herolist.shtml'
response = requests.get(url)
response.encoding = response.apparent_encoding
sel = parsel.Selector(response.text)
