# -*- coding: utf-8 -*-

maxn = 2000000 + 1;
p = []
ans = 0
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
        ans += i
print(ans)
