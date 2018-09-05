# -*- coding: UTF-8 -*- 
import re
import tkinter
import win32clipboard as w
import win32con

#转换函数
def exceltoqas(f):    
    ff = f.split('\n')    
    ss = '|'
    for line in ff:        
        ttt = re.split(r'[\s]+',line.strip())
        s = '|'
        for t in ttt:
            s = s + '|' + t
        ss = ss + s + "\n"   
    # print(ss)
    return ss[0:-1]

#获取剪切板内容
def gettext():
    w.OpenClipboard()
    t = w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()
    t = t.decode('GB2312')
    return t

#写入剪切板内容
def settext(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_TEXT, aString)
    w.CloseClipboard()

#点击按钮执行的方法
def yijian():
    ijt = gettext()
    ojt = exceltoqas(ijt)
    settext(ojt.encode('GB2312'))   

# GUI
class Application(tkinter.Frame):
    # root = TK()
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel1 = tkinter.Label(self, text='Excel to QAS')
        self.helloLabel1.pack()
        self.helloLabel2 = tkinter.Label(self, text='使用方法：选中复制表格后，点击下方按钮，到QAS上粘贴即可\n\n适用范围：Excel、Word、有道云笔记等\n注意事项：点一次就够啦！\n')
        self.helloLabel2.pack()
        # self.helloEntry = tkinter.Entry(self)
        # self.helloEntry.pack()
        # self.helloText = tkinter.Text(self, width=30,height=4 )
        # self.helloText.pack()
        self.quitButton = tkinter.Button(self, text='\n  一键转换到剪贴板  \n', command=yijian)
        self.quitButton.pack()

app = Application()
# 设置窗口标题:
app.master.title('ExceltoQAS V0.2')
# 主消息循环:
app.mainloop()


