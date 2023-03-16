n, k = map(int, input().split())
nums = list(i+1 for i in range(n))

count, index = 0, 0
answer = []
while nums:
    if count==k-1:
        answer.append(nums.pop(index))
        count=0
    else:
        count += 1
        index += 1
    
    if index >= len(nums):
        index = 0
    
print('<' + ', '.join(map(str, answer)) + '>')