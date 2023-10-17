n = int(input())
dict = {}
names = set()
for i in range(n):
    name = input()
    if name not in names:
        names.add(name)
        dict[name] = 1
    else:
        dict[name] += 1

dict = sorted(dict.items(), key = lambda x : [-x[1], x[0]])
print(dict[0][0])