# -*- coding: utf-8 -*-

from functools import reduce

maxn = 100 + 1

if __name__=='__main__':
	ans=x=y=0
	for a in range(1, maxn):
		p = 1
		for b in range(1, maxn):
			p *= a
			s = reduce(lambda x,y: x+y, map(lambda x: int(x),list(str(p))))
			if s>ans:
				ans = s
				x,y = a,b
	print(ans)
	print(x,y)