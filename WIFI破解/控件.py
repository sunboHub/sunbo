import tkinter as t

def ce():
    a = e1.get()
    b = e2.get()
    print(a)
    print(b)

    text.insert(t.END,a+b+'能用能用+1')
    text.see(t.END)
    text.update()
# 控件
root = t.Tk()
# 窗口大小
root.geometry('260x360')

root.title('暴力破解')

r0 = t.Label(root,text = 'wifi名称:',font = 15)
r0.grid(row = 0,column = 0)

r1 = t.Label(root,text = '密码本PATH:',font = 15)
r1.grid(row = 1,column = 0)
# 输入框
e1 = t.Entry(root,font = 22)
e1.grid(row = 0,column = 1)

e2 = t.Entry(root,font = 22)
e2.grid(row = 1,column = 1)

# 列表框
text = t.Listbox(root,font = ('微软雅黑',15),width = 20,height = 10)
text.grid(row = 2, columnspan = 2)

# 按钮
a1 = t.Button(root,text = '开始破解',font = 12,command = ce)#,command = readpass
a1.grid(row = 3,columnspan = 2)

root.mainloop()