for i in range(1,10000):
    flag = True
    if i<100:
        for j in range(1,i):
            nums = []
            for s in str(j):
                nums.append(int(s))
            sums = j + sum(nums)
            if sums==i:
                flag = False
                break
    else:
        for j in range(i-9*len(str(i)),i):
            nums = []
            for s in str(j):
                nums.append(int(s))
            sums = j + sum(nums)
            if sums==i:
                flag = False
                break
        
    if flag:
        print(i)
        
        
