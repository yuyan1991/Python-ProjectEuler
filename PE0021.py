# -*- coding: utf-8 -*-

import math

maxn = 10000 + 1
g = {}
for num in range(2, maxn):
    n = num
    res = 1
    for i in range(2, int(math.sqrt(num)) + 1):
        x = 1
        a = 1
        while n % i == 0:
            n //= i
            a *= i
            x += a
        res *= x
    if n > 1:
        res *= n + 1
    g[num] = res - num
print(g)
ans = 0
for num in range(2, maxn):
    if g[num] < maxn and g.get(g[num]) == num and g[num] != num:
        ans += num
print(ans)
