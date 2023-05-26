import sys
from collections import Counter

n = int(input())
names = list(sys.stdin.readline().strip() for i in range(2*n-1))
cname = Counter(names)

cn = cname.most_common()

for name in cn:
    if name[1]%2==1:
        print(name[0])