from collections import Counter

angles = [int(input()) for i in range(3)]
cnt = Counter(angles)

if sum(angles)!=180:
    print('Error')
elif cnt.most_common(1)[0][1]==3:
    print('Equilateral')
elif cnt.most_common(1)[0][1]==2:
    print('Isosceles')
else:
    print('Scalene')

