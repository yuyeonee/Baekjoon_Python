from itertools import combinations

n, m = map(int, input().split())

nums = list(i+1 for i in range(n))
combi = list(combinations(nums,m))

for nums in combi:
    print(*nums)