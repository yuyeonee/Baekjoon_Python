n = int(input())
fac = 1

for i in range(2,n+1):
    fac *= i
    while True:
        if str(fac)[-1]=='0':
            fac = fac//10   
        else:
            break     
    fac %= 1000000000000 # 중간에 0이 여러번 나오는 경우가 있을 수 있으니까 이게 충분히 길어야하는 듯? 아니? 몰라

print(str(fac)[-5:])