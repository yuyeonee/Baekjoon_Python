n = int(input())

for i in range(n):
    nums = list(map(int, input().split(',')))
    print(sum(nums))