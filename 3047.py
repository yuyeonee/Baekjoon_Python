nums = list(map(int, input().split()))
alp = input()

nums.sort()
ans = []
for al in alp:
    if al=='C':
        ans.append(nums[2])
    elif al=='B':
        ans.append(nums[1])
    else:
        ans.append(nums[0])
print(*ans)