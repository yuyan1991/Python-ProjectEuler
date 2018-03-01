# -*- coding: utf-8 -*-

maxm = 10 + 1
maxn = 1000 + 1
s = set()
ans = 0

def solve():
	global ans
	for i in range(1, maxm):
		for j in range(maxn):
			if len(str(i**j))==j and not (i**j in s):
				ans += 1
				s.add(i**j)
				print('(%d, %d)'%(i, j))

if __name__=='__main__':
	solve()
	print('Ans = ', ans)
	print(s)