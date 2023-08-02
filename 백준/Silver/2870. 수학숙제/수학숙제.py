import sys
import re

n = int(sys.stdin.readline())

datas = [sys.stdin.readline().strip() for i in range(n)]

res = []

for data in datas:
    tmp = ''
    for i in data:
        if i.isdigit():
            tmp += str(i)
        if i.isalpha():
            if tmp == '' : 
                continue
            else:
                res.append(int(tmp))
                tmp = '' 
    if tmp!='' : 
        res.append(int(tmp))
res.sort()

for i in res:
    print(i)
    