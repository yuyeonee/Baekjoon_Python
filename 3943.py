import sys

num = int(input())

for i in range(num):
    n = int(sys.stdin.readline())
    max = n

    while n!=1:
        if n%2==0:
            n //= 2
        else:
            n = n*3 + 1
        if n>max:
            max = n
    print(max)
        
        