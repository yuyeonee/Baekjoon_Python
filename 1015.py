n = int(input())
nums = list(map(int, input().split()))
new_list = []

for idx, num in enumerate(nums):
    new_list.append([num, idx])

new_list.sort(key = lambda x:x[0])

for i in range(n):
    new_list[i].append(i)

new_list.sort(key = lambda x:x[1])

for i in range(n):
    print(new_list[i][2], end=' ')