k, n = map(int, input().split())
num = list(i for i in range(1,k+1))

index, count = 0, 0
answer = []
while num:
    if count==n-1:
        answer.append(num.pop(index))
        count = 0
    else:
        count += 1
        index += 1
    if index>=len(num):
        index = 0

print("<" + ', '.join(map(str, answer)) + ">")