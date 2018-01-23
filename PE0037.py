# -*- coding: utf -*-

maxn = 1000

checked = [False] * (maxn + 1)
P = []

def calPrime():
	P = []
	for i in range(2, maxn):
		if not checked[i]:
			P.append(i)
		for p in P:
			if p * i > maxn:
				break
			checked[p*i] = True
			if i % p == 0:
				break
	return P

def isTruncatePrime(p):
	if p < 10:
		return False
	if p == 89:
		pass
	x = 0
	while True:
		x = x * 10 + p % 10
		if not checked[x]:
			return False
		p //= 10
		if p == 0:
			break
		if not checked[p]:
			return False
	return True

def solve():
	print(P)
	ans  =0
	cnt = 0
	for p in P:
		if isTruncatePrime(p):
			print(p)
			cnt+=1
			ans+=p
	print(cnt, ':', ans)

if __name__ == '__main__':
	P = calPrime()
	solve()