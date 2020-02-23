import tkinter as tk
name = ['書店','大壞蛋','阿蘭德龍']
 # 控件
root = tk.Tk()
# 窗口大小
root.geometry('320x600')

root.title('酷我音樂')

r0 = tk.Label(root, text='請輸入歌手名字:', font=15)
r0.grid(row=0, column=0)

r1 = tk.Label(root, text='請輸入保存地址:', font=15)
r1.grid(row=1, column=0)
# 输入框
e1 = tk.Entry(root, font=22,width=15)
e1.grid(row=0, column=1)

e2 = tk.Entry(root, font=22,width=15)
e2.grid(row=1, column=1)
# 多選框
for i in name:
    index = name.index(i) + 2
    cheak = tk.Checkbutton(root,text =i )
    cheak.grid(row=index, columnspan=1)

# 按钮
a1 = tk.Button(root, text='下載', font=12,
              )  # ,command = readpass
a1.grid(row=1, column=2)

a1 = tk.Button(root, text='搜索', font=12,
              )  # ,command = readpass
a1.grid(row=0, column=2)

root.mainloop()