# 10/4 8:34

n, k = map(int, input().split())
'''
a = n
ans = []
for i in range(20, -1, -1):
    temp = 2**i
    if temp <= a:
        print(i, temp)
        m = a%temp
        a = a//temp
        print(i, temp, a, m)

        ans.append(temp*a)
        a = m'''
answer = 0
while bin(n).count('1')>k:
    n += 1
    answer += 1
print(answer)

'''print(ans)
if len(ans)>k:
    print(ans[k-1] - sum(ans[k:]))
else:
    print(0)'''


