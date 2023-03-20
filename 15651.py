from itertools import product

n, m = map(int, input().split())

num = list(i+1 for i in range(n))
nums=[]
for i in range(m):
    nums.append(num)
combi = list(product(*nums))

for nums in combi:
    print(*nums)