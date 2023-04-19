import sys
from collections import Counter

n, m = map(int, input().split())
words = list(sys.stdin.readline().rstrip() for i in range(n))

cnt = Counter(words)
common = cnt.most_common()
common.sort(key=lambda x:(-x[1], -len(x[0]), x[0]))

for word in common:
    if len(word[0])>=m:
        print(word[0])