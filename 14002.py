n = int(input())
nums = list(map(int, input().split()))

dp = [1]*n

for i in range(n):
    for j in range(i):
        if nums[i]>nums[j]:
            dp[i] = max(dp[i], dp[j]+1)
            
print(max(dp))
answer = []

cnt = max(dp)
for i in range(dp.index(max(dp)), -1, -1):
    if dp[i]==cnt:
        answer.append(nums[i])
        cnt-=1
print(*reversed(answer))
