# -*- coding: utf -*-

maxn = 1000000

checked = [False] * (maxn + 1)
P = []

def calPrime():
	P = []
	checked[0] = checked[1] = True
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
	x = 10
	while x <= p:
		if checked[p//x] or checked[p%x]:
			return False
		x *= 10
	return True

def solve():
	# print(P[-1])
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