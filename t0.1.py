# -*- coding: UTF-8 -*- 
import re

f = open("d:\\liebiao.txt",encoding='utf-8-sig')
line = f.readline()

# s="|"
while line:
#     ttt = re.split(r'[\s]+',line.strip())
    print(line, end = '')
    line = f.readline()


#     for wor in ttt:
#         s = s + "|" + wor 

# print(s)
f.close()