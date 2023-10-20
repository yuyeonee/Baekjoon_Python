s = input()

dic = {')':'(', ']':'[', '(':'', '[':''}
state = []

def score(str, sc):
    if str==')':
        return sc*2
    if str==']':
        return sc*3
    return 0

sc = 1
answer = 0
temp = []
for i in range(len(s)):
    if not state:
        state.append(s[i])
        continue

    if dic[s[i]] == state[-1]:
        state.pop()

        if not state:
            answer += score(s[i], sum(temp))
            temp = []
            sc = 1
            continue
        if sc!=1:
            temp.pop()
        sc = score(s[i], sc)
        temp.append(sc)
    else:
        state.append(s[i])
        sc = 1

print(answer if not state else 0)