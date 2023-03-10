n = int(input())
point = []
for _ in range(n):
    point.append(list(map(int, input().split())))

point.sort(key=lambda x:(x[1], x[0]))

for per in point:
    print(per[0], per[1])