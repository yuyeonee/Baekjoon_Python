import sys

n = int(input())
list = []

for i in range(n):
    list.append(int(sys.stdin.readline()))
    #list.append(int(input()))

list.sort()

for num in list:
    print(num)
