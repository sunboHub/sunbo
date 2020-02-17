import requests
# import parsel
import re


class Reques():
    def __init__(self, url):
        self.url = url
        self.__get_response()

    def __get_response(self):
        response = requests.get(self.url)
        response.encoding = response.apparent_encoding
        self.response = response

    def get_content(self, cssRe):
        regular = re.compile(cssRe)
        urlList = re.findall(regular, self.response.text)
        # sel = parsel.Selector(self.response.text)
        # urlList = sel.css(cssRe).getall()
        return urlList


if __name__ == '__main__':
    wangzhe = Reques('https://pvp.qq.com/web201605/herolist.shtml')
    urlList = wangzhe.get_content('alt="(.*?)">')

    print(urlList)
