# -*- coding: utf-8 -*-

maxn = 100

def solve(low, high):
    p = set([])
    for a in range(low, high):
        n = a
        for i in range(low, high):
            n *= a
            if not n in p:
                p.add(n)
    return len(p)


if __name__=='__main__':
    print(solve(2, maxn + 1))
