import sys
from collections import deque

def bfs(v):
    dx = [1, -1, 0, 0] # x, y 변화량
    dy = [0, 0, 1, -1]
    queue = deque([v]) # 첫번째 길부터 deque 시작

    while queue:
        a, b = queue.popleft() # 좌표 받기
        cnt = 0

        for i in range(4):
            x = a + dx[i] # 변화 위치 계산
            y = b + dy[i]
            if -1 < x < r and -1 < y < c and graph[x][y]=='.': # 그래프에서 해당 위치가 길인지 확인
                cnt += 1 # 길이면 +1
                if visited[x][y] == False: # 방문한 적 없으면 방문으로 수정
                    visited[x][y] = True
                    queue.append([x,y])
        if cnt < 2: # cnt가 2보다 작으면 막다른 길 발견 -> 함수 종료 1 리턴
            return 1   
    return 0 # 함수 끝날 때까지 cnt가 1인 막다른 길 안 나오면 그대로 0 리턴

r, c = map(int, input().split())
check = [] # 길 리스트
graph = [] # 길 건물 그래프

for i in range(r):
    graph.append(list(map(str, sys.stdin.readline().strip())))
    for j in range(c):
        if graph[i][j]=='.':
            check.append([i, j])

visited = [[False]*c for _ in range(r)] # 방문 여부 False로 초기화

print(bfs(check[0])) # 첫번째 길부터 탐색
