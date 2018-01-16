# -*- coding: utf-8 -*-

import math

maxn = 10

F = [math.factorial(x) for x in range(maxn)]
ans = 0

def search(cur, v):
    global ans
    if cur == v:
        print(v)
        ans+=v
    if cur + F[maxn-1] < v * 10:
        # print('(%d,%d)'%(cur,v))
        return
    for i in range(maxn):
        search(cur + F[i], v * 10 + i)

if __name__=='__main__':
    for i in range(1, maxn):
        search(F[i], i)
    print(F)
    print('Ans=', ans -1 - 2)