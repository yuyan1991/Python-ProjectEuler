# -*- coding: utf-8 -*-

ans = 1
l = 0
for i in range(2, 1000):
    g = {}
    r = 1
    cur = 1
    while True:
        r*=10
        d=r//i
        r%=i
        if (d,r) in g:
            if cur - g.get((d,r)) > l:
                ans = i
                l = cur - g.get((d,r))
            g[(d,r)]=cur
            break
        g[(d,r)]=cur
        if r==0:
            break
        cur+=1
    print(i,":")
    print(g)
print(ans,":",l)
