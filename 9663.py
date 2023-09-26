N = int(input())

def backtracking(n):
    global ans

    if n==N:
        ans += 1
        return
    
    for i in range(N):
        if v1[i]==v2[n+i]==v3[n-i]==0:
            v1[i]=v2[n+i]=v3[n-i]=1
            backtracking(n+1)
            v1[i]=v2[n+i]=v3[n-i]=0


ans = 0 
v1 = [0]*N
v2 = [0]*(2*N)
v3 = [0]*(2*N)
backtracking(0)
print(ans)