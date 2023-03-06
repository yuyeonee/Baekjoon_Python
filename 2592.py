import sys
from collections import Counter

num = list(int(input()) for _ in range(10))
count = Counter(num)
print(sum(num)//10)
print(count.most_common(1)[0][0])