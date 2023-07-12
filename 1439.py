s = input() 

s0 = s.replace('1', ' ').split()
s1 = s.replace('0', ' ').split()

if len(s0)<len(s1):
    print(len(s0))
else:
    print(len(s1))