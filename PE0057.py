# -*- coding: utf-8 -*-

maxn = 1000

ans=0

if __name__=='__main__':
	x,y = 1,2
	for i in range(maxn):
		if len(str(x+y))>len(str(y)):
			ans += 1
		x+=2*y
		x,y=y,x
		# print(x+y,y)
	print(ans)
