from itertools import combinations

n = int(input())
nums = list(map(int, input().split()))
combi = []
for i in range(1, n+1):
    combi += (list(combinations(nums, i)))

sums = []
for num in combi:
    s = sum(num)
    sums.append(s)

sums = set(sums)
print(sum(nums) - len(sums))



#for i in (min(nums), sum(nums)):
