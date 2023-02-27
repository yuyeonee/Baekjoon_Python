s1 = input()
s2 = s1.lower()
answer = ''

for i in range(len(s1)):
    if(s1[i]==s2[i]):
        answer += s2[i].upper()
    else:
        answer += s2[i]

print(answer)