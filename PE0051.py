# -*- coding: utf-8 -*-

maxn = 1000000
limit = 8
checked = [False] * maxn
P = []

def cal_prime():
	checked[0] = checked[1] = True
	for i in range(2, maxn):
		if not checked[i]:
			P.append(i)
		for p in P:
			if p*i>=maxn:
				break
			checked[p*i]=True
			if i%p==0:
				break

def getDigit(p, l):
	return (p//(10**l))%10

def solve():
	for p in P:
		l = len(str(p))
		s = (1<<l)-1
		i = s
		while i>0:
			okay = True
			origin = -1
			for j in range(l):
				if i & (1<<j) > 0:
					x = getDigit(p, j)
					if origin == -1:
						origin = x
						if 10 - origin < limit:
							okay = False
							break
					elif origin != x:
						okay = False
						break
			if okay:
				cnt = 0
				for x in range(origin, 10):
					n = p
					for j in range(l):
						if i & (1<<j) > 0:
							y = getDigit(p, j)
							if not checked[p - y * (10**j) + x * (10**j)]:
								cnt += 1
				if cnt >= limit:
					print(p)
					return
			i=(i-1)&s

if __name__=='__main__':
	cal_prime()
	solve()
