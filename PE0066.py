# -*- coding: utf-8 -*-

import math

maxn = 1000 + 1
maxm = 1000000 + 1;

if __name__=='__main__':
	ans = 0
	for D in range(2, maxn):
		if int(math.sqrt(D))**2<D:
			for x in range(2, maxm):
				if (x**2-1)%D==0 and int(math.sqrt((x**2-1)//D))**2==(x**2-1)//D:
					ans = max(ans, x)
					print("%d:%d"%(D, x))
					break
	print('Ans = ', ans)