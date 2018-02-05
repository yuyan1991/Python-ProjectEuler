#-*- coding: utf-8 -*-

maxn = 1000 + 1
r = 10000000000

if __name__=='__main__':
	ans = 0
	for i in range(1, maxn):
		ans = (ans+i**i)%r
	print(ans)