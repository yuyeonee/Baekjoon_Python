import math

N = int(input())
sosu = [2, 3, 5, 7]

def is_prime(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def dfs(n, ans):
    if n==0:
        for num in sosu:
            dfs(n+1, ans+str(num))
    else:
        if n==N:
            print(ans)
            return
        else:
            for i in range(10):
                if is_prime(int(ans+str(i))):
                    dfs(n+1, ans+str(i))
    
ans = ''
dfs(0, ans)