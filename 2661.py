N = int(input())

def check(ans):
    for i in range(1, (len(ans)//2+1)):
        if ans[-(i):] == ans[-(i*2):-i]: # -로 표현
            return False
    return True

def dfs(n, ans):

    if n==N:
        for a in ans:
            print(a, end='')
        print()
        exit(0) # 그냥 종료

    else:
        if n==0:
            for i in range(1, 4): # for c in '123' 이렇게 풀어도 될 듯 문자열로
                dfs(n+1, ans + [i])
        else:
            for i in range(1, 4):
                if check(ans+[i]):
                    dfs(n+1, ans+[i])

answer = []
ans = []
dfs(0, ans)
