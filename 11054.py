n = int(input())
nums = list(map(int, input().split()))
numsr = list(reversed(nums))

dp1 = [1]*n
dp2 = [1]*n

for i in range(n):
    for j in range(i):
        if nums[i]>nums[j]:
            dp1[i] = max(dp1[i], dp1[j]+1)
    for j in range(i):
        if numsr[i]>numsr[j]:
            dp2[i] = max(dp2[i], dp2[j]+1)

answer = []
dp2.reverse()
for i in range(n):
    answer.append(dp1[i]+dp2[i]-1)
print(max(answer))