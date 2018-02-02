# -*- coding: utf-8 -*-

import math

maxn = 10000000

checked = [False] * maxn
P = []

def cal_prime():
	for i in range(2, maxn):
		if not checked[i]:
			P.append(i)
		for p in P:
			if p*i>=maxn:
				break
			checked[p*i]=True
			if i%p==0:
				break

def solve():
	for i in range(3, maxn, 2):
		if checked[i]:
			okay = False
			for j in range(1, int(math.sqrt(i/2)+1)):
				if not checked[i-2*j*j]:
					okay = True
					break
			if not okay:
				print(i)
				return

if __name__=='__main__':
	cal_prime()
	solve()