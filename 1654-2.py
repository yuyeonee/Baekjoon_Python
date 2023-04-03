import sys

k, n = map(int, input().split())

lengths = [int(sys.stdin.readline().strip()) for i in range(k)]

left = 1
right = max(lengths)

while left<=right:
    sum = 0
    mid = (left+right)//2
    for leng in lengths:
        sum += leng//mid
    
    if sum>=n:
        left = mid + 1
    else:
        right = mid - 1

print(right)