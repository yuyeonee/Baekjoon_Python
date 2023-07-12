import sys

n = int(input())
rows = []
mini= 10000

for i in range(n):
    row = int(sys.stdin.readline())
    rows.append(row)

rows.sort()
rows.reverse()
print(rows)

dp = rows[:] 

for i in range(1, n):
    dp[i] = max(dp[i]*(i+1), dp[i-1])

print(max(dp))