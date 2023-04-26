n = int(input())
count = 0
for i in range(n):
    s = input()
    char = []
    flag = True
    for c in s:
        if c not in char:
            char.append(c)
        else:
            if char[-1]!=c:
                flag = False
                break
    if flag:
        count += 1

print(count)