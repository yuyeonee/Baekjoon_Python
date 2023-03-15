n, m = map(int, input().split())
noh = set(input() for i in range(n))
nos = set(input() for i in range(m))

'''for i in range(m):
    name = input()
    if name in noh:
        answer.append(name)'''

answer = sorted(noh & nos)

print(len(answer))
for name in answer:
    print(name)