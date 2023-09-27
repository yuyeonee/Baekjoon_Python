N = int(input())
num_list = list(map(int, input().split()))
operators = list(map(int, input().split()))

def dfs(n, operator, ans):
    
    
    if operator==0:
        ans+=num_list[n]
    elif operator==1:
        ans-=num_list[n]
    elif operator==2:
        ans*=num_list[n]
    elif operator==3:
        if ans<0:
            ans = -(abs(ans)//num_list[n])
        else:
            ans//=num_list[n]
    if n==N-1:
        answer.add(ans)
        return
    else:
        for i in range(4):
            if operators[i]!=0:
                operators[i]-=1
                dfs(n+1, i, ans)
                operators[i]+=1
    
  

answer = set()
dfs(0, -1, num_list[0])
print(max(answer))
print(min(answer))