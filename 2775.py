T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    floor = []
    floor = [i for i in range(1,n+1)] # 이렇게 해보자

    for j in range(k):
        #answer = [1]
        #sum = 1
        for i in range(n-1):
            floor[i+1] += floor[i]
            #sum += floor[i+1]
            #answer.append(sum)
        #floor=answer
    print(floor[-1])
        
