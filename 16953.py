a, b = map(int, input().split())

count = 0
flag = True
while b!=a:
    count+=1
    if b%2==0:
        b //= 2
    elif b%10==1:
        b //= 10
    else:
        flag = False
        break
    
    if b<a:
        flag = False
        break

print(count+1 if flag else -1)