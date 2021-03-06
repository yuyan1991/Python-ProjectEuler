# -*- coding: utf-8 -*-

maxn = 9
ans = 0
checked = 0

import math

def isPrime(n):
	if n == 2:
		return True
	if n % 2 == 0:
		return False
	for i in range(3, int(math.sqrt(n)) + 1, 2):
		if n % i == 0:
			return False
	return True

def dfs(cur, ll, v):
	global ans
	global checked
	if cur > ll:
		if isPrime(v) and v>ans:
			ans=v
		return
	steps = 1
	if cur == 1:
		steps = 2
	for i in reversed(range(1, l+1, steps)):
		if checked & (1<<(i-1)) == 0:
			checked ^= 1<<(i-1)
			dfs(cur+1, ll, v + i*10**(cur-1))
			checked ^= 1<<(i-1)

if __name__=='__main__':
	for l in reversed(range(1, maxn)):
		dfs(1, l, 0)
		if ans > 0:
			break
	print(ans)