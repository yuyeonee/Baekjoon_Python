N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
visited = [True]*N

def dfs(m, ans):
    if m==M:
        if ans not in answer:
            answer.append(ans)
            print(*ans)
        return
    
    else:
        if m==0:
            for i in range(len(nums)):
                if visited[i]:
                    visited[i] = False
                    dfs(m+1, ans+[nums[i]])
                    visited[i] = True
        else:
            for i in range(len(nums)):
                if visited[i] and ans[-1]<=nums[i]:
                    visited[i]=False
                    dfs(m+1, ans+[nums[i]])
                    visited[i]=True

answer = []
ans = []
dfs(0, ans)