n = int(input())

for i in range(-n+1, n):
    print(' '*abs(abs(i)-n+1) + '*'*(abs(i)*2+1))