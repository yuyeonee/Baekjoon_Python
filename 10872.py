n = int(input())
fac = n
for i in range(1,n):
    fac = fac*(n-i)
if n==0:
    print(1)
else:
    print(fac)
