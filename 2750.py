n = int(input())
list = []

for i in range(0,n):
    list.append(int(input()))

list.sort()

for num in list:
    print(num)
