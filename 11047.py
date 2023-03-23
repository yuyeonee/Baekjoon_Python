n, k = map(int, input().split())

coins = sorted(list(int(input()) for i in range(n)), reverse=True)
count = 0

for coin in coins:
    if coin<=k:
        cnt = k//coin
        k %= coin
        count += cnt
    if k==0:
        break

print(count)
