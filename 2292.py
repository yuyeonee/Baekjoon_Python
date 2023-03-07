n = int(input())

count = 1
check = 1
# 1 7 19 37 61
while n!=1:
    check += 6*count
    count += 1

    if check>=n:
        break
    
print(count)