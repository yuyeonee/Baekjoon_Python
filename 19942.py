N = int(input())
satisfy = list(map(int, input().split()))
food = list(list(map(int, input().split())) for i in range(N))

def dfs(n, ans, choice, price, st):
    global best_price, best_choice, flag
    if ans[0]>=satisfy[0] and ans[1]>=satisfy[1] and ans[2]>=satisfy[2] and ans[3]>=satisfy[3]:
        if price<best_price:
            best_price = price
            best_choice = choice[:]
            flag = True
        return
    if n==N:
        return
    if price>best_price:
        return
    
    for i in range(st, N):
        if best_price>=(price+food[i][-1]):
            for j in range(4):
                ans[j]+=food[i][j]
            dfs(n+1, ans, choice+[i+1], price+food[i][-1], i+1)
            for j in range(4):
                ans[j]-=food[i][j]

flag = False
choice = []
best_choice = []
best_price = 500*N
ans = [0]*4
dfs(0, ans, choice, 0, 0)
if flag:
    print(best_price)
    print(*best_choice)
else:
    print(-1)