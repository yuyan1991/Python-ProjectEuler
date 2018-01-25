# -*- coding: utf-8 -*-

import math

maxn = 1001
def solve():
	sol = [0] * maxn
	for a in range(1, maxn):
		for b in range(a, maxn):
			c = int(math.sqrt(a*a+b*b))
			if a*a+b*b==c*c and a+b+c<maxn:
				sol[a+b+c]+=1
	ans = 0
	for i in range(maxn):
		if sol[i]>sol[ans]:
			ans=i
	print(ans,':',sol[ans])

if __name__=='__main__':
	solve()