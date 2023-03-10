n = int(input())

num = [0]*(n+1)

num[0] = 0
if n>0:
    num[1] = 1

for i in range(1,n):
    num[i+1] = num[i] + num[i-1]

print(num[n])
