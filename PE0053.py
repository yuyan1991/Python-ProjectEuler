# -*- coding: utf-8 -*-

maxn = 101
limit = 1000000

c = [[0 for i in range(maxn)] for i in range(maxn)]
ans = 0

if __name__=='__main__':
    c[1][0] = c[1][1] = 1
    for i in range(2, maxn):
        c[i][0]=1
        for j in range(1, i+1):
            c[i][j] = c[i-1][j-1] + c[i-1][j]
            print('(%d, %d) = %d'%(i,j,c[i][j]))
            if c[i][j] > limit:
                ans+=1
    print(ans)
