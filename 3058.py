n = int(input())

for i in range(n):
    nums = list(map(int, input().split()))
    sum = 0
    min = 100
    for n in nums:
        if n%2==0:
            sum += n
            if min>n:
                min = n
    print(sum, min)