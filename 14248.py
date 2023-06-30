from collections import deque

n = int(input())
nums = list(map(int, input().split()))
s = int(input()) - 1

queue = deque()
queue.append(s)

check = [0]*(n)
check[s] = 1
answer = 1

while queue:
    now = queue.popleft()

    for jump in [-nums[now], nums[now]]:
        temp = now + jump
        if 0 <= temp < n and check[temp]==0:
            check[temp] = 1
            queue.append(temp)
            answer += 1
        
print(answer)