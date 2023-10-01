from itertools import permutations

N, M = map(int, input().split())
nums = list(map(int, input().split()))

combi = list(set(permutations(nums, M)))
combi.sort()

for comb in combi:
    print(*comb)