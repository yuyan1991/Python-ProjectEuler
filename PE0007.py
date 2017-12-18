# -*- config: utf-8 -*-

maxn = 1 << 30
L = []
total = 0
for p in range(2, maxn):
    okay = True
    for i in L:
        if p % i == 0:
            okay = False
            break
    if okay:
        L.append(p)
        total += 1
        if total == 10001:
            print(p)
            break
