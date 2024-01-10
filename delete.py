import shutil
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as megbox
from tkinter import filedialog

# 获取配置文件路径
def getUrl( linesList ):
    for str in linesList:
        homeContains = str.__contains__("steward.home")
        if homeContains == True :
            url = str.split("=")[1]
            return url
        
# tk选择框
def select_file(lable):
    file_path = filedialog.askopenfilename()
    if file_path:
        lable.config(text=file_path)

# 删除文件夹
def readDelete(lable, root):
    if megbox.askyesno("确认操作", "该操作无法撤销！"):
        try:
            # child = tk.Tk()
            # child.geometry('360x150+%d+%d'%((mw-360)/2,(mh-150)/2))
            # proOne = ttk.Progressbar(child)
            # proOne.pack(side=TOP)
            # proOne['maximum'] = 1000
            # proOne['value'] = 10

            path = lable.cget("text")

            print(path)
            readme = open(path.replace("/","\\\\"))
            lines = readme.read()
            linesList = lines.split("\n")

            print(lines)
            print(linesList)
            url = getUrl(linesList)
            print(url)
            shutil.rmtree(url)
        except Exception as e:
            megbox.showerror(title="发生错误", message=e)
    else:
        root.destroy()

if __name__ == '__main__':

    # 创建主窗口
    root = tk.Tk()
    # 设置窗口标题
    root.title("甘棠门店管家删除程序")

    mw, mh = root.maxsize()

    root.geometry('360x150+%d+%d'%((mw-360)/2,(mh-150)/2))

    lable = tk.Label(root, text="文件路径", width=30)
    lable.pack(side=TOP,expand=NO)

    select = tk.Button(root, text="选择文件", command=lambda: select_file(lable))
    select.pack(side=LEFT,expand=YES)

    uni = tk.Button(root, text="开始卸载", command=lambda: readDelete(lable, root))
    uni.pack(side=LEFT,expand=YES)

    # 启动主事件循环
    root.mainloop()

