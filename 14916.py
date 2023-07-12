n = int(input())
cnt1 = 0
cnt2 = 0

for i in range(n//5, -1, -1):
    num = n - i*5
    cnt1 = i
    if num%2==0:
        cnt2 = num//2
        break
    else:
        pass

if cnt1==0 and cnt2==0:
    print(-1)
else:
    print(cnt1+cnt2)