# -*- coding: utf-8 -*-

maxn = 1000

def power(x, n = 2):
    res = 1
    while n:
        if n % 2 == 1:
            res *= x
        x = x * x
        n //= 2
    return res

s = str(power(2, maxn))
ans = 0
for c in s:
    ans += int(c)
print(ans)
