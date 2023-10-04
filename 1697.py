# 10/4 9:46
from collections import deque

N, K = map(int, input().split())
visited = [True]*1000000

queue = deque()
queue2 = deque()
if N==K:
    print(0)
elif N>K:
    print(N-K)
else:
    queue.append([N,0])

flag = False
while queue:
    n, dep = queue.popleft()
    num_list = [2*n, n+1, n-1]
    for nn in num_list:
        if 0<=nn<=100000:
            if nn==K:
                flag = True
                print(dep+1)
                break
            if visited[nn]:
                queue.append([nn, dep+1])
                visited[nn] = False
    if flag:
        break
    

