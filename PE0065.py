# -*- coding: utf-8 -*-

from functools import reduce

maxn = 100

def solve(depth):
	L = [[0,0,0, True]]
	L.append([2,0,0, False])
	cur = 1
	while cur:
		if cur == depth:
			L[cur][1] = L[cur][0]
			L[cur][2] = 1
			L[cur][3] = True
			cur-=1
			L[cur][3] = True
			continue
		if L[cur][3] == True:
			x,y = L[cur+1][2], L[cur+1][1]
			L[cur][1] = L[cur][0]*y + x
			L[cur][2] = y
			cur-=1
			L[cur][3] = True
			continue
		a = 1
		if cur % 3 == 2:
			a = (cur + 1) // 3 * 2
		L.append([a, 0, 0, False])
		cur+=1
	print(L[1])
	return reduce(lambda x,y: y+x, map(lambda x: ord(x)-48, str(L[1][1])))

if __name__=='__main__':
	print(solve(maxn))
