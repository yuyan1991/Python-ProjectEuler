# -*- coding: utf-8 -*-

from functools import reduce

maxn = 10000
d = {}
ans = maxn

def solve():
    for n in range(maxn):
        s = reduce(lambda x, y: y + x, sorted(str(n**3)))
        if d.get(s) is None:
            d[s]=[n,1]
        else:
            d[s][1]+=1

if __name__=='__main__':
    solve()
    for v in d.values():
        if v[1]==5 and v[0]<ans:
            ans = v[0]
    print('%d: %d'%(ans, ans**3))
