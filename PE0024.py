# -*- coding: utf-8 -*-

a = []
x = 1
for i in range(9):
    x*=i+1
    a.append(x)

res=[]
n = 1000000
for i in range(9):
    cur=0
    while n > a[8-i]:
        cur+=1
        n-=a[8-i]
    res.append(cur)
res.append(0)

print(res)
l = [1] * 10
# print(l)
for i in res:
    cur=0
    for j in range(10):
        cur+=l[j]
        if cur==i+1:
            l[j]=0
            print(j,end="")
            break
