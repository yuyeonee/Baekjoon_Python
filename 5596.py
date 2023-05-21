score1 = list(map(int, input().split()))
score2 = list(map(int, input().split()))

print(max(sum(score1), sum(score2)))