# -*- coding: utf-8 -*-

maxn = 1000000

def solve():
	s = ''
	for i in range(1, maxn):
		s += str(i)
		if len(s) > maxn:
			print('total = ', i)
			break
	ans = 1
	x = 1
	while x <= maxn:
		ans *= int(s[x - 1])
		print(s[x - 1])
		x *= 10
	print(ans)

if __name__=='__main__':
	solve()