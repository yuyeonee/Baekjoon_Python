N = int(input())
nums = [True]*N

def dfs(n, answer):
    if n==N:
        print(*answer)
        return
    
    else:
        for i in range(N):
            if nums[i]:
                nums[i] = False
                dfs(n+1, answer+[i+1])
                nums[i] = True

    

answer = []
dfs(0, answer)