n = int(input())
info = []
for _ in range(n):
    info.append(list(input().split()))

info.sort(key=lambda a:int(a[0]))

for per in info:
    print(per[0], per[1])
