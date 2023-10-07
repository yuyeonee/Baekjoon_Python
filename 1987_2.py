from collections import deque

R, C = map(int, input().split())
graph = list(list(input()) for _ in range(R))
visited = [True]*26
visited[ord(graph[0][0])-65] = False

def dfs(a, b, count):
    global max_cnt
    if max_cnt<count:
        max_cnt = count

    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
        nx = a + dx
        ny = b + dy
        if 0<=nx<R and 0<=ny<C and visited[ord(graph[nx][ny])-65]:
            visited[ord(graph[nx][ny])-65] = False
            dfs(nx, ny, count+1)
            visited[ord(graph[nx][ny])-65] = True

    return max_cnt

max_cnt = 1
print(dfs(0, 0, 1))
