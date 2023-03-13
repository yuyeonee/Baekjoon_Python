n = int(input())
nums = list(map(int, input().split()))

nums.sort(reverse=True)

for i in range(n):
    nums[i] += i+1

print(max(nums)+1)