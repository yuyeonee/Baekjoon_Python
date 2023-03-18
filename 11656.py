s = input()

tale = sorted(list(s[i:] for i in range(len(s))))

for s in tale:
    print(s)
