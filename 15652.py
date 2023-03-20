from itertools import combinations_with_replacement as cwr

n, m = map(int, input().split())

num = list(i+1 for i in range(n))
combi = list(cwr(num,m))

for nums in combi:
    print(*nums)


