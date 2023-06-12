n = int(input())
flag = False

for i in range(n//5, -1, -1):
    cnt = i
    r = n
    if i!=0:
        r = n - 5*i
    if r%3==0:
        cnt += r//3
        flag = True
        break


print(cnt if flag else -1)