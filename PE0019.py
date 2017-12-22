# -*- coding: utf-8 -*-

r = [1, 4, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6]

ans = 0
for year in range(1901, 2001):
    for i in range(12):
        if (r[i] + 1) % 7 == 0:
            ans += 1
            print(year, i + 1)
    for i in range(12):
        r[i] += 1
    if (year + 1) % 4 == 0 and (year + 1) % 100 != 0 or (year + 1) % 400 == 0:
        for i in range(2, 12):
            r[i] += 1

print(ans)
