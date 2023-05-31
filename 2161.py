n = int(input())

nums = list(i for i in range(1, n+1))

flag = True
answer = []

while nums:
    if flag:
        answer.append(str(nums.pop(0)))
        flag = False

    else:
        nums.append(nums.pop(0))
        flag = True

print(*answer)
