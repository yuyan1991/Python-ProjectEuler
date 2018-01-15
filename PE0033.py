# -*- coding: utf-8 -*-

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

a=b=1
for i in range(10, 99):
    for j in range(i+1, 99):
        if i%10==0:
            break
        if j%10==0:
            continue
        if i//10==j//10 and i*(j%10)==j*(i%10):
            a*=i
            b*=j
            print('(%d,%d)'%(i,j))
        elif i%10==j%10 and i*(j//10)==j*(i//10):
            a*=i
            b*=j
            print('(%d,%d)'%(i,j))
        elif i//10==j%10 and i*(j//10)==j*(i%10):
            a*=i
            b*=j
            print('(%d,%d)'%(i,j))
        elif i%10==j//10 and i*(j%10)==j*(i//10):
            a*=i
            b*=j
            print('(%d,%d)'%(i,j))
print(b//gcd(a,b))
