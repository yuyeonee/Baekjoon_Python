import sys

n = int(input())
nums = list(int(sys.stdin.readline()) for _ in range(n))
nums.sort(reverse=True)
total = 0

for i in range(0, n-2, 3):
    price = nums[i] + nums[i+1]
    total += price
  
if n%3==1:
    total += nums[-1]
if n%3==2:
    total = total + nums[-1] + nums[-2]

print(total)