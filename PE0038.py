# -*- coding -*-

maxn = 100000
maxm = 10

def cal(x):
	checked = [False] * maxm
	res = ''
	okay = False
	for i in range(1, maxm):
		k = x * i
		for s in str(k):
			if s=='0':
				return -1
			if checked[ord(s) - 48]:
				return -1
			checked[ord(s) - 48] = True
		res += str(k)
		if len(res) == maxm - 1:
			return int(res)
	return -1

if __name__=='__main__':
	ans=0
	for i in range(maxn):
		ans = max(ans, cal(i))
	print(ans)
