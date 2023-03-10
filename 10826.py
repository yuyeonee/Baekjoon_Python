n = int(input())

num = [0]*(n+1)

num[0] = 0
num[1] = 1

for i in range(1,n):
    num[i+1] = num[i] + num[i-1]

if n>1:
    print(num[n])
else:
    print(n)