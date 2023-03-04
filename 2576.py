import sys

num = [int(input()) for _ in range(7)]
sum = 0
min = 100
for n in num:
    if n%2==1:
        sum += n
        if min>n:
            min = n

if sum==0:
    print(-1)
else:
    print(sum)
    print(min)
