import sys

n = int(input())
nums = []

for i in range(n):
    num = int(sys.stdin.readline())
    if num!=0:
        nums.append(num)
    else:
        nums.pop(-1)
    
print(sum(nums))