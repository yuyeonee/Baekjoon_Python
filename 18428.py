N = int(input())
graph = list(list(input().split()) for _ in range(N))
teacher = []

for i in range(N):
    for j in range(N):
        if graph[i][j]=='T':
            teacher.append([i,j])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    for a, b in teacher:
        flag = [True]*4
        cnt=0
        while cnt<N:
            for i in range(4):
                if flag[i]:
                    x = a+dx[i]*cnt
                    y = b+dy[i]*cnt
                    if 0<=x<N and 0<=y<N and graph[x][y]=='S':
                        return False
                    if 0>x or x>=N or 0>y or y>=N or graph[x][y]=='O':
                        flag[i]=False
            cnt+=1
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

