N = int(input())
graph = list(list(input().split()) for _ in range(N))
teacher = []

for i in range(N):
    for j in range(N):
        if graph[i][j]=='T':
            teacher.append((i,j))


def bfs():
    for a, b in teacher:
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            x, y = a+dx, b+dy
            while 0<=x<N and 0<=y<N:
                if graph[x][y]=='O':
                    break
                if graph[x][y]=='S':
                    return False
                x += dx
                y += dy  
    return True

def dfs(n):
    if n==3:
        for i in range(N):
            #print(*graph[i])
            if bfs():
                print('YES')
                exit(0)
        return
    
    else:
        for i in range(N):
            for j in range(N):
                if graph[i][j]=='X':
                    graph[i][j]='O'
                    dfs(n+1)
                    graph[i][j]='X'

dfs(0)
print('NO')

