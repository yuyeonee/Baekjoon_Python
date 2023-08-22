bridge = [0,1,0,1,0]

people = [[0,1,0,1,0], [0,1,1,0,1], [1,1,1,1,1], [0,1,1,1,1], [0,0,0,0,0], [1,0,1,0,0], [1,1,1,1,1], [0,0,0,0,0], [1,0,1,0,1]]
check = [False]*5
answer = 0

for person in people:
    count = 0
    for i in range(5):
        if check[i]:
            count+=1
        elif bridge[i]!=person[i]:
            check[i]=True
            break
        elif bridge[i]==person[i]:
            count+=1
    if count==5:
        answer+=1

print(answer)