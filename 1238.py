import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))


def dijkstra(start):
    time = [INF]*(N+1)
    time[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        cur_t, st = heapq.heappop(queue)

        if time[st] < cur_t:
            continue

        for next_n, t in graph[st]:
            next_t = cur_t + t
            if time[next_n]>next_t:
                time[next_n] = next_t
                heapq.heappush(queue, (next_t, next_n))
    if start==X:
        return time[X], time[1:]
    return time[X]

times = []
index = -1
X_time = []
for i in range(1, N+1):
    if i==X:
        t, time = dijkstra(i)
        times.append(t)
        X_time = time
    else:
        times.append(dijkstra(i))

ans = 0
for i in range(N):
    if ans<(times[i]+X_time[i]):
        ans = times[i]+X_time[i]
print(ans)


