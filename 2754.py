sc = input()
score = 0.0

for s in sc:
    if s=='A':
        score += 4
    elif s=='B':
        score += 3
    elif s=='C':
        score += 2
    elif s=='D':
        score += 1
    elif s=='F':
        score += 0
    elif s == '+':
        score += 0.3
    elif s == '-':
        score -= 0.3

print(score)
