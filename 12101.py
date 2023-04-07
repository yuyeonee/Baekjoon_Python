
def DFS(idx, sum, check):
    global cnt
    if sum > n:
        return

    if sum == n:
        cnt += 1
        if cnt == k:
            print(''.join(check)[:-1])
            exit(0)

    for i in range(1, 4):
        check.append(str(i)+ '+')
        DFS(idx+1, sum+i, check)
        check.pop()



if __name__ == '__main__':
    cnt = 0
    n, k = map(int, input().split())
    DFS(0, 0, [])
    print(-1)
