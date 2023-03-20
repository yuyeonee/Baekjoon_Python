from itertools import permutations

n, m = map(int, input().split())

nums = list(map(int, input().split()))

combi = permutations(sorted(nums), m)

for nums in combi:
    print(*nums)