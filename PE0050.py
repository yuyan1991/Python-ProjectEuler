# -*- coding: utf-8 -*-

maxm = 1000000
maxn = 1000000

checked = [False] * maxn
P = []
S = []

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

if __name__=='__main__':
	cal_prime()
	s = 0
	for p in P:
		s+=p
		S.append(p)
	cnt = ans = 0
	for i in range(0, len(S)):
		for j in range(i + cnt, len(S)):
			if S[j]-S[i]+P[i]<maxm and j-i+1>cnt and not checked[S[j]-S[i]+P[i]]:
				cnt = j-i+1
				ans = S[j] - S[i] + P[i]
	print("%d:%d"%(ans, cnt))
