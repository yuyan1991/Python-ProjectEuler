# -*- coding: utf-8 -*-

maxn = 10000
d = {}
ans = maxn

def solve():
	for n in range(maxn):
		res = n ** 3
		s = ''
		for c in sorted(str(res)):
			s += c
		if d.get(s) is None:
			d[s]=[n,1]
		else:
			d[s][1]+=1

if __name__=='__main__':
	solve()
	for v in d.values():
		if v[1]==5 and v[0]<ans:
			ans = v[0]
	print('%d: %d'%(ans, ans**3))