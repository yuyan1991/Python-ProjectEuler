# -*- coding: utf-8 -*-

import math

numOfCorner = 4
limit = 0.1

def isPrime(n):
	for i in range(2, int(math.sqrt(n))+1):
		if n % i == 0:
			return False
	return True

if __name__=='__main__':
	n = 1
	tot = 1
	cntPrime = 0
	while True:
		n += 2
		tot += numOfCorner
		for i in range(numOfCorner):
			if isPrime(n * n - i * (n - 1)):
				cntPrime += 1
		if cntPrime / tot < limit:
			print(n)
			break