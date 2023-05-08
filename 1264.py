alp = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
while 1:
    s = input()
    if s=='#':
        break
    count = 0
    for c in s:
        if c in alp:
            count+=1
    print(count)
