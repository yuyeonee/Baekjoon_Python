n = int(input())

nums = list(map(int, input().split()))

nums.sort()

sum = 0
newlist = []
print(nums)

flag = True
for i in range(n//2):
    if flag:
        newlist.insert(0,nums[i])
        newlist.append(nums[n-1-i])
        print(newlist)
        flag=False 
    else:
        newlist.insert(0,nums[n-1-i])
        newlist.append(nums[i])
        print(newlist)
        flag=True

if n%2==1:
    if abs(newlist[0]-nums[n//2])>abs(newlist[-1]-nums[n//2]):
        newlist.insert(0,nums[n//2])
    else:
        newlist.append(nums[n//2])

print(newlist)

for i in range(n-1):
    sum += abs(newlist[i]-newlist[i+1])
print(sum)
