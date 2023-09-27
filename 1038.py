k = int(input())

def dfs(n, ans):
    
    if n==0:
        for i in range(10):
            answer.append(i)
            dfs(n+1, ans+str(i))

    else:
        for i in range(10):
            if int(ans[-1])>i:
                answer.append(int(ans+str(i)))
                dfs(n+1, ans+str(i))

ans = ''
answer = []
dfs(0, ans)
answer.sort()
print(answer[k] if k<len(answer) else -1)