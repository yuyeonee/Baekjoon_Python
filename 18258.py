import sys

n = int(input())
temp = []
que = []
point = 0

for i in range(n):
    temp = sys.stdin.readline().split()
    quest = temp[0]
    
    if quest=='push':
        que.append(temp[1])
    
    elif quest == 'front':
        print(que[point] if point<len(que) else -1)
        
    elif quest == 'back':
        print(que[-1] if point<len(que) else -1)
    
    elif quest == 'pop':
        if point<len(que):
            print(que[point])
            point += 1
        else:
            print(-1)
        
    elif quest == 'size':
        print(len(que)-point)

    elif quest == 'empty':
        print(0 if point<len(que) else 1)