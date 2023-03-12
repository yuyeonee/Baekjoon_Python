n = int(input())
num1 = set(map(int, input().split()))

m = int(input())
num2 = list(map(int, input().split()))

answer = []

for num in num2:
    if num in num1:
        answer.append(1)
    else:
        answer.append(0)

print(*answer)