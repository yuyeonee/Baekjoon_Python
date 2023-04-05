import sys
import heapq as hq

n = int(input())
nums = []

for i in range(n):
    x = int(sys.stdin.readline())
    
    if x==0:
        if nums:
            print(-hq.heappop(nums))
        else:
            print(0)
    else:
        hq.heappush(nums, -x)
    
