import sys

for i in range(3):
    n = int(input())
    nums = []
    for i in range(n):  
        nums.append(int(sys.stdin.readline()))
    if sum(nums)>0:
        print("+")
    elif sum(nums)<0:
        print('-')
    else:
        print(0)