n = int(input())

left = 0
right = n
answer = 0
while 1:
    mid = (left+right)//2
    if mid*mid < n:
        left = mid
    elif mid*mid > n:
        right = mid
    else:
        answer = mid
        break

print(answer)