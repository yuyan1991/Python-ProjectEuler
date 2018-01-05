# -*- coding: utf-8 -*-

import math

maxn = 28123 + 1
s=set()

for i in range(1, maxn):
    tot = 1
    n = i
    for j in range(2, int(math.sqrt(i)) + 1):
        res = a = 1
        while n % j == 0:
            a*=j
            res+=a
            n//=j
        tot*=res
    if n > 1:
        tot*=1+n
    tot-=i
    if tot > i:
        print(i," ")
        s.add(i)

ans = 0
for i in range(1, maxn):
    okay = True
    for j in range(1, i//2 + 1):
        if j in s and (i-j) in s:
            okay = False
            break
    if okay:
        ans+=i
print(ans)
