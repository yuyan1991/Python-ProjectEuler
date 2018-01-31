# -*- coding: utf-8 -*-

if __name__=='__main__':
	limit = 3000
	S = set()
	n = 1
	ans =  1 << 30
	okay = False
	while n <= limit:
		m = n*(3*n-1)//2
		for s in S:
			if (m-s) in S and abs(2*s-m) in S and abs(2*s-m)<ans:
				ans = abs(2*s-m)
				okay = True
		if okay:
			break
		S.add(m)
		n += 1
	print(ans)