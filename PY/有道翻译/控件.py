import tkinter as t

# 控件
root = t.Tk()
# 窗口大小
root.geometry('245x360')

root.title('有道翻译')

r0 = t.Label(root, text='输入单词:', font=15)
r0.grid(row=0, column=0)
# 输入框
e1 = t.Entry(root, font=22)
e1.grid(row=0, column=1)

# 列表框
text = t.Listbox(root, font=('微软雅黑', 15), width=20, height=10)
text.grid(row=2, columnspan=2)

# 按钮
a1 = t.Button(root, text='翻译', font=12)  # ,command = readpass
a1.grid(row=3, columnspan=2)

root.mainloop()
