# -*- coding: utf-8 -*-

maxn=201
F=[0]*maxn
C=(1,2,5,10,20,50,100,200)

F[0]=1
for c in C:
    for i in reversed(range(maxn)):
        for k in range(1,maxn):
            if i<c*k:
                break
            F[i]+=F[i-c*k]
    print(F)

print(F[maxn-1])
