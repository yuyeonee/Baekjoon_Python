import sys
from collections import deque

T = int(input())

for _ in range(T):
    n = int(sys.stdin.readline())
    nums = [0] + list(int(sys.stdin.readline()) for _ in range(n))

    queue = deque([1])
    visited = [False]*(n+1)
    cnt = 0

    while queue:
        now = queue.popleft()

        if visited[now]==False:
            visited[now] = True
            queue.append(nums[now])
            cnt += 1  
        if nums[now] == n:
            visited[n] = True
            break
    print(cnt if visited[n] else 0)