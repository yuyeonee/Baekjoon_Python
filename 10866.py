import sys

n = int(input())
deq = []

for i in range(n):
    temp = sys.stdin.readline().split()
    cmd = temp[0]

    if cmd=='push_front':
        deq.insert(0, temp[1])
    elif cmd=='push_back':
        deq.append(temp[1])
    elif cmd=='pop_front':
        print(deq.pop(0) if deq else -1)
    elif cmd=='pop_back':
        print(deq.pop() if deq else -1)
    elif cmd=='size':
        print(len(deq))
    elif cmd=='empty':
        print(0 if deq else 1)
    elif cmd=='front':
        print(deq[0] if deq else -1)
    elif cmd=='back':
        print(deq[-1] if deq else -1)
    