N = int(input())
score = list(list(map(int, input().split())) for _ in range(N))

def dfs(n, alst, blst):
    global ans, N
    if n==N:
        if len(alst)==len(blst):
            m = N//2
            asum , bsum = 0, 0
            for i in range(m):
                for j in range(m):
                    asum += score[alst[i]][alst[j]]
                    bsum += score[blst[i]][blst[j]]
            ans = min(ans, abs(asum-bsum))

    else:
        dfs(n+1, alst+[n], blst)
        dfs(n+1, alst, blst+[n])

'''def cal(alst, blst):
    global N
    m = N//2
    asum , bsum = 0, 0
    for i in range(m):
        for j in range(m):
            asum += score[alst[i]][alst[j]]
            bsum += score[blst[i]][blst[j]]
    return abs(asum-bsum)
'''
alst = []
blst = []
ans = 100*N*N
dfs(0, alst, blst)

print(ans)