# -*- config: utf-8 -*-
import math

n=600851475143
ans=n
for i in range(2, int(math.sqrt(n)) + 1):
    print(i)
    while n%i==0:
        n/=i
        ans=i
ans=max(ans,n)
print("ans=", int(ans))
