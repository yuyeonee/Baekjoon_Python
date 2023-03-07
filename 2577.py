mul = 1
for _ in range(3):
    mul *= int(input())

num = list(c for c in str(mul))

count = [0,0,0,0,0,0,0,0,0,0]
for n in num:
    for i in range(10):
        if int(n) == i:
            count[i] += 1

for i in range(10):
    print(count[i]) 