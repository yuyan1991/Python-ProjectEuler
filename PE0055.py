# -*- coding: utf-8 -*-

maxn = 10000
numOfIterations = 50 + 1

if __name__=='__main__':
	ans=0
	for number in range(maxn):
		n = number
		okay = True
		for j in range(numOfIterations):
			if str(n)==str(n)[::-1]:
				okay = False
				break
			n = n + int(str(n)[::-1])
		ans += okay
	print(ans)
	# print(int(str(ans)[::-1]))