from collections import Counter

s = input().upper()

slist = list(c for c in s)
count = Counter(slist)

if len(s)==1:
    print(s)
elif count.most_common(2)[0][1] == count.most_common(2)[1][1]:
    print('?')
else:
    print(count.most_common(1)[0][0])

