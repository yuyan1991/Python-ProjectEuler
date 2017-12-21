# -*- coding: utf-8 -*-

maxn = 1000
ans = 0
for i in range(maxn + 1):
    n = i
    if n == 1000: # one thousand
        ans += 11
        break
    if 100 <= n:
        if 100 <= n < 300 or 600 <= n < 700:
            ans += 3 # one, two, six
        if 300 <= n < 400 or 700 <= n < 900:
            ans += 5 # three, seven, eight
        if 400 <= n < 600 or 900 <= n:
            ans += 4 # four, five, nine
        ans += 7 # hundred
        n %= 100
        if n:
            ans += 3 # and
    if 10 <= n < 20:
        cnt = {10: 3, 11 : 6, 12 : 6, 13 : 8, 14 : 8, 15 : 7, 16 : 7, 17 : 9, 18 : 8, 19: 8} # ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen
        ans += cnt[n]
        continue
    if 20 <= n < 40 or 80 <= n < 100:
        ans += 6 # twenty, thirty, eighty, ninety
    if 40 <= n < 70:
        ans += 5 # forty, fifty, sixty
    if 70 <= n < 80:
        ans += 7 # seventy
    n %= 10
    if 1 <= n < 3 or n == 6:
        ans += 3 # one, two, six
    if n == 3 or 7 <= n < 9:
        ans += 5 # three, seven, eight
    if 4 <= n < 6 or n == 9:
        ans += 4 # four, five, nine

print(ans)
