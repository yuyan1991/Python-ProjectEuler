# -*- coding: utf-8 -*-

import math

# Answer:
# [13, 5197, 5701, 6733, 8389]
# 26033

maxn = 10000
limit = 5

checked = [False] * maxn
P = []
num = [0] * limit
ans = 1<<30
cntPrime = 0

def calPrime():
    global cntPrime
    checked[0]=checked[1]=True
    for i in range(2, maxn):
        if not checked[i]:
            P.append(i)
            cntPrime += 1
        for p in P:
            if p * i >= maxn:
                break
            checked[p*i]=True
            if i%p==0:
                break

def isPrime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

def checkPrime(a, b):
    if int(str(a) + str(b)) < maxn:
        return not checked[int(str(a) + str(b))]
    return isPrime(int(str(a) + str(b)))

def search(dep, cur, tot):
    global ans
    if dep == limit:
        ans = tot
        print(num)
        return
    for i in range(cur, cntPrime):
        if tot + P[i] * (limit - dep) > ans:
            break
        num[dep]=P[i]
        okay = True
        for j in range(dep):
            if not checkPrime(num[dep], num[j]) or not checkPrime(num[j], num[dep]):
                okay = False
                break
        if okay:
            search(dep+1, i+1, tot+num[dep])

if __name__=='__main__':
    calPrime()
    search(0, 1, 0)
    print(ans)
