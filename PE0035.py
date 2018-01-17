#-*- coding: utf-8 -*-

maxn = 1000000
P = set([2])

def prime_generator(high):
    for n in range(3, high, 2):
        okay = True
        for p in P:
            if n % p == 0:
                okay = False
                break
        if okay:
            yield n

if __name__=='__main__':
	for n in prime_generator(maxn):
		P.add(n)
	ans=0
	for p in P:
		l = len(str(p))
		x = p
		while True:
			x = (x%10)*10**(l-1)+x//10
			if not (x in P):
				break
			if x == p:
				break
		if x==p:
			ans+=1
			print(p, end=' ')
	print('')
	print(ans)
