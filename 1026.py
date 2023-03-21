n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)
mul=[]
for i in range(n):
    mul.append(a[i]*b[i])

print(sum(mul))