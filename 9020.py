import sys

n = int(input())

def is_prime(n):
    if n==1:
        return False
    
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

for i in range(n):
    num = int(sys.stdin.readline().strip())
    mid = num//2
    a, b = mid, mid

    while 1:
        if is_prime(a) and is_prime(b):
            print(a, b)
            break
        a -= 1
        b += 1

