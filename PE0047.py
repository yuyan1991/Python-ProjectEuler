# -*- coding: utf-8 -*-

import math

maxn=1000000
wanted = 4

totalFactor = [0] * maxn

def countFactor(n):
	ans = 0
	x = n
	for i in range(2, int(math.sqrt(n)) + 1):
		if x % i == 0:
			ans += 1
			if ans>wanted:
				break
		else:
			continue
		while x % i == 0:
			x//=i
	if x > 1:
		ans+=1
	return ans

def solve():
	for i in range(5, maxn):
		totalFactor[i] = countFactor(i)
		if totalFactor[i] == wanted and totalFactor[i-1] == wanted and totalFactor[i-2] == wanted and totalFactor[i-3] == wanted:
			print(i-3)
			return

if __name__=='__main__':
	solve()