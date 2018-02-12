# -*- coding: utf-8 -*-

maxn = 1000000

if __name__=='__main__':
	# print(sorted(str(maxn)))
	# print(sorted(str(maxn)) == list(['0', '0', '0', '0', '0', '0', '1']))
	# print(sorted(str(maxn)) == sorted(str(1000000)))
	for i in range(1, maxn):
		origin = sorted(str(i))
		okay = True
		for j in range(2, 7):
			if origin != sorted(str(i*j)):
				okay = False
				break
		if okay:
			print(i)
			break
