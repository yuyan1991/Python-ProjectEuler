# -*- config: utf-8 -*-

low = 100
high = 1000

def isPalindrome(n):
    r = 0
    x = n
    while x > 0:
        r = r * 10 + (x % 10)
        x //= 10
    return r == n

ans = 0

for i in range(low, high):
    for j in range(low, high):
        if isPalindrome(i*j):
            ans=max(ans, i*j)

print("ans=", ans)
