from collections import Counter

s = input()
s = s.replace('9', '6')
nums = list(c for c in s)
print(nums)

cnt = Counter(nums)

mc = cnt.most_common(2)
mc.append(('0', 0))

if mc[0][0]=='6':
    if mc[0][1]/2 > mc[1][1]:
        if mc[0][1]%2==0:
            print(mc[0][1]//2)
        else:
            print(mc[0][1]//2+1)
        
    else:
        print(mc[1][1])
else:
    print(mc[0][1])


#print(cnt)
