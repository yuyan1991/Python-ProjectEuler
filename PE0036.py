# -*- coding: utf-8 -*-

maxn = 1000000 + 1

if __name__=='__main__':
	ans=0
	for n in range(maxn):
		if list(str(n))==list(reversed(str(n))) and list(str(bin(n))[2:])==list(reversed(str(bin(n)[2:]))):
			ans+=n
	print('Ans=', ans)