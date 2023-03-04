n = int(input())

for i in range(-n+1, n):
    print('*'*abs(abs(i)-n) + ' '*(abs(i)*2) + '*'*abs(abs(i)-n))