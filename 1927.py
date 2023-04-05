import sys
import heapq

n = int(input())
nums = []

for i in range(n):
    x = int(sys.stdin.readline())
    if x==0:
        if nums:
            print(heapq.heappop(nums))
        else:
            print(0)

    else:
        heapq.heappush(nums, x)

