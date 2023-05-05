from collections import Counter

x = []
y = []
for i in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

cnt1 = Counter(x)
cnt2 = Counter(y)

print(cnt1.most_common(2)[1][0], cnt2.most_common(2)[1][0])