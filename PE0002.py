# -*- config: utf-8 -*-

ans=0
a=0
b=1
while True:
    c = a + b
    a = b
    b = c
    if c > 4000000:
        break
    if c%2==0:
        ans += c

print("ans=", ans)
