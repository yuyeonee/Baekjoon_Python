N = int(input())
blist = list(input().split())
num_list = [True]*10

def check(prev, cur, buho):
    if buho=='<':
        return int(prev)<cur
    if buho=='>':
        return int(prev)>cur
    return True

def dfs(n, ans):
    global minans, maxans

    if n==N+1:
        if minans=='':
            minans = ans
        else:
            maxans = ans
        
        return

    for i in range(10):
        if num_list[i]:
            if n==0 or check(ans[-1], i, blist[n-1]):
                num_list[i] = False
                #ans += str(i) 진ㅉㅏ 더하지 말고 더한 걸 dfs에 넣기..
                dfs(n+1, ans+str(i))
                num_list[i] = True


'''def dfs(n, prev, ans):
    global num_list
    if n==N+1:
        answer.append(ans)
        return
    print(num_list)
    print(n)
    if n!=0:
        buho = blist[n-1]
        print(buho)
        if buho=='<':
            flag = True
        else:
            flag = False

        for i in range(10):
            if num_list[i]!=0:
                if flag:
                    if prev<i:
                        prev = i
                        ans.append(str(i))
                        num_list[i] = 0
                        print(ans)
                        dfs(n+1, prev, ans)
                        #num_list[i] = 1
                else:
                    if prev>i:
                        prev = i
                        ans.append(str(i))
                        num_list[i]=0
                        print(ans)
                        dfs(n+1, prev, ans)
                        #num_list[i] = 1

    else:
        for i in range(10):
            if num_list[i]!=0:
                prev = i
                ans.append(str(i))
                num_list[i] = 0
                print(n+1, prev, ans)
                dfs(n+1, prev, ans)
                num_list[i] = 1
                '''  

cnt = 0
minans, maxans = '', ''
ans = ''

dfs(0, ans)
print(maxans)
print(minans)
