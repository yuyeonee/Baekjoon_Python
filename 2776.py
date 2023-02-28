import sys

T = int(input())

for i in range(T):
    n = input()
    data1 = set(sys.stdin.readline().split()) # set을 써도 될 때는 set을 쓰는 게 훨씬 빠르으으 다
    m = input()
    data2 = list(sys.stdin.readline().split())

    for data in data2:
        if data in data1:
            print(1)
        else:
            print(0)
