# -*- coding: utf-8 -*-

maxn = 1000000
ans = 1
length = 1
f={}
f[1]=1
def cal(n):
    if n in f:
        return f[n]
    if n % 2 == 1:
        f[n] = cal(n * 3 + 1) + 1
        return f[n]
    else:
        f[n] = cal(n // 2) + 1
        return f[n]
for num in range(1, maxn):
    n = num
    # x = 0
    # while n > 1:
    #     if n in f:
    #         x += f[n]
    #         break
    #     if n % 2 == 1:
    #         n = n * 3 + 1
    #     else:
    #         n //= 2
    #     x += 1
    x = cal(num)
    if x > length:
        ans = num
        length = x
    if not num in f:
        f[num] = x
print(ans,':',length)
