import math

m, n = map(int, input().split())
nums = []
for i in range(m, n+1):
    flag = True
    for j in range(2, int(math.sqrt(i))+1):
        if i%j==0:
            flag = False
            break
    if flag:
        if i!=1:
            print(i)
