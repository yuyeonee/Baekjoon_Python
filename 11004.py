k, n = map(int, input().split())
num = list(map(int, input().split()))

num.sort()

print(num[n-1])