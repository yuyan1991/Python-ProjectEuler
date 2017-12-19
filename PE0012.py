# -*- coding: utf-8 -*-

maxn = 100000 + 1
lim = 500
p =[]
for i in range(2, maxn):
    okay = True
    for j in p:
        if i % j == 0:
            okay = False
            break
        if j * j > i:
            break
    if okay:
        p.append(i)

for i in range(2, maxn):
    n = i * (i + 1) // 2
    m = 1
    for j in p:
        cnt = 0
        while n % j == 0:
            n //= j
            cnt += 1
        m *= cnt + 1
        if n == 1:
            break
        if j * j > n:
            m *= 2
            break
    if m > lim:
        print(i,':', i * (i+1) // 2)
        break
