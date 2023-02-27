n = int(input())

num1 = 0
num2 = 1
num3 = 1

for _ in range(n-1):
    num3 = num1 + num2
    num1 = num2
    num2 = num3

print(num3)