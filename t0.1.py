# -*- coding: UTF-8 -*- 
import re
import tkinter

class Application(tkinter.Frame):

    # root = TK()
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = tkinter.Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.helloEntry = tkinter.Entry(self)
        self.helloEntry.pack()
        self.helloText = tkinter.Text(self, width=30,height=4 )
        self.helloText.pack()
        self.quitButton = tkinter.Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()

f = open("d:\\liebiao.txt",encoding='utf-8-sig')
line = f.readline()
ss = "|" 
print('|', end = '')
while line:
    ttt = re.split(r'[\s]+',line.strip())
    # print(ttt, end = '')
    s = '|'
    for t in ttt:
        s = s + '|' + t
    print(s)  
    ss = ss + s + "\n"
    line = f.readline()

f.close()
print(ss[0:-1])