N = int(input())
nums = list(map(int, input().split()))
iters = list(map(int, input().split()))
iters_r = ['+', '-', '*', '//']

def dfs(n, ans):
    ans += str(nums[n])

    if n==N-1:
        #print(ans, 'd')
        answer.append(eval(ans))
        return
    
    for i in range(4):
        if iters[i]!=0:
            iters[i]-=1
            dfs(n+1, ans+iters_r[i])
            iters[i]+=1

answer = []
ans = ''
dfs(0, ans)
print(max(answer))
print(min(answer))