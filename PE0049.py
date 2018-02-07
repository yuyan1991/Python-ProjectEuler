# -*- coding: utf-8 -*-

maxn = 10000
checked = [False] * maxn
P = []

def cal_prime():
	for i in range(2, maxn):
		if not checked[i]:
			P.append(i)
		for p in P:
			if p*i>=maxn:
				break
			checked[p*i]=True
			if i%p==0:
				break

if __name__=='__main__':
	cal_prime()
	for a in range(1, 10):
		for b in range(a, 10):
			for c in range(b, 10):
				for d in range(c, 10):
					L = [a, b, c, d]
					res = []
				for i in range(4):
					if L[i]!=0:
						for j in range(4):
							if i!=j:
								for k in range(4):
									if i!=k and j!=k:
										l = 6 - i - j - k
										if not checked[L[i]*1000+L[j]*100+L[k]*10+L[l]]:
											res.append(L[i] * 1000 + L[j] * 100 + L[k] * 10 + L[l])
				for i in range(0, len(res)):
					for j in range(i+1, len(res)):
						for k in range(j+1, len(res)):
							if res[k]-res[j]==res[j]-res[i] and res[i]!=res[k]:
								print("%d%d%d"%(res[i],res[j],res[k]))
