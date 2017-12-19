# -*- coding: utf-8 -*-

maxn = 1000 + 1

ans = -1

for a in range(1, maxn):
    for b in range(a, (maxn - a)//2 ):
        c = maxn - a - b - 1
        if a*a+b*b==c*c:
            print(a,b,c)
            ans = a * b * c
print(ans)
