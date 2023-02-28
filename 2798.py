import sys

n, m = map(int, input().split())

number  = list(map(int, sys.stdin.readline().split()))

sum=[]

for i in range(len(number)):
    for j in range(i+1, len(number)):
        for k in range(j+1, len(number)):
            sum.append(number[i] + number[j] + number[k])

sum.sort()
sum.reverse()

for c in sum:
    if c<=m:
        print(c) 
        break
