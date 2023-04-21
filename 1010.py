n = int(input())

def factorial(n):
    fac = 1
    for i in range(1, n+1):
        fac*=i
    return fac


for i in range(n):
    a, b = map(int, input().split())
    combi = factorial(b) // factorial(b-a) // factorial(a)
    print(combi)