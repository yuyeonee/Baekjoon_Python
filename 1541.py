s_minus = list(input().split('-'))
num = []

for nums in s_minus:
    num.append(sum(map(int, nums.split('+'))))

answer = num[0]

for i in range(1, len(num)):
    answer -= num[i]
print(answer)