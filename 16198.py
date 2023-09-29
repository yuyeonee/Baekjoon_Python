N = int(input())
energy = list(map(int, input().split()))

def dfs(n, ans):
    if len(energy)==2:
        answer.append(ans)
        return
    
    else:
        for i in range(1, len(energy)-1):
            eg = energy[i-1]*energy[i+1]
            temp = energy.pop(i)
            dfs(n+1, ans+eg)
            energy.insert(i, temp)
ans=0
answer = []
dfs(0, ans)
print(max(answer))
