import sys

n = int(input())
stack = []

for i in range(n):
    temp = sys.stdin.readline().split()
    cmd = temp[0]

    if cmd=='push':
        stack.append(temp[1])
    elif cmd=='pop':
        print(stack.pop(-1) if stack else -1)
    elif cmd=='size':
        print(len(stack))
    elif cmd=='empty':
        print(0 if stack else 1)
    elif cmd=='top':
        print(stack[-1] if stack else -1)
    
