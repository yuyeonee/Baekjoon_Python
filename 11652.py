import sys
from collections import Counter

n = int(input())
nums = []

for i in range(n):
    nums.append(int(sys.stdin.readline().strip()))

c = Counter(nums)
ans = c.most_common()
ans.sort(key=lambda x:(-x[1], x[0]))

print(ans[0][0])
