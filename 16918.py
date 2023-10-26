from collections import deque

r, c, n = map(int, input().split())
graph = list(list(input()) for _ in range(r))

def find_bomb():
    for i in range(r):
        for j in range(c):
            if graph[i][j]=='O':
                bomb.append((i,j))

def set_bomb():
    for i in range(r):
        for j in range(c):
            graph[i][j]='O'

def explode():
    while bomb:
        a, b = bomb.popleft()
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1),(0,0)]:
            nx, ny = a+dx, b+dy
            if 0<=nx<r and 0<=ny<c:
                graph[nx][ny] = '.'

bomb = deque()
for i in range(1, n):
    if i%2==1:
        find_bomb()
        set_bomb()
    else:
        explode()

for i in range(r):
    print(''.join(graph[i]))






