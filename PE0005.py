# coding: utf-8 -*-
x=2520
while True:
    okay=True
    for i in [num for num in range(2,21)]:
        if x%i>0:
            okay=False
            break
    if okay:
        print(x)
        break
    x+=2520 # we increased by 2520 to fasten the speed of finding the solution
