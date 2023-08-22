from collections import deque

n = int(input())

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

for _ in range(n):
    I = int(input())
    graph = [[-1]*I for _ in range(I)]
    a, b = map(int, input().split())
    x, y = map(int, input().split())
    graph[a][b] = 0
    queue = deque()
    queue.append([a, b])

    if a==x and b==y:
        print(0)
        pass

    while queue:
        a, b = queue.popleft()

        for i in range(8):
            n = a + dx[i]
            m = b + dy[i]

            if -1<n<I and -1<m<I and graph[n][m]==-1:
                graph[n][m]  = graph[a][b] + 1
                queue.append([n, m])
                if n==x and m==y:
                    print(graph[n][m])
                    break






