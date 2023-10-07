import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

# 1 - v1- v2- N, 1-v2-v1-N
def dijkstra(start):
    distance = [INF]*(N+1)
    distance[start] = 0 #멍청아
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        dist, st = heapq.heappop(queue)

        if distance[st] < dist:
            continue

        for next_n, d in graph[st]:
            next_d = dist + d
            if next_d < distance[next_n]:
                distance[next_n] = next_d
                heapq.heappush(queue, (next_d, next_n))

    return distance


st_dist = dijkstra(1)
v1_dist = dijkstra(v1)
v2_dist = dijkstra(v2)

way1 = st_dist[v1] + v1_dist[v2] + v2_dist[N]
way2 = st_dist[v2] + v2_dist[v1] + v1_dist[N]

print(min(way1, way2) if min(way1, way2)<INF else (-1))
