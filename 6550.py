import sys

while True:
    try:
        s, t = sys.stdin.readline().split()
        ind = -1
        flag = True
        for c in s:
            index = t.find(c, ind+1)
            if ind<index:
                ind = index
            else:
                print('No')
                flag=False
                break
        if flag:
            print('Yes')
    except:
        break
