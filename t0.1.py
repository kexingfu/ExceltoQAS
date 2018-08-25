# -*- coding: UTF-8 -*- 
import re

f = open("d:\\liebiao.txt",encoding='utf-8-sig')
line = f.readline()

print('|', end = '')
while line:
    ttt = re.split(r'[\s]+',line.strip())
    # print(ttt, end = '')
    s = '|'
    for t in ttt:
        s = s + '|' + t
    print(s)    
    line = f.readline()

f.close()