# -*- coding: utf-8 -*-

maxn = 200000
# def solve():
#     ans = 0
#     for a in range(1, 10):
#         for b in range(0, 10):
#             for c in range(0, 10):
#                 for d in range(0, 10):
#                     for e in range(0, 10):
#                         if a**5+b**5+c**5+d**5+e**5==10000*a+1000*b+100*c+10*d+e:
#                             ans+=10000*a+1000*b+100*c+10*d+e
#                             print(10000*a+1000*b+100*c+10*d+e)
#     return ans

def isFifthPower(n):
    x=n
    res=0
    while x:
        res+=(x%10)**5
        x//=10
    return res==n

def solve2():
    ans=0
    for i in range(10, maxn):
        if isFifthPower(i):
            print(i)
            ans+=i
    return ans
if __name__=='__main__':
    print('Ans=', solve2())
