# -*- coding: utf-8 -*-

import math

maxn = 10

F = [math.factorial(x) for x in range(maxn)]
ans = 0

def search(cur, v):
    global ans
    if cur + F[maxn-1] < v * 10:
        return
    if cur == v:
        print(v)
        ans+=v
    print('(%d,%d)'%(cur,v))
    for i in range(maxn):
        search(cur + F[i], v * 10 + i)
    # search(cur + F[0], v * 10 + 0)
    # search(cur + F[1], v * 10 + 1)
    # search(cur + F[2], v * 10 + 2)
    # search(cur + F[3], v * 10 + 3)
    # search(cur + F[4], v * 10 + 4)
    # search(cur + F[5], v * 10 + 5)
    # search(cur + F[6], v * 10 + 6)
    # search(cur + F[7], v * 10 + 7)
    # search(cur + F[8], v * 10 + 8)
    # search(cur + F[9], v * 10 + 9)

if __name__=='__main__':
    for i in range(1, maxn):
        search(F[i], i)
    print('Ans=', ans)