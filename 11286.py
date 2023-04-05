import sys
import heapq as hq

n = int(input())
nums = []


for i in range(n):
    x = int(sys.stdin.readline())
    if x==0:
        if nums:
            print(hq.heappop(nums)[1])
        else:
            print(0)
    else:
        hq.heappush(nums, (abs(x), x))

    