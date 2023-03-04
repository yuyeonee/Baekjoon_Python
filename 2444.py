n = int(input())

for i in range(-n+1, n):
    print(' '*abs(i) + '*'*(abs(abs(i)-n)*2-1))