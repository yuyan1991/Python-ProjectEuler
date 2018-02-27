# -*- coding: utf-8 -*-

# ===================== [0, 1, 4, 5, 3, 2] ===================== (start)
# 2882
# 8128
# 1281
# 2512
# 5625
# 8256
# Sum =  28684
# ===================== [0, 1, 4, 5, 3, 2] ===================== (end)

import math

n = 6
maxn = 150
nSize = 100

A = [[
x * (x + 1) // 2 for x in range(maxn) if 1000 <= x * (x + 1) // 2 <= 9999
], [x * x for x in range(maxn) if 1000 <= x * x <= 9999], [
x * (3 * x - 1) // 2 for x in range(maxn)
if 1000 <= x * (3 * x - 1) // 2 <= 9999
], [x * (2 * x - 1) for x in range(maxn) if 1000 <= x * (2 * x - 1) <= 9999], [
x * (5 * x - 3) // 2 for x in range(maxn)
if 1000 <= x * (5 * x - 3) // 2 <= 9999
], [x * (3 * x - 2) for x in range(maxn) if 1000 <= x * (3 * x - 2) <= 9999]]


def gen_permutation(x):
	checked = [False] * maxn
	res = []
	for i in reversed(range(n)):
		for j in reversed(range(i+1)):
			if j*(math.factorial(i))<=x:
				x -= j * (math.factorial(i))
				cur = 0
				for k in range(n):
					if not checked[k]:
						if cur == j:
							checked[k] = True
							res.append(k)
							break
						cur+=1
				break
	return res

def solve():
	for x in range(math.factorial(n)):
		F = [[[0] * nSize for i in range(n)] for i in range(nSize)]
		L = gen_permutation(x)
		for i in A[L[0]]:
			F[i//100][0][i%100]=i
		for i in range(1, n):
			for j in A[L[i]]:
				for k in range(nSize):
					if F[k][i-1][j//100]:
						F[k][i][j%100]=j
		okay = False
		for i in range(nSize):
			if F[i][n-1][i]:
				okay = True
				break
		if not okay:
			continue
		print('=====================', L, '===================== (start)')
		for i in range(nSize):
			if F[i][n-1][i]:
				cur = i
				ans = 0
				for l in reversed(range(n)):
					k = F[i][l][cur]
					print(k)
					ans+=k
					cur = k//100
				print('Sum = ', ans)
		print('=====================', L, '===================== (end)')
		break

if __name__=='__main__':
	solve()
