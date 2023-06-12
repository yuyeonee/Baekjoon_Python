'''s1 = input()
s2 = input()    

dp = [0]*len(s1)
maxi = 0
for i in range(len(s1)):
    if s1[i] in s2:
        print(s1[i])
        maxi = max(dp)
        print(maxi)
        print(s1[i-maxi:i+1])
        print(dp)
        if s1[i-maxi:i+1] in s2:
            dp[i] = max(max(dp)+1, dp[i])
            print(s1[i-maxi:i+1] )
        print(dp)

print(max(dp))'''

s1 = input()
s2 = input()    

dp = [0]*len(s1)
maxi = 0
for i in range(len(s1)):
    if s1[i] in s2:
        maxi = max(dp)
        if s1[i-maxi:i+1] in s2:
            dp[i] = max(max(dp)+1, dp[i])

print(max(dp))
