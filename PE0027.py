# -*- coding: utf-8 -*-

maxp = 100000
maxn = 1000

p = []
def calPrime():
    p = [2]
    for i in range(3, maxp):
        okay = True
        for j in p:
            if i % j == 0:
                okay = False
                break
            if j * j > i:
                break
        if okay:
            p.append(i)
    p = set(p)
    print(p)
    return p

def solve(lim1, lim2):
    maxlen = 0
    ans = 0
    x = y = 0
    for a in range(-lim1 + 1, lim1):
        for b in range(-lim2 + 1, lim2):
            n = 0
            while n*n+a*n+b in p:
                n+=1
            if n>maxlen:
                maxlen=n
                ans=a*b
                x,y = a,b
    return ans, x, y, maxlen
if __name__=='__main__':
    p = calPrime()
    print(solve(maxn, maxn + 1))
