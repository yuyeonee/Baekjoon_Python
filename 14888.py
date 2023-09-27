N = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))

def dfs(n, oper, ans):
    if oper==0:
        ans+=nums[n]
    elif oper==1:
        ans-=nums[n]
    elif oper==2:
        ans*=nums[n]
    elif oper==3:
        if ans<0:
            ans = -(abs(ans)//nums[n])
        else:
            ans //= nums[n]
    for i in range(4):
        if operators[i]!=0:
            operators[i]-=1
            dfs(n+1, i, ans)
            operators[i]+=1
    if n==N-1:
        answer.append(ans)
        return
        
answer = []
ans = ''
dfs(0, -1, nums[0])
print(max(answer), min(answer))
