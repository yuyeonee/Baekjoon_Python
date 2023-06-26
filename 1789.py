S = int(input())
sum = 0

if S==1:
    print(1)

for i in range(1, S):
    sum += i
    if i >= (S-sum):
        print(i)
        break
