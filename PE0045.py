# -*- coding: utf-8 -*-

maxn = 1000000 + 1

def find(F, n):
	l = 1
	r = maxn
	while l<=r:
		mid = (l+r)//2
		if F(mid)<n:
			l = mid + 1
		else:
			r = mid - 1
	return l

def solve(low, high):
	for i in range(low, high):
		n = (lambda x: x*(3*x-1)//2)(i)
		T = lambda x: x*(x+1)//2
		H = lambda x: x*(2*x-1)//2
		if T(find(T, n))==n and H(find(H, n))==n:
			print(n)

if __name__=='__main__':
	solve(1, maxn)