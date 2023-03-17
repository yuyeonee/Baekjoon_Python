n, m = map(int, input().split())
nums = list(map(int, input().split()))

count = 0
left = 0
right = 0 
sum = 0
while 1:
    if sum >= m:
        sum -= nums[left]
        left += 1
    elif n == right:
        break
    else:
        sum += nums[right]
        right += 1
    
    if sum == m:
        count += 1

print(count)