'''
n1, n2, n3 = map(int, input().split())

if n1>n2:
    temp = n1
    n1 = n2
    n2 = temp

if n2>n3:
    temp = n2
    n2 = n3
    n3 = temp

if n1>n2:
    temp = n1
    n1 = n2
    n2 = temp'''

num = list(map(int, input().split()))

num.sort()

print(*num)