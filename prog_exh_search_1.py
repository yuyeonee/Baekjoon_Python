import math

def solution(numbers):


    def is_prime(num):
        if num == 0 or num == 1:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True


    def dfs(dep, ans):        

        if dep!=0 and is_prime(int(ans)):
            if int(ans) not in answer:
                answer.append(int(ans))

        for i in range(n):
            if visited[i]:
                visited[i]=False
                dfs(dep + 1, ans+numbers[i])
                visited[i]=True


    answer = []
    n = len(numbers)
    visited = [True]*n
    dfs(0, '')


    return len(answer)
