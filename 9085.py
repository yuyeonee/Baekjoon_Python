n = int(input())   

for i in range(n):
    c = int(input())
    nums = list(map(int, input().split()))
    print(sum(nums))