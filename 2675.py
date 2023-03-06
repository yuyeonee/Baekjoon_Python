import sys

N = int(input())

for _ in range(N):
    n, s = sys.stdin.readline().split()
    n = int(n)
    for c in s:
        print(c*n, end='')
    print()

