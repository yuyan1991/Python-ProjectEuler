# -*- coding: utf-8 -*-

maxn = 100
ans=0
d=set()
for i in range(1,maxn):
    x=str(i)
    for j in range(max(maxn,i),maxn*maxn):
        y=str(j)
        z=str(i*j)
        if len(x)+len(y)+len(z)>9:
            break
        if len(x)+len(y)+len(z)<9:
            continue
        if z in d:
            break
        s=set()
        for p in x:
            s.add(p)
        for p in y:
            s.add(p)
        for p in z:
            s.add(p)
        okay=True
        for k in range(1,10):
            if not str(k) in s:
                okay=False
                break
        if okay:
            d.add(z)
            print("%d*%d=%d"%(i,j,i*j))
            ans+=i*j
print(ans)
