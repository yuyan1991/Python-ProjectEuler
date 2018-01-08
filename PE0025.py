# -*- coding: utf-8 -*-

def fib():
    a = 0
    b = 1
    while (True):
        yield b
        a,b = b, a + b
g = fib()
ans = 0
while (True):
    res = str(next(g))
    ans += 1
    if len(res) >= 1000:
        print(res)
        print(ans)
        break
