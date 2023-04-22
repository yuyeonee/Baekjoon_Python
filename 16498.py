from itertools import product

a, b, c = map(int, input().split())
nums = []

for i in range(3):
    nums.append(set(map(int, input().split())))

combi = set(product(*nums))
ans = []

for cb in combi:
    d = max(cb) - min(cb)
    ans.append(d)
print(min(ans))
