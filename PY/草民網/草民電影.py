import requests
import re
class CaoMin():
    def __init__(self):
        self.Url = 'https://www.cmdy5.com/'
        self.file = open('E:\\8.txt', 'a')
        self.list_address = []
        self.all_address = []
        self.Big_list = []
        self.get_address_()
    def get_address_(self):
        respone = requests.get(self.Url)
        respone.encoding = respone.apparent_encoding
        regular = re.compile('<li><a href="(.*?)">(.*?)</a></li>')
        result = re.findall(regular, respone.text)
        for i in range(1, 8):
            self.list_address.append(result[i][0])
    def Visit_address_(self):
        for a in self.list_address:
            respone = requests.get(a)
            respone.encoding = respone.apparent_encoding
            regular = re.compile(
                '<li class="p1 m1"><a class="link-hover" href="(.*?)" title="(.*?)">')
            result = re.findall(regular, respone.text)
            self.Big_list.extend(result)
            index = a.rfind('.')
            post = a[0:index]
            postfix = a[index:]
            for c in range(2, 380):
                new_address = post + '-' + str(c) + postfix
                try:
                    respone = requests.get(new_address)
                except:
                    break
                else:
                    respone.encoding = respone.apparent_encoding
                    regular = re.compile(
                        '<li class="p1 m1"><a class="link-hover" href="(.*?)" title="(.*?)">')
                    result = re.findall(regular, respone.text)
                    self.Big_list.extend(result)
                    for i in range(len(self.Big_list)):
                        try:
                            s = str(self.Big_list[i]) + '\n'
                            self.file.write(s)
                        except:
                            continue
                    else:
                        self.Big_list.clear()


a = CaoMin()
a.Visit_address_()
a.file.close()