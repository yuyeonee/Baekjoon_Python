import sys

n, m = map(int, input().split())

S = set(sys.stdin.readline().strip() for i in range(n))
T = list(sys.stdin.readline().strip() for i in range(m))

count = 0
for test in T:
    if test in S:
        count += 1

print(count)
