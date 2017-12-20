# -*- coding: utf-8 -*-

maxn = 20
f = [[0 for i in range(maxn + 1)], [0 for i in range(maxn + 1)]]
o = 1
for i in range(maxn + 1):
    f[o][0] = 1
    for j in range(1, maxn + 1):
        f[o][j] = f[o][j-1] + f[o^1][j]
    o ^= 1
print(f[o^1][maxn])
