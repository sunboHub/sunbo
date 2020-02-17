import requests
import urllib


class Save():
    def __init__(self,path,dawnload_url):
        self.dawnload_url = dawnload_url

    def open_save(self,path):
        data = requests.get(self.dawnload_url).content
        with open(path,'a') as f:
            f.write(data)

    def urllib_save(self,path):
        urllib.request.urlretrieve(self.dawnload_url, filename=path)