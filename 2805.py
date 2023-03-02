import sys

n, m = map(int, input().split())

trees = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(trees)

while start <= end:
    mid = (start+end)//2
    sum = 0
    for tree in trees:
        if tree > mid:
            sum += (tree-mid)
        if sum > m:
            break
    if sum >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)

