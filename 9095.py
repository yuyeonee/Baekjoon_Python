import sys

def dfs(sum, num):
    global cnt

    if sum > num:
        return

    if sum == num:
        cnt += 1

    for i in range(1,4):
        dfs(sum+i, num)



if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        cnt = 0
        num = int(sys.stdin.readline().strip())
        dfs(0, num)
        print(cnt)