# -*- coding: utf-8 -*-

import math

maxn = 10000 + 1

def cal(n):
	s = {}
	a,b,c = int(math.sqrt(n)), 1, -int(math.sqrt(n))
	s[(a,b,c)]=cnt=0
	while True:
		cnt+=1
		b = (n - c**2) // b
		for i in reversed(range(int(math.sqrt(n))+1)):
			if (i - c) % b == 0:
				a = (i-c)//b
				c = -i
				break
		if (a,b,c) in s:
			return cnt-s[(a,b,c)]
		s[(a,b,c)]=cnt

if __name__=='__main__':
	ans=0
	for n in range(2, maxn):
		if int(math.sqrt(n))**2<n:
			if cal(n) & 1:
				print(n)
				ans+=1
	print('Ans=', ans)