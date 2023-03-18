import sys
n = int(input())
temp = []
que = []

for i in range(n):
    temp = sys.stdin.readline().split()
    quest = temp[0]
    if quest=='push':
        que.append(temp[1])
    
    elif quest == 'front':
        if que:
            print(que[0])
        else:
            print(-1)
    
    elif quest == 'back':
        if que:
            print(que[-1])
        else:
            print(-1)
    
    elif quest == 'pop':
        if que:
            print(que.pop(0))
        else:
            print(-1)
    
    elif quest == 'size':
        print(len(que))

    elif quest == 'empty':
        if que:
            print(0)
        else:
            print(1)
