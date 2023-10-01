TC = int(input())
opers = [' ', '+', '-']

def cal(exp):
    exp = exp.replace(' ', '')
    oper = []
    for ex in exp:
        if ex in opers:
            oper.append(ex)
    exp = exp.replace('-', '+')
    exp = exp.split('+')
    sum = int(exp[0])
    for i in range(len(oper)):
        if oper[i]=='+':
            sum+=int(exp[i+1])
        elif oper[i]=='-':
            sum-=int(exp[i+1])
    if sum==0:
        return True
    else:
        return False

def dfs(n, ans):
    ans += str(n+1)
    if n==N-1:
        if cal(ans):
            print(ans)
    
    else:
        for i in range(3):
            dfs(n+1, ans+opers[i])


for _ in range(TC):
    N = int(input())
    ans = ''
    dfs(0, ans)
    print()
