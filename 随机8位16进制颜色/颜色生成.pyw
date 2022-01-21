import random
import tkinter as tk

list = []
a = ''


# 创建主窗口
win = tk.Tk()
win.title("颜色生成")
win.minsize(20, 100)
# 创建标签
t = tk.Entry(win, width=20)
t.place(x=30, y=20, height="20px")


def shengcheng():
    for i in range(8):
        tem = random.randint(0, 15)
        if tem == 10:
            list.append('a')
        if tem == 11:
            list.append('b')
        if tem == 12:
            list.append('c')
        if tem == 13:
            list.append('d')
        if tem == 14:
            list.append('e')
        if tem == 15:
            list.append('f')
        if tem < 10:
            list.append(tem)
    a = "".join('%s' % id for id in list)
    t.delete(0, 'end')
    t.insert(20, a)
    list.clear()


tt = tk.Button(win, text="生成", command=shengcheng)
list.clear()
tt.place(x=80, y=100, height="20px")

# 启动主循环
win.mainloop()
