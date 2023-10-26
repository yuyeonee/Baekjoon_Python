from collections import deque

N = int(input())
M = int(input())
graph = [[] for _ in range(N)]
nums = list(list(map(int, input().split())) for _ in range(N))
travel = list(map(int, input().split()))
for i in range(N):
    for j in range(N):
        if nums[i][j]==1:
            graph[i].append(j)

def check(i):
    visited = [True]*N
    queue = deque()
    queue.append(i)
    visited[i] = False

    while queue:
        a = queue.popleft()
        for next in graph[a]:
            if visited[next]:
                visited[next] = False
                queue.append(next)
    return visited

poss = [[] for _ in range(N)]
for i in range(N):
    visit = check(i)
    for j in range(N):
        if not visit[j]:
            poss[i].append(j)
    print(poss)

flag = True
for i in range(1, M):
    print(poss[i - 1], travel[i] - 1)
    if travel[i]-1 not in poss[travel[i-1]-1]:
        flag = False
        print(poss[i - 1], travel[i]-1, 'd')
        break

print('YES' if flag else 'NO')

'''5
5
0 1 0 1 0
1 0 0 0 0
0 0 0 0 1
1 0 0 0 0
0 0 1 0 0
2 4 2 4 1
'''