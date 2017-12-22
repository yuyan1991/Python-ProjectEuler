# -*- coding: utf-8 -*-

maxn = 100

product = 1
for i in range(1, maxn + 1):
    product *= i
ans = 0
for x in str(product):
    ans += int(x)

print(ans)
print(product)
