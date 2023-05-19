n = int(input())
alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(n):
    s = input()
    sum = 0

    for al in alp:
        if al not in s:
            sum += ord(al)
    print(sum)
