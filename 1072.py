x, y = map(int, input().split())
z = int(y/x*100)

left = 1
right = 1000000000
ans = 0

if z>=99:
    print(-1)
else:
    while left<=right:
        mid = (left+right)//2
        newz = int((y+mid)/(x+mid)*100)
        if newz > z:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    print(ans)