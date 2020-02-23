import urllib
import requests
import os
import tkinter as tk


class kuwoMusic():
    def __init__(self, singerName, address):
        self.address = address
        self.singerName = singerName
        self.headers = {
            'Referer': f'http://www.kuwo.cn/search/list?key={self.singerName}',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
            'csrf': 'NZNCXJFZLFF',
            'Host': 'www.kuwo.cn',
            'Cookie': '_ga=GA1.2.172942019.1580702894; _gid=GA1.2.771718281.1580890479; uname3=%u3081%u3044%u305F%u3093%u3066%u3044%u3053%u306A%u3093; t3kwid=235511292; userid=235511292; websid=2033651825; pic3="http://q.qlogo.cn/qqapp/100243533/BEB10B9B72AB7C5E6700E08B820BA1C5/100"; t3=qq; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1580702894,1580890479,1580891122; _gat=1; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1580892336; kw_token=NZNCXJFZLFF'
        }
        self.songname = []
        self.songurl = []

    def _get_url(self):
        url = f'http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={self.singerName}&pn=1&rn=30&reqId=ec2404f0-47f3-11ea-b35a-df5b093dd227'
        response = requests.get(url, headers=self.headers).json()
        return response

    def _get_data(self):
        rids = []
        jsons = self._get_url()
        lists = jsons['data']['list']
        for i in lists:
            rids.append((i['rid'], i['name']))
        return rids

    def download_mp3(self):
        for i in self._get_data():
            url = 'http://www.kuwo.cn/url?format=mp3&rid={}&response=url&type=convert_url3'.format(
                str(i[0]))
            self.songname.append(i[1])
            response = requests.get(url,headers = self.headers).json()
            html = response['url']
            self.songurl.append(html)
            print(i[1])
            print(html)
            data = requests.get(html).content
            path = os.path.join(r"C:\\Users\Administrator\Desktop\mu", i[1] + '.mp3')
            with open(path,'wb') as f:
                f.write(data)


def sou():
    address = e2.get()
    name = e1.get()
    singerName = urllib.parse.quote(name)
    a = kuwoMusic(singerName, address)
    a.download_mp3()
    for i in a.songname:
        index = a.songname.index(i) + 2
        if index <= 21:
            cheak = tk.Checkbutton(root, text=i,)
            cheak.grid(row=index, column=0)
        elif index > 21:
            cheak = tk.Checkbutton(root, text=i,)
            cheak.grid(row=index-20, column=1)


    # 控件
root = tk.Tk()
# 窗口大小
root.geometry('520x600')

root.title('酷我音樂')

r0 = tk.Label(root, text='請輸入歌手名字:', font=15)
r0.grid(row=0, column=0)

r1 = tk.Label(root, text='請輸入保存地址:', font=15)
r1.grid(row=1, column=0)
# 输入框
e1 = tk.Entry(root, font=22, width=15)
e1.grid(row=0, column=1)

e2 = tk.Entry(root, font=22, width=15)
e2.grid(row=1, column=1)
# 多選框
# for i in a.songname:
#     index = a.songname.index(i) + 1
#     cheak = tk.Checkbutton(root, text=i)
#     cheak.grid(row=index, columnspan=3)

# 按钮
a1 = tk.Button(root, text='下載', font=12,
               )  # ,command = readpass
a1.grid(row=1, column=2)

a1 = tk.Button(root, text='搜索', font=12, command=sou)  # ,command = readpass
a1.grid(row=0, column=2)

root.mainloop()


# if __name__ == '__main__':
#     name = str(input('请输入想要下载的歌手：'))
#     singerName = urllib.parse.quote(name)
#     Mp3 = kuwoMusic(singerName)
#     Mp3.download_mp3()
# def start():
#     address = value2.get()
#     name = value1.get()
#     singerName = urllib.parse.quote(name)
#     Mp3 = kuwoMusic(singerName,address)
#     Mp3.download_mp3()
#
# if __name__ == '__main__':
#     window = tk.Tk()                                     # 创建窗口对象
#     window.geometry('400x200')                           # 设置窗口大小
#     window.title('VIP解析')                              # 设置窗口标题
#
#     # 设置上边frame框架控件；在屏幕上显示一个矩形区域，多用来作为容器
#     # 用来放两个标签，下拉框和输入框
#     ContentBoxTop = tk.Frame(window, width=200)
#     ContentBoxTop.pack(side=tk.TOP, anchor='s')
#
#     # 设置下边frame框架控件；在屏幕上显示一个矩形区域，多用来作为容器
#     # 用来放按钮
#     ContentBoxBottom = tk.Frame(window, width=200)
#     ContentBoxBottom.pack(side=tk.TOP, anchor='n', fill='y',
#                         expand='yes')
#
#     # 设置左边frame框架控件；在屏幕上显示一个矩形区域，多用来作为容器
#     # 用来放两个标签控件
#     ContentBoxTopLeft = tk.Frame(ContentBoxTop, width=200)
#     ContentBoxTopLeft.pack(side=tk.LEFT, anchor='n', fill='x',
#                         expand='yes', pady='30', padx='15')
#
#     # 设置右边frame框架控件；在屏幕上显示一个矩形区域，多用来作为容器
#     # 用来放下拉框和输入框
#     ContentBoxTopRight = tk.Frame(ContentBoxTop, width=200)
#     ContentBoxTopRight.pack(side=tk.RIGHT, anchor='n', fill='x',
#                             expand='yes', pady='30', padx='15')
#
#     txt1 = tk.Label(ContentBoxTopLeft, text='輸入下載歌手：')       # 设置标签框
#     txt1.pack(side=tk.TOP, anchor='e', pady='5')
#
#     txt2 = tk.Label(ContentBoxTopLeft, text='輸入保存地址：')       # 设置标签框
#     txt2.pack(side=tk.TOP, anchor='e', pady='5')
#
#     value1 = tk.Entry(ContentBoxTopRight, text='', width=103)  # 设置输入框
#     value1.pack(side=tk.TOP, anchor='w', pady='5')
#
#     value2 = tk.Entry(ContentBoxTopRight, text='', width=103)  # 设置输入框
#     value2.pack(side=tk.TOP, anchor='w', pady='5')
#
#     button = tk.Button(ContentBoxBottom, text='开始下載',
#                     font=12,command=start)  # 设置按钮
#     button.pack(side=tk.TOP, anchor='center')
#     window.mainloop()
