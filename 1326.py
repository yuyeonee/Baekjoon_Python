from collections import deque

n = int(input())
nums = list(map(int, input().split()))
a, b = map(int, input().split())

queue = deque() 
queue.append(a-1)

while queue:
    now = queue.popleft()
    
    for jump in 

