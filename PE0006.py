# -*- config: utf-8 -*-

def cal(*nums):
    square_sum=0
    for i in nums:
        square_sum += i*i
    sum_square=0
    for i in nums:
        sum_square += i
    sum_square = sum_square * sum_square
    return sum_square - square_sum

# method 1 (start)
nums=range(1,101)
ans=cal(*nums)
# method 1 (end)
ans=cal(*[num for num in range(1,101)]) # method 2
ans=cal(*range(1,101))  # method 3
print(ans)
