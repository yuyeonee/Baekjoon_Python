n, m = map(int, input().split())
whole = []
one = []

for i in range(m):
    a, b = map(int, input().split())
    whole.append(a)
    one.append(b)

print(min((n//6)*min(whole) + (n%6)*min(one), (n//6+1)*min(whole), n*min(one)))
