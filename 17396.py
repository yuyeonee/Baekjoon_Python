import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
danger = list(map(int, input().split()))
graph = [[] for _ in range(N)]
danger[-1] = 0


for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))


time = [INF]*(N)
time[0] = 0
queue = []
heapq.heappush(queue, (0, 0))

while queue:
    cur_t, st = heapq.heappop(queue)

    if time[st]<cur_t:
        continue

    for next_n, t in graph[st]:
        if danger[next_n]==1:
            continue
        next_t = cur_t + t
        if next_t < time[next_n]:
            time[next_n] = next_t
            heapq.heappush(queue, (next_t, next_n))

print(time)
print(time[N-1] if time[N-1]!=INF else -1)

