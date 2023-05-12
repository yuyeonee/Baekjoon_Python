import math

n, w, h = map(int, input().split())
wh = math.sqrt(w**2 + h**2)

for i in range(n):
    leng = int(input())
    if leng>wh:
        print('NE')
    else:
        print('DA')
