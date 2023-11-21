S = input()

cnt0 = S.count('0')
cnt1 = S.count('1')

S = S.replace('1', '', cnt1//2)
S = list(reversed(S))

S = ''.join(S)
S = S.replace('0', '', cnt0//2)

S = list(reversed(S))
print(''.join(S))
