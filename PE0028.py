# -*- coding: utf-8 -*-

def solve(n):
    ans = 1
    for i in range(1, n - 1, 2):
        ans += 4 * i * i + 10 * i + 10
    return ans
if __name__=='__main__':
    print(solve(1001))
