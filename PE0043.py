# -*- coding: utf-8 -*-

maxn = 10
checked = 0
ans = 0
a = [1, 2, 3, 5, 7, 11, 13, 17]

def dfs(cur, v, num):
	global checked
	global ans
	if cur == maxn:
		print(num)
		ans += num
		return
	start = 0
	if cur == 1:
		start = 1
	for i in range(start, maxn):
		if checked & (1<<i) == 0:
			if cur < 3 or (cur >= 3 and ((v % 100) * 10 + i) % a[cur - 3] == 0):
				checked ^= 1<<i
				dfs(cur + 1, (v % 100) * 10 + i, num * 10 + i)
				checked ^= 1<<i
if __name__=='__main__':
	dfs(1,0, 0)
	print(ans)